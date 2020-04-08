import logging
import datetime

import exanho.orm.sqlalchemy as domain

from exanho.model.loading import LoadStatus, LoadTask, LoadArchive, LoadFile

log = logging.getLogger(__name__)

class Context:
    pass

context = Context()

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

        context.session = domain.Session()

    log.info(f'initialize')

def work():    
    now = datetime.datetime.now()
    for load_task in context.session.query(LoadTask).\
        filter(LoadTask.scheduled_date < now).\
        filter(LoadTask.status == LoadStatus.NEW.value):
        log.debug(load_task)
    log.info(f'work')

def finalize():
    log.info(f'finalize')