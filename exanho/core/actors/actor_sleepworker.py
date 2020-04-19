import importlib
import logging

from collections import defaultdict
from threading import Thread, Event

from . import Actor

class SleepWorker(Actor):
    pass

    def run(self):
        log = logging.getLogger(__name__)

        self.workers = []
        self.worker_terminated = Event()
        for worker_config in self.config.workers:
            t = Thread(target=self.start_worker, args=(worker_config.module, worker_config.sleep, worker_config.appsettings))
            t.daemon = True
            t.start()
            self.workers.append(t)

    def finalize(self):
        self.worker_terminated.set()
        for worker_thread in self.workers:
            worker_thread.join()

    def handle(self):
        pass

    def start_worker(self, worker_module, timeout, appsettings):
        import importlib
        mod = importlib.import_module(worker_module)

        context = mod.initialize(appsettings.__dict__ if appsettings else None)

        while not self.worker_terminated.wait(timeout):
            try:
                context = mod.work(context)
            except Exception as ex:
                logging.getLogger(worker_module).exception(ex)

        mod.finalize(context)


