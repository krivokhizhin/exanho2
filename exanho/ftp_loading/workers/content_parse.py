import logging
import time
from collections import namedtuple
from multiprocessing import shared_memory

from exanho.orm.domain import Sessional
from exanho.core.manager_context import Context as ExanhoContext
from exanho.core.common import Error
from exanho.ftp_loading.model import FtpContentStatus, FtpContent

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context:ExanhoContext):
    context = appsettings
    log.info(f'initialize')
    return context

def work(context, message):
    log.debug('content_parse in work')

    content_id = int(message)
    memory_name = None
    memory_size = None

    content_date = None
    content_name = None

    try:
        with Sessional.domain.session_scope() as session:
            content = session.query(FtpContent).filter(FtpContent.id == content_id).one()

            memory_name = content.message
            memory_size = content.size
            content_date = content.last_modify
            content_name = content.name
            content.status = FtpContentStatus.PARSING
        
        parsed = None
        error = None
        shm = buffer = None
        
        try:
            shm = shared_memory.SharedMemory(memory_name)
            buffer = shm.buf[:memory_size]
            data = buffer.tobytes().decode(encoding="utf-8", errors="strict")

            # time.sleep(10)
            # log.debug(f'load_content({content_id}): {content_date} | {content_name} | data={data[:50]}')

            parsed = True

        except Exception as ex:
            log.exception(ex)
            parsed = False
            error = ex.args[0][:100]
        finally:
            if buffer:
                buffer.release()
            if shm:
                shm.close()
                shm.unlink()


        with Sessional.domain.session_scope() as session:
            content = session.query(FtpContent).filter(FtpContent.id == content_id).one()

            if parsed:
                content.status = FtpContentStatus.PROCESSED
                content.message = None
                log.info(f'load_content({content.id}): {content.status}')
            else:
                content.status = FtpContentStatus.FAULT
                content.message = error
                log.error(f'load_content({content.id}): {content.status}')

    except Exception as ex:
        log.exception(ex)

    return context 

def finalize(context):
    log.info(f'finalize')