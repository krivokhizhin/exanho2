import concurrent.futures
import datetime
import io
import logging
import zipfile
import queue
from collections import defaultdict, namedtuple
from multiprocessing import JoinableQueue
from ftplib import FTP
from multiprocessing import shared_memory
from sqlalchemy import text

from exanho.orm.sqlalchemy import Sessional
from exanho.core.manager_context import Context as ExanhoContext
from exanho.core.common import Error, get_used_memory_level
from exanho.ftp_loading.model import FtpContentStatus, FtpFileStatus, FtpContent, FtpFile

log = logging.getLogger(__name__)

ERROR_FTP_LABEL = object()
ERROR_UNKNOWN_LABEL = object()

Context = namedtuple('Context', [
    'ftp_host', 
    'ftp_port', 
    'ftp_user', 
    'ftp_password',
    'parse_queues',
    'queue_by_filter',
    'parse_filters',
    'max_mem_level',
    'with_swap',
    'max_pool_workers',
    'executor',
    'error_attempts',
    'attemp_count',
    'block_timeout'
    ], defaults=[[], [], [], 0.8, False, 20, None, 60, 1, 60])

ContentData = namedtuple('ContentData', ['name', 'crc', 'size', 'last_modify', 'message'])
ParseContent = namedtuple('ParseContent', ['id', 'archive_date', 'archive_name', 'date', 'name'])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    if len(context.parse_queues) != len(context.queue_by_filter):
        raise RuntimeError(f'The number of "parse_queues" and "queue_by_filter" must match ({len(context.parse_queues)}!={len(context.queue_by_filter)})')

    if sum(context.queue_by_filter) != len(context.parse_filters):
        raise RuntimeError(f'The sum of "queue_by_filter" and number of "parse_filters" must match ({sum(context.queue_by_filter)}!={len(context.parse_filters)})')
    
    parse_queues = dict()
    for parse_queue_name in context.parse_queues:
        parse_queues[parse_queue_name] = exanho_context.joinable_queues[parse_queue_name]

    queue_by_filter = dict()
    queue_num = 0
    counter = context.queue_by_filter[queue_num]
    filter_count = len(context.parse_filters)
    for index, parse_filter in enumerate(context.parse_filters):
        queue_name = context.parse_queues[queue_num]
        queue_by_filter[parse_filter] = queue_name
        if index+1 < filter_count and index+1 == counter:
            queue_num += 1
            counter += context.queue_by_filter[queue_num]

    parse_filters = '({})'.format(' or '.join(["ftp_load_file.filename like '%{}%'".format(parse_filter) for parse_filter in context.parse_filters])) if context.parse_filters and ('' not in context.parse_filters) else None

    context = context._replace(parse_queues=parse_queues, queue_by_filter=queue_by_filter, parse_filters=parse_filters)
    log.debug(context.parse_queues)
    log.debug(context.queue_by_filter)
    log.debug(context.parse_filters)

    if context.max_mem_level > 1:
        max_mem_level = context.max_mem_level / 100.0
        if max_mem_level > 1:
            raise Error('Invalid "max_mem_level" value: must be 0..1 or 0..100')
        context = context._replace(max_mem_level=max_mem_level)

    executor = concurrent.futures.ThreadPoolExecutor(context.max_pool_workers)
    context = context._replace(executor=executor)

    log.info(f'initialize')
    return context

def work(context:Context):
    log.debug('file_load in work')

    try:
        while True:
            used_mem_level = get_used_memory_level(context.with_swap)
            if used_mem_level > context.max_mem_level:
                log.warning(f'Allowed memory usage level ({context.max_mem_level:.1%}) exceeded: {used_mem_level:.1%}')
                break

            futures = set()
            with Sessional.domain.session_scope() as session:
                load_file_ids = []

                query_ = session.query(FtpFile).filter(FtpFile.status == FtpFileStatus.READY)
                if context.parse_filters:
                    query_ = query_.filter(text(context.parse_filters))
                
                for load_file in query_.order_by(FtpFile.date, FtpFile.filename).limit(context.max_pool_workers):
                    load_file.status = FtpFileStatus.LOADING
                    future = context.executor.submit(ftp_loading, context.ftp_host, context.ftp_port, context.ftp_user, context.ftp_password, load_file.id, load_file.filename, load_file.directory, load_file.date)
                    futures.add(future)
                    log.info(f'load_file({load_file.id}): {load_file.status}')
                    load_file_ids.append(load_file.id)

                session.flush()

                query_ = session.query(FtpFile.id, FtpContent.status).select_from(FtpFile).join(FtpContent).filter(FtpFile.status == FtpFileStatus.LOADING)
                if context.parse_filters:
                    query_ = query_.filter(text(context.parse_filters))

                file_statuses = query_.all()
                statuses_by_archive = defaultdict(list)
                for file_id, file_status in file_statuses:
                    if file_id in load_file_ids:
                        continue
                    statuses_by_archive[file_id].append(file_status)

                for file_id, statuses in statuses_by_archive.items():
                    statuses_set = set(statuses)
                    if (len(statuses_set) == 1) and (FtpContentStatus.PROCESSED in statuses_set):
                        done_file = session.query(FtpFile).get(file_id)
                        done_file.status = FtpFileStatus.DONE
                        done_file.err_desc = None
                        log.info(f'load_file({done_file.id}): {done_file.status}')
                    elif FtpContentStatus.FAULT in statuses_set:
                        failed_file = session.query(FtpFile).get(file_id)
                        failed_file.status = FtpFileStatus.FAILED
                        failed_file.err_desc = f'{statuses.count(FtpFileStatus.FAILED)} files have failed status'
                        log.info(f'load_file({failed_file.id}): {failed_file.status}')

            if futures:
                wait_for(context, futures)

            with Sessional.domain.session_scope() as session:
                query_ = session.query(FtpFile).filter(FtpFile.status == FtpFileStatus.READY)
                if context.parse_filters:
                    query_ = query_.filter(text(context.parse_filters))

                if query_.count() == 0:
                    if context.attemp_count > 1:
                        context = context._replace(attemp_count=1)
                    break
    except Exception as ex:
        log.exception(ex)

    return context 

def finalize(context):
    context.executor.shutdown(True)
    log.info(f'finalize')

def ftp_loading(host, port, user, password, load_file_id, filename, location, create_date):
    try:
        files = []
        with FTP() as ftp_client:

            try:
                ftp_client.connect(host, port)
                ftp_client.login(user, password)            
                ftp_client.cwd(location) 
            except Exception as ex:
                raise Error(ex.args[0], ex, ERROR_FTP_LABEL)

            for name, crc, size, last_modify, message in download_extract_zip(ftp_client, filename):
                files.append(ContentData(name, crc, size, last_modify, message))

        return (load_file_id, filename, location, create_date, files)
    except Exception as ex:
        log.exception(ex)
        label = ERROR_FTP_LABEL if isinstance(err, Error) and err.params == ERROR_FTP_LABEL else ERROR_UNKNOWN_LABEL
        raise Error(ex.args[0], ex, (load_file_id, filename, location, label))

def download_extract_zip(ftp_client, zipfilename, ext_file='.xml'):
    """
    Download a ZIP file from FTP and extract its contents in memory
    """
    with io.BytesIO() as buffer:

        try:
            ftp_client.retrbinary('RETR '+zipfilename, buffer.write)
        except Exception as ex:
            raise Error(ex.args[0], ex, ERROR_FTP_LABEL)
            
        with zipfile.ZipFile(buffer) as thezip:
            for zipinfo in thezip.infolist():
                
                if not zipinfo.filename.endswith(ext_file):
                    continue

                shm = shared_memory.SharedMemory(create=True, size=zipinfo.file_size)
                message = shm.name              
                with thezip.open(zipinfo) as thefile:
                    shm.buf[:zipinfo.file_size] = thefile.read()
                shm.close()
                #TODO: take out in a function
                yy, mt, dd, hh, mi, ss = zipinfo.date_time                
                if ss > 59:
                    ss = 0
                    mi += 1
                if mi > 59:
                    mi = 0
                    hh += 1
                if hh > 23:
                    hh = 23
                    mi = 59
                    ss = 59
                yield zipinfo.filename, zipinfo.CRC, zipinfo.file_size, datetime.datetime(yy, mt, dd, hh, mi, ss), message

def wait_for(context:Context, futures):
    ready_to_parse = list()

    for future in concurrent.futures.as_completed(futures):
        err = future.exception()
        if err is None:
            load_file_id, filename, location, create_date, files = future.result()                
            with Sessional.domain.session_scope() as session:
                reassigned = 0
                if files:               
                    for file_data in files:
                        exists_content = session.query(FtpContent).\
                            filter(FtpContent.file_id == load_file_id).\
                                filter(FtpContent.name == file_data.name).\
                                    one_or_none()
                        if exists_content is None:
                            content = FtpContent(file_id=load_file_id, status=FtpContentStatus.PREPARED, name=file_data.name, crc=file_data.crc, size=file_data.size, last_modify=file_data.last_modify, message=file_data.message)
                            session.add(content)
                            session.flush()
                            ready_to_parse.append(ParseContent(content.id, create_date, filename, content.last_modify, content.name))
                        elif (exists_content.status == FtpContentStatus.FAULT) or ((exists_content.status in [FtpContentStatus.PROCESSED, FtpContentStatus.PREPARED]) and (exists_content.crc != file_data.crc) and (exists_content.last_modify <= file_data.last_modify)):
                            exists_content.crc = file_data.crc
                            exists_content.size = file_data.size
                            exists_content.last_modify = file_data.last_modify
                            exists_content.message = file_data.message
                            exists_content.status = FtpContentStatus.PREPARED
                            reassigned += 1
                            ready_to_parse.append(ParseContent(exists_content.id, create_date, filename, exists_content.last_modify, exists_content.name))
                        else:
                            shm = shared_memory.SharedMemory(file_data.message)
                            shm.close()
                            shm.unlink()
                else:
                    load_file = session.query(FtpFile).get(load_file_id)
                    if load_file:
                        load_file.status = FtpFileStatus.DONE
                        load_file.err_desc = 'Empty'


                if session.new or reassigned:
                    log.debug(f'{filename} (id={load_file_id}): added {len(session.new)}, reassigned {reassigned} files')
        elif isinstance(err, Error):
            load_file_id, filename, location, label = err.params
            with Sessional.domain.session_scope() as session:
                load_file = session.query(FtpFile).get(load_file_id)
                if load_file:
                    if label == ERROR_UNKNOWN_LABEL or context.attemp_count >= context.error_attempts:
                        load_file.status = FtpFileStatus.FAILED
                        load_file.err_desc = err.message
                        log.error(f'{filename} (id={load_file_id}) error')
                    else:
                        load_file.status = FtpFileStatus.READY
                        context = context._replace(attemp_count=context.attemp_count+1)
        else:
            raise err

    sorted_ready_to_parse_by_name = sorted(ready_to_parse, key=lambda content: content.name)
    sorted_ready_to_parse_by_date = sorted(sorted_ready_to_parse_by_name, key=lambda content: content.date)
    sorted_ready_to_parse_by_archive_name = sorted(ready_to_parse, key=lambda content: content.archive_name)
    sorted_ready_to_parse = sorted(sorted_ready_to_parse_by_archive_name, key=lambda content: content.archive_date)

    for content in sorted_ready_to_parse:

        for parse_filter, queue_name in context.queue_by_filter.items():
            if content.archive_name.rfind(parse_filter) != -1:
                try:
                    context.parse_queues[queue_name].put(content.id, block=True, timeout=context.block_timeout)
                except queue.Full:
                    log.warning(f'The queue is moving slowly enough. {context.block_timeout} seconds is not enough. Another attempt to wait and an exception will be thrown.')
                    context.parse_queues[queue_name].put(content.id, block=True, timeout=context.block_timeout)                    
                
                # log.debug(f'q.put: {content.id}')
                break