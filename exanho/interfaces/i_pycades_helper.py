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

    @abstractmethod
    def sign(self, content:str, thumbprint:str, encoding_type:str, detached=True):
        pass

    @abstractmethod
    def sign_hash(self, hash:str, thumbprint:str, hash_alg:int):
        pass