from abc import ABC, abstractmethod

class ISampleService2(ABC):
    
    @abstractmethod
    def echo(self, *args, **kwargs):
        pass