import collections
import logging
import multiprocessing

from .common import ExitException
from . import WorkerRun, run_worker_wrapper
from .units.creators.get_creator import get_creator

class WorkerManager:

    def __init__(self, log_queue):
        self.workers = collections.defaultdict(WorkerRun)
        self.log_queue = log_queue

        # self.log = logging.getLogger(__name__)

    def install_worker(self, config):
        if config.name in self.workers:
            raise ValueError("Worker with name '{}' has been already installed early.".format(config.name))

        creator = get_creator(config.kind)
        # creator.validate()(config)

        process = multiprocessing.Process(target=run_worker_wrapper, args=(creator, ), kwargs={'config':config, 'log_queue':self.log_queue}, name=config.name)
        # process.daemon = config.process_daemon

        self.workers[config.name] = WorkerRun(config, process, creator.get_unit_class())

        self.workers[config.name].process.start()

    def uninstall_worker(self, worker_name):
        if worker_name not in self.workers:
            raise ValueError(f"Worker with name '{worker_name}' does not exist..")

        worker_run = self.workers[worker_name]
        worker_run.terminate()
        worker_run.process.join(5) #1 sec TODO: parameterize

        if worker_run.process.is_alive():
            worker_run.process.terminate()
            worker_run.process.join() #1 sec TODO: parameterize
            self.log.warning(f"The process '{worker_name}' was  terminated directly.")

        if worker_run.process.is_alive():
            raise Exception(f"An attempt to terminate the process {worker_name} failed.")

        del self.workers[worker_name]

    def get_worker_names(self, *args):
        return list(self.workers.keys())

    def get_worker_configuration(self, worker_name):
        pass

    def stop_app(self, obj=None):
        raise ExitException()
