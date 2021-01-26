import importlib
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.manager_context import Context as ExanhoContext
from exanho.orm.domain import Sessional

from ..model.aggregate import EisTableName, LogPlaceholder

log = logging.getLogger(__name__)

Context = namedtuple('Context', ['log_placeholders'])

LogModulePH = namedtuple('LogModulePH', ['module', 'id'])

def get_log_placeholder(session:OrmSession, table_name:EisTableName) -> LogPlaceholder:
    placeholder = session.query(LogPlaceholder).filter(LogPlaceholder.source_table == table_name).one_or_none()
    if placeholder is None:
        placeholder = LogPlaceholder(source_table = table_name)
        session.add(placeholder)
        session.flush()
    return placeholder

def get_table_last_id(session:OrmSession, placeholder_id:int) -> int:
    return session.query(LogPlaceholder.last_id).filter(LogPlaceholder.id == placeholder_id).scalar()

def set_table_last_id(session:OrmSession, placeholder_id:int, last_id:int):
    state = session.query(LogPlaceholder).get(placeholder_id)
    state.last_id = last_id

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    modules = list()
    with Sessional.domain.session_scope() as session:
        for module_name in set(context.log_placeholders):
            mod = importlib.import_module(module_name.strip())
            placeholder = get_log_placeholder(session, mod.get_work_table_name())
            modules.append(LogModulePH(mod, placeholder.id))

    context = context._replace(log_placeholders=modules)
    
    log.info('Initialized')
    return context

def work(context:Context):
    with Sessional.domain.session_scope() as session:
        for log_placeholder in context.log_placeholders:
            table_name = log_placeholder.module.get_work_table_name().name
            try:
                last_id = get_table_last_id(session, log_placeholder.id)
                current_dto = log_placeholder.module.get_current_dto(session, last_id)
                while current_dto:
                    last_id = log_placeholder.module.add_to_log(session, current_dto)
                    set_table_last_id(session, log_placeholder.id, last_id)
                    session.commit()

                    log.debug(f'The document id={last_id} from {table_name} was placed in a log')
                    current_dto = log_placeholder.module.get_current_dto(session, last_id)
            except Exception as ex:
                session.rollback()
                log.exception('log_placeholder: ', ex)

    return context 

def finalize(context:Context):
    for log_placeholder in context.log_placeholders:
        log_placeholder.module.finalize()
    log.info(f'Finalized')