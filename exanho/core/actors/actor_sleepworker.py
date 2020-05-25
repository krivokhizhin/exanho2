import importlib
import logging

from collections import defaultdict
from threading import Thread, Event

from . import Actor
from .configs import SleepWorkerActorConfig

TIMEOUT = 2

class SleepWorker(Actor):
    pass

    def run(self, *args, **kwargs):
        if not isinstance(self.config, SleepWorkerActorConfig):
            raise RuntimeError(f'{type(self.config)} type configuration, expected {SleepWorkerActorConfig} type')

        joinable_queues = dict()
        if self.config.joinable_queues:
            for queue_name in self.config.joinable_queues:
                joinable_queue = kwargs.get(queue_name)
                if joinable_queue:
                    joinable_queues[queue_name] = joinable_queue

        self.workers = []
        self.thread_terminated = Event()
        for index, worker_config in enumerate(self.config.workers):
            for n in range(worker_config.factor_thread):
                t = Thread(target=self.start_worker, args=(worker_config.module, worker_config.sleep, worker_config.appsettings), kwargs=joinable_queues, name=f'{self.config.name}_Thr#{index}{n}')
                t.daemon = self.config.daemon
                t.start()
                self.workers.append(t)

    def finalize(self): 

        self.thread_terminated.set()
        for worker in self.workers:
            worker.join(timeout=TIMEOUT)

    def handle(self):
        pass

    def start_worker(self, worker_module, timeout, appsettings, **joinable_queues):

        import importlib
        mod = importlib.import_module(worker_module)

        context = mod.initialize(appsettings.__dict__ if appsettings else None, **joinable_queues)

        while not self.thread_terminated.wait(timeout):
            try:
                context = mod.work(context)
            except Exception as ex:
                logging.getLogger(worker_module).exception(ex)

        mod.finalize(context)


