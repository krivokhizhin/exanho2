import io
import logging
import datetime
import time
import zipfile

from collections import namedtuple, defaultdict
from ftplib import FTP
from threading import Thread
from queue import Queue

import exanho.eis44.config as config
import exanho.orm.sqlalchemy as domain

from exanho.model.loading import TaskStatus, LoadTask, ArchiveStatus, LoadArchive
from exanho.eis44.ftp_consider import FtpConsider
from exanho.eis44.ftp_objects import FtpFile

log = logging.getLogger(__name__)

def initialize(*args, **kwargs):
    db_url = kwargs.get('db_url', None)
    if db_url:
        db_validate = kwargs.get('db_validate', False)
        if db_validate:
            is_valid, errors, warnings = domain.validate(db_url)
            if not is_valid:
                log.error(errors)
                if warnings:
                    log.warning(warnings)
                raise RuntimeError(f'The database schema does not match the ORM model')
            
        domain.configure(db_url)

    log.info(f'initialize')

def work():
    now = datetime.datetime.now()

    with domain.session_scope() as session:

        load_task = session.query(LoadTask).filter(LoadTask.scheduled_date < now).filter(LoadTask.status == TaskStatus.SCHEDULED).first()

        if load_task:
            load_task.status = TaskStatus.SCANNING
            session.flush()
            log.info(f'load_task({load_task.id}): {load_task.status}')

            archives = []
            try:
                viewer = FtpConsider(host=config.ftp_host, port=config.ftp_port, user=config.ftp_user, password=config.ftp_password, location=load_task.location)
                viewer.consider()
                archives = [ftp_object for ftp_object in viewer.ftp_objects if isinstance(ftp_object, FtpFile)]
            except Exception as ex:
                load_task.status = TaskStatus.ERROR
                load_task.err_desc = f'{ex.__class__.__name__}: {ex.args[0]}'
                log.exception(ex)

            reassigned = 0
            for archive in archives:
                exists_archive = session.query(LoadArchive).\
                    filter(LoadArchive.task == load_task).\
                        filter(LoadArchive.name == archive.name).\
                            one_or_none()

                if exists_archive is None:
                    session.add(LoadArchive(task_id=load_task.id, name=archive.name, status=ArchiveStatus.READY, date=archive.date, size=archive.size))
                elif exists_archive.date < archive.date: # and (exists_archive.status != ArchiveStatus.LOADING):
                    exists_archive.date = archive.date
                    exists_archive.size = archive.size
                    exists_archive.err_desc = None
                    exists_archive.status = ArchiveStatus.READY
                    reassigned += 1
                
            if session.new or reassigned:
                load_task.status = TaskStatus.RUNNING
                log.info(f'Archives: added {len(session.new)}, reassigned {reassigned}')
            elif load_task.status == TaskStatus.SCANNING:
                load_task.status = TaskStatus.DONE

            session.flush()
            log.info(f'load_task({load_task.id}): {load_task.status}')

        archive_statuses = session.query(LoadArchive.task_id, LoadArchive.status).\
            filter(LoadArchive.task_id.in_(session.query(LoadTask.id).filter(LoadTask.status == TaskStatus.RUNNING))).all()
        statuses_by_task = defaultdict(list)
        for task_id, archive_status in archive_statuses:
            statuses_by_task[task_id].append(archive_status)

        for task_id, statuses in statuses_by_task.items():
            statuses_set = set(statuses)
            if (len(statuses_set) == 1) and (ArchiveStatus.PERFORMED in statuses_set):
                complete_task = session.query(LoadTask).get(task_id)
                complete_task.status = TaskStatus.DONE
                complete_task.err_desc = None
                log.info(f'load_task({complete_task.id}): {complete_task.status}')
            elif ArchiveStatus.FAILED in statuses_set:
                complete_task = session.query(LoadTask).get(task_id)
                complete_task.status = TaskStatus.ERROR
                complete_task.err_desc = f'{statuses.count(ArchiveStatus.FAILED)} archives have failed status'
                log.info(f'load_task({complete_task.id}): {complete_task.status}')

            

def finalize():
    log.info(f'finalize')