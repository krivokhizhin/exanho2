import datetime
import importlib
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.manager_context import Context as ExanhoContext
from exanho.orm.domain import Sessional

log = logging.getLogger(__name__)

Context = namedtuple('Context', ['log_parser'])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    module_name = context.log_parser.strip()
    context = context._replace(log_parser=importlib.import_module(module_name))
    
    log.info(f'Initialized')
    return context

def work(context:Context, message):
    reg_num:str = message

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)

        last_handled_publish_dt = context.log_parser.get_last_handled_publish_dt(session, *reg_num)
        if last_handled_publish_dt is None:
            last_handled_publish_dt = datetime.datetime(datetime.MINYEAR, 1, 1, tzinfo=datetime.timezone.utc)

        for source, doc_id, publish_dt in context.log_parser.unhandled_docs(session, *reg_num):
            try:
                addition_only = True if publish_dt < last_handled_publish_dt else False
                context.log_parser.handle(session, source, doc_id, addition_only, *reg_num)
                context.log_parser.mark_as_handled(session, source, doc_id, *reg_num)
                last_handled_publish_dt = max(last_handled_publish_dt, publish_dt)
                session.commit()

            except Exception as ex:
                session.rollback()
                log.exception(f'source={source}, doc_id={doc_id}', ex)

    log.debug(f'Log records for reg_num={reg_num} have been handled')

    return context 

def finalize(context:Context):
    context.log_parser.finalize()
    log.info(f'Finalized')