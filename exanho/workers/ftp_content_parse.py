import concurrent.futures
import io
import logging
import datetime
import time
import zipfile

from collections import namedtuple
from multiprocessing import shared_memory
from threading import Thread
from queue import Queue

import exanho.eis44.config as config
import exanho.orm.sqlalchemy as domain

from exanho.core.common import Error
from exanho.model.loading import ContentStatus, FtpContent

log = logging.getLogger(__name__)

executor = concurrent.futures.ThreadPoolExecutor(config.load_archive_max_workers)

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
    while True:
        futures = set()

        with domain.session_scope() as session:
            for file_to_parse in session.query(FtpContent).filter(FtpContent.status == ContentStatus.PREPARED).order_by(FtpContent.last_modify).limit(config.parse_file_max_workers):
                file_to_parse.status = ContentStatus.PARSING
                future = executor.submit(send_to_parse, file_to_parse.id, file_to_parse.name, file_to_parse.size, file_to_parse.message)
                futures.add(future) 
                log.debug(f'load_content({file_to_parse.id}): {file_to_parse.status}')
        if futures:
            wait_for(futures)

        with domain.session_scope() as session:
            if session.query(FtpContent).filter(FtpContent.status == ContentStatus.PREPARED).count() == 0:
                break   

def finalize():
    executor.shutdown(True)
    log.info(f'finalize')

def send_to_parse(id, filename, size, message):
    try:
        shm = shared_memory.SharedMemory(message)
        buffer = shm.buf[:size]
        doc = buffer.tobytes().decode(encoding="utf-8", errors="strict")
        log.debug(f'{doc[:50]}...')
        buffer.release()
        shm.close()
        shm.unlink()
        return id, filename
    except Exception as ex:
        log.exception(ex)
        raise Error(ex.args[0], ex, (id, filename, size, message))
    


def wait_for(futures):
    for future in concurrent.futures.as_completed(futures):
        err = future.exception()
        if err is None:
            id, filename = future.result()                
            with domain.session_scope() as session:
                load_content = session.query(FtpContent).get(id)
                if load_content:
                    load_content.status = ContentStatus.PROCESSED
                    load_content.message = None
                    log.debug(f'load_content({load_content.id}): {load_content.status}')
        elif isinstance(err, Error):
            id, filename, *_ = err.params
            with domain.session_scope() as session:
                load_content = session.query(FtpContent).get(id)
                if load_content:
                    load_content.status = ContentStatus.FAULT
                    load_content.message = err.message
                    log.error(f'{filename} (id={id}) error')
        else:
            raise err