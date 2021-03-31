import datetime
import logging
import time
from collections import defaultdict, namedtuple
from queue import Queue
from threading import Thread
from sqlalchemy.orm.session import Session as OrmSession

from exanho.orm.domain import Sessional
from exanho.core.manager_context import Context as ExanhoContext
from exanho.ftp_loading.ftp_consider import FtpConsider
from exanho.ftp_loading.model import FtpFileStatus, FtpFile, FtpTask, FtpTaskStatus

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'ftp_host', 
    'ftp_port', 
    'ftp_user', 
    'ftp_password',
    'ready_minutes',
    'schedule_minutes',
    'insp_file_queue',
    'w_thread',
    'error_attempts',
    'attemp_count'
    ], defaults=[10, 30, None, None, 60, 1])
    
InspFile = namedtuple('InspFile', ['task_id', 'name', 'directory', 'date', 'size'])

files_failed_desc = 'files have failed status'

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)
    
    insp_file_queue=Queue()
    w_thread = Thread(target=write_ftp_files, args=(insp_file_queue, ))
    w_thread.daemon = True
    w_thread.start()

    context = context._replace(insp_file_queue=insp_file_queue, w_thread=w_thread)

    log.info(f'initialize')
    return context

def work(context:Context):
    # log.debug('task_run in work')

    try:        
        with Sessional.domain.session_scope() as session:
            assert isinstance(session, OrmSession)
            now = datetime.datetime.today()
            load_task = session.query(FtpTask).filter(FtpTask.scheduled_date < now).filter(FtpTask.status == FtpTaskStatus.SCHEDULED).first()

            if load_task:
                load_task.status = FtpTaskStatus.SCANNING
                session.flush()
                log.info(f'FtpTask({load_task.id}): {load_task.status}')

                try:
                    viewer = FtpConsider(
                        task_id=load_task.id,
                        insp_q=context.insp_file_queue,
                        host=context.ftp_host,
                        port=context.ftp_port,
                        user=context.ftp_user,
                        password=context.ftp_password,
                        location=load_task.location,
                        min_date=load_task.min_date,
                        max_date=load_task.max_date,
                        excluded_folders=load_task.excluded_folders,
                        delimiter=load_task.delimiter)
                    viewer.prepare()
                    viewer.inspect()
                    load_task.status = FtpTaskStatus.RUNNING                
                except Exception as ex:                
                    load_task.err_desc = f'{ex.__class__.__name__}: {ex.args[0]}'
                    log.exception(ex)
                    if context.attemp_count >= context.error_attempts:
                        load_task.status = FtpTaskStatus.ERROR
                    else:
                        load_task.status = FtpTaskStatus.SCHEDULED
                        context = context._replace(attemp_count=context.attemp_count+1)
                finally:
                    session.flush()
                    log.info(f'FtpTask({load_task.id}): {load_task.status}')
                

            ready_dt = datetime.datetime.today() - datetime.timedelta(minutes=context.ready_minutes)
            insp_file_statuses = session.query(FtpTask.id, FtpFile.status).\
                select_from(FtpTask).outerjoin(FtpFile).filter(FtpTask.status == FtpTaskStatus.RUNNING).\
                    filter(FtpTask.scheduled_date < ready_dt).all()
            statuses_by_task = defaultdict(list)
            for task_id, insp_file_status in insp_file_statuses:
                if load_task and task_id == load_task.id:
                    continue
                statuses_by_task[task_id].append(insp_file_status)

            for task_id, statuses in statuses_by_task.items():
                statuses_set = set(statuses)
                if (len(statuses_set) == 1) and (not {FtpFileStatus.DONE, None}.isdisjoint(statuses_set)):
                    task_done = session.query(FtpTask).get(task_id)
                    task_done.err_desc = None
                    task_done.last_date = task_done.scheduled_date
                    if task_done.schedule == '*':
                        task_done.scheduled_date = datetime.datetime.today() + datetime.timedelta(minutes=context.schedule_minutes)
                        task_done.status = FtpTaskStatus.SCHEDULED
                    else:
                        task_done.status = FtpTaskStatus.PERFORMED
                    log.info(f'FtpTask({task_done.id}): {task_done.status}')
                elif (FtpFileStatus.FAILED in statuses_set) and ({FtpFileStatus.READY, FtpFileStatus.LOADING}.isdisjoint(statuses_set)):
                    task_done = session.query(FtpTask).get(task_id)
                    if task_done.err_desc is None:
                        task_done.status = FtpTaskStatus.SCHEDULED
                        task_done.err_desc = f'{statuses.count(FtpFileStatus.FAILED)} {files_failed_desc}'
                        log.warning(f'load_task({task_done.id}): {task_done.err_desc}')                    
                    elif task_done.err_desc.endswith(files_failed_desc):
                        last_err_count = int(task_done.err_desc.split(files_failed_desc)[0])
                        err_count = statuses.count(FtpFileStatus.FAILED)
                        if err_count < last_err_count:
                            task_done.status = FtpTaskStatus.SCHEDULED
                            task_done.err_desc = f'{err_count} {files_failed_desc}'
                            log.warning(f'load_task({task_done.id}): {task_done.err_desc}')
                        else:
                            task_done.status = FtpTaskStatus.ERROR
                            task_done.err_desc = f'{err_count} {files_failed_desc}'
                    else:
                        task_done.status = FtpTaskStatus.ERROR
                        task_done.err_desc = f'{statuses.count(FtpFileStatus.FAILED)} {files_failed_desc}'
                    log.info(f'load_task({task_done.id}): {task_done.status}')
    except Exception as ex:
        log.exception(ex)

    return context

def finalize(context):
    context.insp_file_queue.put(None)
    context.w_thread.join()
    log.info(f'finalize')

def write_ftp_files(insp_file_queue):
    while True:
        try:
            insp_file = insp_file_queue.get()
            if insp_file is None:
                break

            insp_file = InspFile(*insp_file)
            with Sessional.domain.session_scope() as session:

                exists_file = session.query(FtpFile).\
                    filter(FtpFile.task_id == insp_file.task_id).\
                        filter(FtpFile.filename == insp_file.name).\
                            one_or_none()

                if exists_file is None:
                    session.add(FtpFile(task_id=insp_file.task_id, filename=insp_file.name, directory=insp_file.directory, status=FtpFileStatus.READY, date=insp_file.date, size=insp_file.size))
                elif exists_file.date < insp_file.date or (exists_file.status == FtpFileStatus.FAILED):
                    exists_file.date = insp_file.date
                    exists_file.size = insp_file.size
                    exists_file.err_desc = None
                    exists_file.status = FtpFileStatus.READY
            
        except Exception as ex:
            log.exception(ex)
