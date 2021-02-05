from abc import ABC, abstractmethod

class IVkDriver(ABC):
    
    @abstractmethod
    def get_response(self, *args, **kwargs):
        pass