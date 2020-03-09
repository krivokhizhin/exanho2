import collections
import logging
import multiprocessing

from .common import ExitException
from . import WorkerRun, run_worker_wrapper
from .units.creators.get_creator import get_creator

class UnitManager:

    def __init__(self, log_queue):
        self.units = collections.defaultdict(WorkerRun)
        self.log_queue = log_queue

        self.log = logging.getLogger(__name__)

    def install_unit(self, config):
        if config.name in self.units:
            raise ValueError("Unit with name '{}' has been already installed early.".format(config.name))

        creator = get_creator(config.kind)
        # creator.validate()(config)

        process = multiprocessing.Process(target=run_worker_wrapper, args=(creator, ), kwargs={'config':config, 'log_queue':self.log_queue}, name=config.name)
        process.daemon = True

        self.units[config.name] = WorkerRun(config, process, creator.get_unit_class())

        self.units[config.name].process.start()

    def uninstall_unit(self, unit_name):
        if unit_name not in self.units:
            raise ValueError(f"Worker with name '{unit_name}' does not exist..")

        worker_run = self.units[unit_name]
        worker_run.terminate()
        worker_run.process.join(5) #1 sec TODO: parameterize

        if worker_run.process.is_alive():
            worker_run.process.terminate()
            worker_run.process.join() #1 sec TODO: parameterize
            self.log.warning(f"The process '{unit_name}' was  terminated directly.")

        if worker_run.process.is_alive():
            raise Exception(f"An attempt to terminate the process {unit_name} failed.")

        del self.units[unit_name]

    def get_worker_names(self, *args):
        return list(self.units.keys())

    def get_worker_configuration(self, worker_name):
        pass

    def stop_app(self, obj=None):
        raise ExitException()
