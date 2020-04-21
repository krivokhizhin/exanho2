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

import exanho.orm.sqlalchemy as domain

from exanho.core.common import create_client_class
from exanho.core.common import Error
from exanho.model.loading import ContentStatus, FtpContent
from exanho.interfaces import IParse

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'db_url', 
    'db_validate',
    'rpc_port',
    'rpc_secretkey',
    'max_pool_workers',
    'executor',
    'like_expression'
    ], defaults = [None, 4, None, None])

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

    secretkey = context.rpc_secretkey.encode('utf-8') if context.rpc_secretkey else None
    
    global RpcClient
    RpcClient = create_client_class(IParse, 'localhost', context.rpc_port, secretkey)

    executor = concurrent.futures.ThreadPoolExecutor(context.max_pool_workers)

    context = context._replace(rpc_secretkey=secretkey, executor=executor)

    log.info(f'initialize')
    return context

def work(context):
    while True:
        futures = set()

        with domain.session_scope() as session:
            q = session.query(FtpContent).filter(FtpContent.status == ContentStatus.PREPARED)
            if context.like_expression:
                q = q.filter(FtpContent.name.like(context.like_expression))
            for file_to_parse in q.order_by(FtpContent.last_modify).limit(context.max_pool_workers):
                file_to_parse.status = ContentStatus.PARSING
                future = context.executor.submit(send_to_parse, file_to_parse.id, file_to_parse.name, file_to_parse.size, file_to_parse.message)
                futures.add(future) 
                log.info(f'load_content({file_to_parse.id}): {file_to_parse.status}')
        if futures:
            wait_for(futures)

        with domain.session_scope() as session:
            if session.query(FtpContent).filter(FtpContent.status == ContentStatus.PREPARED).count() == 0:
                break
    return context 

def finalize(context):
    context.executor.shutdown(True)
    log.info(f'finalize')

def send_to_parse(id, filename, size, message):
    try:
        shm = shared_memory.SharedMemory(message)

        client = RpcClient()
        new_counter, update_counter = client.parse(filename, size, message)
        log.info(f'Objects: added {new_counter}, updated {update_counter}')

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
                    log.info(f'load_content({load_content.id}): {load_content.status}')
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