import logging
import random
import string

from collections import defaultdict, namedtuple
# from multiprocessing import JoinableQueue

log = logging.getLogger(__name__)

Context = namedtuple('Context', ['joinable_queue'])

def initialize(appsettings=None, **joinable_queues):
    log.info(f'initialize')
    context = Context(**appsettings)
    random.seed()
    context = context._replace(joinable_queue=joinable_queues.get(context.joinable_queue))
    return context

def work(context:Context):
    log.info(f'work')

    task_number = ''.join([random.choice(string.hexdigits) for _ in range(10)])
    context.joinable_queue.put(task_number)
    log.info(f'Task "{task_number}" has been assigned.')

    return context

def finalize(context):
    log.info(f'finalize')