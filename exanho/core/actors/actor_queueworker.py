import importlib
import logging

from multiprocessing import Process, Event, JoinableQueue

from . import Actor, serve_forever
from .configs import QueueWorkerActorConfig

JOIN_TIMEOUT = 2
LAUNCHED_TIMEOUT = 2

class QueueWorker(Actor):
    pass

    def run(self, config, context):
        log = logging.getLogger(__name__)
        if not isinstance(config, QueueWorkerActorConfig):
            raise RuntimeError(f'{type(config)} type configuration, expected {QueueWorkerActorConfig} type')

        self._processes = []
        self.joinable_queues = set()
        worker_launched = Event()
        for index, worker_config in enumerate(config.workers):
            joinable_queue = context.joinable_queues.get(worker_config.queue_name)
            if joinable_queue is None:
                raise RuntimeError(f'Queue "{worker_config.queue_name}" in context not found.')

            worker_launched.clear()
            worker_name = f'{config.name}-{index+1}'
            thread_count = worker_config.factor_thread - 1

            p = Process(target=serve_forever, name=worker_name, args=(start_worker, context, worker_config.db_key, thread_count), daemon=True, kwargs={'worker_module': worker_config.module, 'joinable_queue': joinable_queue, 'appsettings': worker_config.appsettings, 'exanho_context': context, 'launched': worker_launched})
            p.start()
            
            self.joinable_queues.add(joinable_queue)
            self._processes.append(p)      
            worker_launched.wait(LAUNCHED_TIMEOUT)

            log.debug(f'Worker "{worker_name}" has been located in "{p.name}" process')

    def finalize(self):

        for joinable_queue in self.joinable_queues:
            joinable_queue.put(None)

        for p in self._processes:
            p.join(JOIN_TIMEOUT)
            if p.is_alive():
                p.terminate()

    def handle(self):
        pass

def start_worker(**kwargs):
    worker_module = kwargs['worker_module']
    joinable_queue = kwargs['joinable_queue']
    appsettings = kwargs['appsettings']
    exanho_context = kwargs['exanho_context']
    launched = kwargs['launched']

    import importlib
    mod = importlib.import_module(worker_module)

    context = mod.initialize(appsettings.__dict__ if appsettings else None, exanho_context)

    launched.set()

    while True:
        message = joinable_queue.get()
        if message is None:
            joinable_queue.task_done()
            joinable_queue.put(None)
            break

        try:
            context = mod.work(context, message)
        except Exception as ex:
            logging.getLogger(worker_module).exception(ex)

        joinable_queue.task_done()

    mod.finalize(context)


