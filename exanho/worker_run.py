from multiprocessing import Process
from .contract import UnitConfig
from .units import ExanhoUnitBase

class WorkerRun:

    def __init__(self, config: UnitConfig, process: Process, worker_class: ExanhoUnitBase):
        self.worker_name = config.name
        self.config = config
        self.process = process
        self._worker_class = worker_class

    def terminate(self):
        self._worker_class.terminate(self.config)