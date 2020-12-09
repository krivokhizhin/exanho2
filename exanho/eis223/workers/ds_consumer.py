import importlib
import logging
import time
import xml.etree.ElementTree as ET
from collections import namedtuple
from multiprocessing import JoinableQueue
from multiprocessing import shared_memory

from exanho.orm.domain import Sessional
from exanho.core.common import Error, Timer
from exanho.core.manager_context import Context as ExanhoContext
from exanho.ftp_loading.model import FtpContentStatus, FtpContent

from ..ds.match_builder import match_builder
from ..parsing import parsers

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'error_attempts',
    'update'
    ], defaults = [2, False])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)
    log.info(f'Initialized')
    return context

def work(context:Context, message):
    attempt_count = context.error_attempts
    update = context.update
    content_id = int(message)
    domain = Sessional.domain

    try:
        with domain.session_scope() as session:
            content_to_parse = session.query(FtpContent).get(content_id)
            if content_to_parse is None:
                return context

            obj_builder = match_builder(content_to_parse.name)

            content_to_parse.status = FtpContentStatus.PARSING
            session.flush()

            shm = buffer = None
            try:
                shm = shared_memory.SharedMemory(content_to_parse.message)
                buffer = shm.buf[:content_to_parse.size]
                root_obj = obj_builder(buffer.tobytes(),silence = True, print_warnings=False)

                xml_root_tag = root_obj.get_xml_tag()
                parser = parsers.get(xml_root_tag, None)
                if parser is None:
                    raise Error(f'No parser found for "{xml_root_tag}" document')

                remain_attempt = attempt_count
                while remain_attempt > 0:

                    try:
                        parser(session, root_obj, update, **{'content_id' : content_to_parse.id})                    
                        content_to_parse.status = FtpContentStatus.PROCESSED
                        content_to_parse.message = None
                        session.flush()
                        remain_attempt = 0
                    except Exception as ex:
                        remain_attempt -= 1
                        log.warning(f'load_content({content_id}): remain_attempt={remain_attempt}, error={ex.args}')
                        if remain_attempt < 1:
                            raise
                        time.sleep(1)                                    
            
            except Exception as ex:
                content_to_parse.status = FtpContentStatus.FAULT
                content_to_parse.message = ex.message if isinstance(ex, Error) else str(ex.args)[:100]
                log.exception(ex)
                
            finally:
                if buffer:
                    buffer.release()
                if shm:
                    shm.close()
                    shm.unlink()

            log.debug(f'load_content({content_id}): {content_to_parse.status}')        
    except Exception as ex:        
        with domain.session_scope() as session:
            content_to_parse = session.query(FtpContent).get(content_id)
            if content_to_parse is None:
                return context
                
            content_to_parse.status = FtpContentStatus.FAULT
            content_to_parse.message = ex.message if isinstance(ex, Error) else str(ex.args)[:100]
            log.exception(ex)

    

    return context 

def finalize(context):
    log.info(f'Finalized for {context.parse_module.__name__}')