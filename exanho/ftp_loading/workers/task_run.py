import datetime
import logging
import time
from collections import defaultdict, namedtuple
from queue import Queue
from threading import Thread

import exanho.orm.sqlalchemy as domain
from exanho.ftp_loading.ftp_consider import FtpConsider
from exanho.ftp_loading.model.loading import FileStatus, FtpFile, FtpTask, TaskStatus

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'db_url', 
    'db_validate', 
    'ftp_host', 
    'ftp_port', 
    'ftp_user', 
    'ftp_password',
    'insp_file_queue',
    'w_thread'
    ], defaults=[None, None])
    
InspFile = namedtuple('InspFile', ['task_id', 'name', 'directory', 'date', 'size'])

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
    
    insp_file_queue=Queue()
    w_thread = Thread(target=write_ftp_files, args=(insp_file_queue, ))
    w_thread.daemon = True
    w_thread.start()

    context = context._replace(insp_file_queue=insp_file_queue, w_thread=w_thread)

    log.info(f'initialize')
    return context

def work(context):

    with domain.session_scope() as session:
        now = datetime.datetime.now()
        load_task = session.query(FtpTask).filter(FtpTask.scheduled_date < now).filter(FtpTask.status == TaskStatus.SCHEDULED).first()

        if load_task:
            load_task.status = TaskStatus.SCANNING
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
            except Exception as ex:
                load_task.status = TaskStatus.ERROR
                load_task.err_desc = f'{ex.__class__.__name__}: {ex.args[0]}'
                log.exception(ex)
                
            load_task.status = TaskStatus.RUNNING
            session.flush()
            log.info(f'FtpTask({load_task.id}): {load_task.status}')

        insp_file_statuses = session.query(FtpTask.id, FtpFile.status).\
            select_from(FtpTask).outerjoin(FtpFile).filter(FtpTask.status == TaskStatus.RUNNING).all()
        statuses_by_task = defaultdict(list)
        for task_id, insp_file_status in insp_file_statuses:
            if load_task and task_id == load_task.id:
                continue
            statuses_by_task[task_id].append(insp_file_status)

        for task_id, statuses in statuses_by_task.items():
            statuses_set = set(statuses)
            if (len(statuses_set) == 1) and (not {FileStatus.DONE, None}.isdisjoint(statuses_set)):
                task_done = session.query(FtpTask).get(task_id)
                task_done.status = TaskStatus.PERFORMED
                task_done.err_desc = None
                log.info(f'FtpTask({task_done.id}): {task_done.status}')
            elif FileStatus.FAILED in statuses_set:
                task_done = session.query(FtpTask).get(task_id)
                task_done.status = TaskStatus.ERROR
                task_done.err_desc = f'{statuses.count(FileStatus.FAILED)} files have failed status'
                log.info(f'load_task({task_done.id}): {task_done.status}')

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
            with domain.session_scope() as session:

                exists_file = session.query(FtpFile).\
                    filter(FtpFile.task_id == insp_file.task_id).\
                        filter(FtpFile.filename == insp_file.name).\
                            one_or_none()

                if exists_file is None:
                    session.add(FtpFile(task_id=insp_file.task_id, filename=insp_file.name, directory=insp_file.directory, status=FileStatus.READY, date=insp_file.date, size=insp_file.size))
                elif exists_file.date < insp_file.date or (exists_file.status == FileStatus.FAILED):
                    exists_file.date = insp_file.date
                    exists_file.size = insp_file.size
                    exists_file.err_desc = None
                    exists_file.status = FileStatus.READY
            
        except Exception as ex:
            log.exception(ex)
