from abc import ABC, abstractmethod

class ISampleService(ABC):
    
    @abstractmethod
    def echo(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def load(self, load = 10000000):
        pass
    
    @abstractmethod
    def raise_ex(self, message = 'raise Exception'):
        pass
    
    # @abstractmethod
    # def execute(self, task):
    #     pass