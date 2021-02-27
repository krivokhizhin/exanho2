from abc import ABC, abstractmethod

class IVkDriver(ABC):
    
    @abstractmethod
    def get(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def post(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def upload_file(self, *args, **kwargs):
        pass