from abc import abstractmethod

from . import ExanhoUnitBase

class WorkerUnitBase(ExanhoUnitBase):

    @abstractmethod
    def _run_cycle(self):
        pass

    def run(self, *args, **kwargs):
        while True:
            try:
                self._run_cycle()
            except Exception as ex:
                self.log.exception(ex)