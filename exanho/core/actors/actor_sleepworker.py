import importlib
import logging
import multiprocessing
import threading

from collections import defaultdict

from . import Actor

TIMEOUT = 2

class SleepWorker(Actor):
    pass

    def run(self):

        self.workers = []
        self.worker_thread_terminated = threading.Event()
        self.worker_process_terminated = multiprocessing.Event()
        for worker_config in self.config.workers:
            if worker_config.concurrency:
                if worker_config.concurrency.kind.lower() == 'process':
                    for n in range(worker_config.concurrency.degree):
                        p = multiprocessing.Process(target=start_worker, args=(worker_config.module, worker_config.sleep, worker_config.appsettings, self.worker_process_terminated, self._log_queue), name=f'{self.config.name}_Pr#{n}')
                        p.daemon = worker_config.concurrency.daemon
                        p.start()
                        self.workers.append(p)
                elif worker_config.concurrency.kind.lower() == 'thread':
                    for n in range(worker_config.concurrency.degree):
                        t = threading.Thread(target=start_worker, args=(worker_config.module, worker_config.sleep, worker_config.appsettings, self.worker_thread_terminated, None), name=f'{self.config.name}_Thr#{n}')
                        t.daemon = worker_config.concurrency.daemon
                        t.start()
                        self.workers.append(t)
                else:
                    raise Exception(f'The concurrency_type is "{worker_config.concurrency.kind}". There must be either "Thread" or "Process"')
            else:
                t = threading.Thread(target=start_worker, args=(worker_config.module, worker_config.sleep, worker_config.appsettings, self.worker_thread_terminated, None), name=f'{self.config.name}_Thr_single')
                t.daemon = True
                t.start()
                self.workers.append(t)

    def finalize(self): 

        self.worker_thread_terminated.set()
        self.worker_process_terminated.set()
        for worker in self.workers:
            worker.join(timeout=TIMEOUT)
            if worker.is_alive() and isinstance(worker, multiprocessing.Process):
                worker.terminate()

    def handle(self):
        pass

def start_worker(worker_module, timeout, appsettings, event, log_queue):
    if log_queue:
        from exanho.core.common.log_utilities import configurer_logging
        configurer_logging(log_queue)

    import importlib
    mod = importlib.import_module(worker_module)

    log = logging.getLogger(worker_module)

    context = mod.initialize(appsettings.__dict__ if appsettings else None)

    while not event.wait(timeout):
        try:
            context = mod.work(context)
        except Exception as ex:
            log.exception(ex)

    mod.finalize(context)


