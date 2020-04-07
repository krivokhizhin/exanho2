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
            db_url = worker_config.db_domain.url if worker_config.db_domain else None
            db_validate = worker_config.db_domain.validate if worker_config.db_domain else None
            t = Thread(target=self.start_worker, args=(worker_config.module, worker_config.sleep, db_url, db_validate))
            t.daemon = True
            t.start()
            self.workers.append(t)

    def finalize(self):
        self.worker_terminated.set()
        for worker_thread in self.workers:
            worker_thread.join()

    def handle(self):
        pass

    def start_worker(self, worker_module, timeout, db_url, db_validate):
        import importlib
        mod = importlib.import_module(worker_module)

        mod.initialize(db_url=db_url, db_validate=db_validate)

        while not self.worker_terminated.wait(timeout):
            mod.work()

        mod.finalize()


