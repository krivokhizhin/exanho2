import importlib
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession
from multiprocessing import shared_memory

from exanho.orm.domain import Sessional
from exanho.core.common import Error
from exanho.core.manager_context import Context as ExanhoContext
from exanho.ftp_loading.model import FtpContentStatus, FtpContent, FtpErrorContent

from ..parsing import parsers

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'parse_module',
    'update'
    ], defaults = [False])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    mod = importlib.import_module(context.parse_module.strip())
    context = context._replace(parse_module=mod)
    
    log.info(f'Initialized for {context.parse_module}')
    return context

def work(context:Context, message):
    update = context.update
    content_id = int(message)
    domain = Sessional.domain

    with domain.session_scope() as session:
        assert isinstance(session, OrmSession)
        content_to_parse = session.query(FtpContent).get(content_id)
        if content_to_parse is None:
            return context

        content_to_parse.status = FtpContentStatus.PARSING
        session.flush()

        shm = buffer = None
        try:
            shm = shared_memory.SharedMemory(content_to_parse.message)
            buffer = shm.buf[:content_to_parse.size]
            export_obj = None

            try:

                export_obj = context.parse_module.parseString(buffer.tobytes(), silence = True, print_warnings=False)

            except Exception as ex:
                
                if content_to_parse.error_content and content_to_parse.error_content.origin_data != buffer.tobytes():
                    content_to_parse.error_content = None
                    session.flush()
                
                if content_to_parse.error_content is None:
                    content_to_parse.error_content = FtpErrorContent(
                        origin_data = buffer.tobytes()
                    )

                if content_to_parse.error_content.correct_data:
                    try:
                        export_obj = context.parse_module.parseString(content_to_parse.error_content.correct_data, silence = True, print_warnings=False)
                    except Exception as inner_ex:
                        log.exception(inner_ex)
                        raise Error(str(inner_ex.args)[:100], inner_ex)
                
                if export_obj is None:
                    raise Error(str(ex.args)[:100], ex)


            for eis_doc_obj in export_obj.get_children():

                xml_root_tag = eis_doc_obj.get_xml_tag()
                parser = parsers.get(xml_root_tag, None)
                if parser is None:
                    raise Error(f'No parser found for "{xml_root_tag}" document')

                with session.begin_nested():
                    parser(session, eis_doc_obj, update, **{'content_id' : content_to_parse.id}) 

            content_to_parse.status = FtpContentStatus.PROCESSED
            content_to_parse.message = None             
        
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

    return context 

def finalize(context):
    log.info(f'Finalized for {context.parse_module.__name__}')