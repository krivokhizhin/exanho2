from abc import ABC, abstractmethod

class IPycadesHelperService(ABC):
    
    @abstractmethod
    def hash_gost_2012_512(self, data:bytes):
        pass
    
    @abstractmethod
    def hash_gost_2012_256(self, data:bytes):
        pass
    
    @abstractmethod
    def hash_gost_3411(self, data:bytes):
        pass