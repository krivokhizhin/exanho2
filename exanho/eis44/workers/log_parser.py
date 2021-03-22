import datetime
import importlib
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.manager_context import Context as ExanhoContext
from exanho.orm.domain import Sessional

from ..model.aggregate import EisTableName, LogPlaceholder

log = logging.getLogger(__name__)

COUNT_TO_LOGGER = 50000

Context = namedtuple('Context', ['log_parser'])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    module_name = context.log_parser.strip()
    context = context._replace(log_parser=importlib.import_module(module_name))
    
    log.info(f'Initialized')
    return context

def work(context:Context):

    handled_count = 0

    with Sessional.domain.session_scope() as session:
        entity = context.log_parser.extract_unit(session)

        while entity:
            last_handled_publish_dt = context.log_parser.get_last_handled_publish_dt(session, *entity)
            if last_handled_publish_dt is None:
                last_handled_publish_dt = datetime.datetime(datetime.MINYEAR, 1, 1, tzinfo=datetime.timezone.utc)

            for source, doc_id, publish_dt in context.log_parser.unhandled_docs(session, *entity):
                try:
                    handled_count += 1
                    addition_only = True if publish_dt < last_handled_publish_dt else False
                    context.log_parser.handle(session, source, doc_id, addition_only, *entity)
                    context.log_parser.mark_as_handled(session, source, doc_id, *entity)
                    last_handled_publish_dt = max(last_handled_publish_dt, publish_dt)
                    session.commit()

                    if not (handled_count % COUNT_TO_LOGGER):
                        log.info(f'Another {COUNT_TO_LOGGER} log records were handled')
                except Exception as ex:
                    session.rollback()
                    log.exception(f'source={source}, doc_id={doc_id}', ex)

            log.debug(f'Log for {entity} entity has been parsed')
            entity = context.log_parser.extract_unit(session)

    if handled_count:
        log.info(f'All {handled_count} log records have been handled')

    return context 

def finalize(context:Context):
    context.log_parser.finalize()
    log.info(f'Finalized')