import importlib
import logging
from collections import namedtuple

from exanho.core.manager_context import Context as ExanhoContext

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'placeholder_module',
    'source_db_key'
    ])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    mod = importlib.import_module(context.placeholder_module.strip())
    context = context._replace(placeholder_module=mod)

    context.placeholder_module.initialize(exanho_context.get_domain(context.source_db_key))
    
    log.info(f'Initialized for {context.placeholder_module}')
    return context

def work(context:Context):
    context.placeholder_module.perform()
    return context 

def finalize(context:Context):
    context.placeholder_module.finalize()
    log.info(f'Finalized for {context.parse_module.__name__}')