import importlib
import logging

from collections import defaultdict
from threading import Thread, Event
from multiprocessing import JoinableQueue

from . import Actor
from .configs import QueueWorkerActorConfig

TIMEOUT = 2

class QueueWorker(Actor):
    pass

    def run(self, *args, **kwargs):
        if not isinstance(self.config, QueueWorkerActorConfig):
            raise RuntimeError(f'{type(self.config)} type configuration, expected {QueueWorkerActorConfig} type')

        self.workers = []
        self.joinable_queues = set()
        for index, worker_config in enumerate(self.config.workers):
            for n in range(worker_config.factor_thread):

                joinable_queue = kwargs.get(worker_config.queue_name)
                if joinable_queue is None:
                    raise RuntimeError(f'Queue "{worker_config.queue_name}" in context not found.')

                t = Thread(target=self.start_worker, args=(worker_config.module, joinable_queue, worker_config.appsettings), name=f'{self.config.name}_Thr#{index}{n}')
                t.daemon = self.config.daemon
                t.start()

                self.joinable_queues.add(joinable_queue) 
                self.workers.append(t)

    def finalize(self): 

        for joinable_queue in self.joinable_queues:
            joinable_queue.put(None)

        for worker in self.workers:
            worker.join(timeout=TIMEOUT)

    def handle(self):
        pass

    def start_worker(self, worker_module, joinable_queue:JoinableQueue, appsettings):

        import importlib
        mod = importlib.import_module(worker_module)

        context = mod.initialize(appsettings.__dict__ if appsettings else None)

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


