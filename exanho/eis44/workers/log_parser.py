import datetime
import importlib
import logging

from collections import namedtuple
from multiprocessing import JoinableQueue
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.manager_context import Context as ExanhoContext
from exanho.orm.domain import Sessional

log = logging.getLogger(__name__)

COUNT_TO_LOGGER = 5000
BATCH_COUNT_TO_LOGGER = 100

Context = namedtuple('Context', ['log_parser', 'log_parser_queue', 'batch_size'], defaults=[None, 1])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    module_name = context.log_parser.strip()
    context = context._replace(log_parser=importlib.import_module(module_name))

    if context.batch_size > 1:
        context = context._replace(log_parser_queue=exanho_context.joinable_queues[context.log_parser_queue])
    
    log.info(f'Initialized')
    return context

def work(context:Context):

    handled_count = 0

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)
        if context.batch_size > 1:
            consumer_queue:JoinableQueue = context.log_parser_queue
            entities = context.log_parser.extract_units(session, context.batch_size)
            while entities:
                handled_count += 1
                for entity in entities:
                    consumer_queue.put(entity)
                consumer_queue.join()
                if not (handled_count % BATCH_COUNT_TO_LOGGER):
                    log.info(f'Another {BATCH_COUNT_TO_LOGGER} batch log records were handled')
                entities = context.log_parser.extract_units(session, context.batch_size)

            if handled_count:
                log.info(f'All {handled_count} batch log records have been handled')
        else:
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