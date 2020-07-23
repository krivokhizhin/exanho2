import importlib
import logging

from multiprocessing import Process, Event

from . import Actor, serve_forever
from .configs import SleepWorkerActorConfig

JOIN_TIMEOUT = 2
LAUNCHED_TIMEOUT = 2

class SleepWorker(Actor):

    def run(self, config, context):
        log = logging.getLogger(__name__)
        if not isinstance(config, SleepWorkerActorConfig):
            raise RuntimeError(f'{type(self.config)} type configuration, expected {SleepWorkerActorConfig} type')

        self._processes = []
        self.worker_terminated = Event()
        worker_launched = Event()
        for index, worker_config in enumerate(config.workers):
            worker_launched.clear()
            worker_name = f'{config.name}-{index+1}'
            thread_count = worker_config.factor_thread - 1

            p = Process(target=serve_forever, name=worker_name, args=(start_worker, context, worker_config.db_key, thread_count), daemon=True, kwargs={'worker_module': worker_config.module, 'timeout': worker_config.sleep, 'appsettings': worker_config.appsettings, 'exanho_context': context, 'terminated': self.worker_terminated, 'launched': worker_launched})
            p.start()
            
            self._processes.append(p)
            globals()['JOIN_TIMEOUT'] = max([JOIN_TIMEOUT, worker_config.sleep])       
            worker_launched.wait(LAUNCHED_TIMEOUT)

            log.debug(f'Worker "{worker_name}" has been located in "{p.name}" process')

    def finalize(self): 

        self.worker_terminated.set()
        for p in self._processes:
            p.join(JOIN_TIMEOUT)
            if p.is_alive():
                p.terminate()

    def handle(self):
            pass

def start_worker(**kwargs):
    worker_module = kwargs['worker_module']
    timeout = kwargs['timeout']
    appsettings = kwargs['appsettings']
    exanho_context = kwargs['exanho_context']
    launched = kwargs['launched']
    terminated = kwargs['terminated']

    import importlib
    mod = importlib.import_module(worker_module)

    context = mod.initialize(appsettings.__dict__ if appsettings else None, exanho_context)

    launched.set()

    while not terminated.wait(timeout):
        try:
            context = mod.work(context)
        except Exception as ex:
            logging.getLogger(worker_module).exception(ex)

    mod.finalize(context)