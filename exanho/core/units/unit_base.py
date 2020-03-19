import logging
import logging.handlers

from abc import ABC, abstractmethod

class ExanhoUnitBase(ABC):    
    
    def __init__(self, *args, **kwargs):
        self.config = kwargs.get('config')
        self.log_queue = kwargs.get('log_queue')  
        
        self.log = self.__class__.logger

    def initialize(self, *args, **kwargs):
        self._configurer_logging(self.log_queue)

    def _configurer_logging(self, queue):
        h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
        root = logging.getLogger('root')
        root.addHandler(h)
        root.setLevel(logging.DEBUG)

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

    @abstractmethod
    def shutdown(self, *args, **kwargs):
        pass

    # @staticmethod
    # @abstractmethod
    # def validate(*args, **kwargs):
    #     pass
    
    # @staticmethod
    # @abstractmethod
    # def terminate(*args, **kwargs):
    #     pass