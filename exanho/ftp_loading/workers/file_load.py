import concurrent.futures
import datetime
import io
import logging
import zipfile
from collections import defaultdict, namedtuple
from ftplib import FTP
from multiprocessing import shared_memory

import exanho.orm.sqlalchemy as domain
from exanho.core.common import Error, get_used_memory_level
from exanho.ftp_loading.model.loading import (ContentStatus, FileStatus,
                                              FtpContent, FtpFile)

log = logging.getLogger(__name__)

ERROR_FTP_LABEL = object()
ERROR_UNKNOWN_LABEL = object()

Context = namedtuple('Context', [
    'db_url', 
    'db_validate', 
    'ftp_host', 
    'ftp_port', 
    'ftp_user', 
    'ftp_password',
    'max_mem_level',
    'with_swap',
    'max_pool_workers',
    'executor',
    'error_attempts',
    'attemp_count'
    ], defaults=[0.8, False, 20, None, 60, 1])

ContentData = namedtuple('ContentData', ['name', 'crc', 'size', 'last_modify', 'message'])

def initialize(appsettings):
    context = Context(**appsettings)

    if context.db_validate:
        is_valid, errors, warnings = domain.validate(context.db_url)
        if not is_valid:
            log.error(errors)
            if warnings:
                log.warning(warnings)
            raise RuntimeError(f'The database schema does not match the ORM model')
            
    domain.configure(context.db_url)

    if context.max_mem_level > 1:
        max_mem_level = context.max_mem_level / 100.0
        if max_mem_level > 1:
            raise Error('Invalid "max_mem_level" value: must be 0..1 or 0..100')
        context = context._replace(max_mem_level=max_mem_level)

    executor = concurrent.futures.ThreadPoolExecutor(context.max_pool_workers)
    context = context._replace(executor=executor)

    log.info(f'initialize')
    return context

def work(context):
    log.debug('file_load in work')

    try:
        while True:
            used_mem_level = get_used_memory_level(context.with_swap)
            if used_mem_level > context.max_mem_level:
                log.warning(f'Allowed memory usage level ({context.max_mem_level:.1%}) exceeded: {used_mem_level:.1%}')
                break


            futures = set()
            with domain.session_scope() as session:
                load_file_ids = []
                for load_file in session.query(FtpFile).filter(FtpFile.status == FileStatus.READY).order_by(FtpFile.date, FtpFile.filename).limit(context.max_pool_workers):
                    load_file.status = FileStatus.LOADING
                    future = context.executor.submit(ftp_loading, context.ftp_host, context.ftp_port, context.ftp_user, context.ftp_password, load_file.id, load_file.filename, load_file.directory)
                    futures.add(future)
                    log.info(f'load_file({load_file.id}): {load_file.status}')
                    load_file_ids.append(load_file.id)

                session.flush()

                file_statuses = session.query(FtpFile.id, FtpContent.status).\
                    select_from(FtpFile).join(FtpContent).filter(FtpFile.status == FileStatus.LOADING).all()
                statuses_by_archive = defaultdict(list)
                for file_id, file_status in file_statuses:
                    if file_id in load_file_ids:
                        continue
                    statuses_by_archive[file_id].append(file_status)

                for file_id, statuses in statuses_by_archive.items():
                    statuses_set = set(statuses)
                    if (len(statuses_set) == 1) and (ContentStatus.PROCESSED in statuses_set):
                        done_file = session.query(FtpFile).get(file_id)
                        done_file.status = FileStatus.DONE
                        done_file.err_desc = None
                        log.info(f'load_file({done_file.id}): {done_file.status}')
                    elif ContentStatus.FAULT in statuses_set:
                        failed_file = session.query(FtpFile).get(file_id)
                        failed_file.status = FileStatus.FAILED
                        failed_file.err_desc = f'{statuses.count(FileStatus.FAILED)} files have failed status'
                        log.info(f'load_file({failed_file.id}): {failed_file.status}')

            if futures:
                wait_for(context, futures)

            with domain.session_scope() as session:
                if session.query(FtpFile).filter(FtpFile.status == FileStatus.READY).count() == 0:
                    break
    except Exception as ex:
        log.exception(ex)

    return context 

def finalize(context):
    context.executor.shutdown(True)
    log.info(f'finalize')

def ftp_loading(host, port, user, password, load_file_id, filename, location):
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

        return (load_file_id, filename, location, files)
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
    for future in concurrent.futures.as_completed(futures):
        err = future.exception()
        if err is None:
            load_file_id, filename, location, files = future.result()                
            with domain.session_scope() as session:
                reassigned = 0
                if files:               
                    for file_data in files:
                        exists_content = session.query(FtpContent).\
                            filter(FtpContent.file_id == load_file_id).\
                                filter(FtpContent.name == file_data.name).\
                                    one_or_none()
                        if exists_content is None:
                            session.add(FtpContent(file_id=load_file_id, status=ContentStatus.PREPARED, name=file_data.name, crc=file_data.crc, size=file_data.size, last_modify=file_data.last_modify, message=file_data.message))
                        elif (exists_content.status == ContentStatus.FAULT) or ((exists_content.status in [ContentStatus.PROCESSED, ContentStatus.PREPARED]) and (exists_content.crc != file_data.crc) and (exists_content.last_modify <= file_data.last_modify)):
                            exists_content.crc = file_data.crc
                            exists_content.size = file_data.size
                            exists_content.last_modify = file_data.last_modify
                            exists_content.message = file_data.message
                            exists_content.status = ContentStatus.PREPARED
                            reassigned += 1
                        else:
                            shm = shared_memory.SharedMemory(file_data.message)
                            shm.close()
                            shm.unlink()
                else:
                    load_file = session.query(FtpFile).get(load_file_id)
                    if load_file:
                        load_file.status = FileStatus.DONE
                        load_file.err_desc = 'Empty'


                if session.new or reassigned:
                    log.info(f'{filename} (id={load_file_id}): added {len(session.new)}, reassigned {reassigned} files')
        elif isinstance(err, Error):
            load_file_id, filename, location, label = err.params
            with domain.session_scope() as session:
                load_file = session.query(FtpFile).get(load_file_id)
                if load_file:
                    if label == ERROR_UNKNOWN_LABEL or context.attemp_count >= context.error_attempts:
                        load_file.status = FileStatus.FAILED
                        load_file.err_desc = err.message
                        log.error(f'{filename} (id={load_file_id}) error')
                    else:
                        load_file.status = FileStatus.READY
                        context = context._replace(attemp_count=context.attemp_count+1)
        else:
            raise err
