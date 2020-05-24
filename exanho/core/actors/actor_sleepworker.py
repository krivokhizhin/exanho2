import importlib
import logging

from collections import defaultdict
from threading import Thread, Event

from . import Actor

TIMEOUT = 2

class SleepWorker(Actor):
    pass

    def run(self, *args, **kwargs):

        self.workers = []
        self.thread_terminated = Event()
        for index, worker_config in enumerate(self.config.workers):
            for n in range(worker_config.factor_thread):
                t = Thread(target=self.start_worker, args=(worker_config.module, worker_config.sleep, worker_config.appsettings), name=f'{self.config.name}_Thr#{index}{n}')
                t.daemon = self.config.daemon
                t.start()
                self.workers.append(t)

    def finalize(self): 

        self.thread_terminated.set()
        for worker in self.workers:
            worker.join(timeout=TIMEOUT)

    def handle(self):
        pass

    def start_worker(self, worker_module, timeout, appsettings):

        import importlib
        mod = importlib.import_module(worker_module)

        context = mod.initialize(appsettings.__dict__ if appsettings else None)

        while not self.thread_terminated.wait(timeout):
            try:
                context = mod.work(context)
            except Exception as ex:
                logging.getLogger(worker_module).exception(ex)

        mod.finalize(context)


