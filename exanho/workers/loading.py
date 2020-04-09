import logging
import datetime
import time

from collections import namedtuple

import exanho.eis44.config as ftp_config
import exanho.orm.sqlalchemy as domain

from exanho.model.loading import LoadStatus, LoadTask, LoadArchive, LoadFile
from exanho.eis44.ftp_extractor import FtpExtractor

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
    TaskExec = namedtuple('TaskExec', ['id', 'location'])
    tasks = []
    with domain.session_scope() as session:
        for load_task in session.query(LoadTask).\
            filter(LoadTask.scheduled_date < now).\
            filter(LoadTask.status == LoadStatus.NEW.value):

            log.debug(load_task)
            tasks.append(TaskExec(load_task.id, load_task.location))
            load_task.status = LoadStatus.EXECUTION.value

    log.debug(tasks)

    for task in tasks:
        extractor = FtpExtractor(host=ftp_config.ftp_host, port=ftp_config.ftp_port, user=ftp_config.ftp_user, password=ftp_config.ftp_password, location=task.location)
        extractor.extract()
        time.sleep(10)
        log.debug(extractor.ftp_objects)

    with domain.session_scope() as session:
        for task in tasks:
            load_task = session.query(LoadTask).filter_by(id=task.id).one()
            load_task.status = LoadStatus.COMPLETE.value

    log.info(f'work')

def finalize():
    log.info(f'finalize')