import logging
import random
import string

from xmlrpc.client import ServerProxy

from collections import defaultdict, namedtuple
from exanho.core.manager_context import Context as ExanhoContext

from exanho.interfaces import ISampleService
from exanho.core.common import create_client_class

log = logging.getLogger(__name__)

Context = namedtuple('Context', ['joinable_queue', 'exanho_context'], defaults=[None])

def initialize(appsettings, exanho_context:ExanhoContext):
    log.info(f'initialize')
    context = Context(**appsettings)
    random.seed()

    context = context._replace(joinable_queue=exanho_context.joinable_queues.get(context.joinable_queue), exanho_context=exanho_context)
    return context

def work(context:Context):
    log.info(f'work')

    task_number = ''.join([random.choice(string.hexdigits) for _ in range(10)])
    context.joinable_queue.put(task_number)
    log.info(f'Task "{task_number}" has been assigned.')

    host, port = context.exanho_context.get_service_endpoint(ISampleService)
    rpc_paths = '/'
    
    if host and port:
        client = ServerProxy(f'http://{host}:{port}{rpc_paths}', allow_none=True, use_builtin_types=True)
        client.execute(task_number)

    return context

def finalize(context):
    log.info(f'finalize')