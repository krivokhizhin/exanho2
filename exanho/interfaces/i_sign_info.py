from abc import ABC, abstractmethod

class ISignInfoService(ABC):
    
    @abstractmethod
    def by_content_sign(self, content:str, sign:str, encoding_type:str):
        pass
    
    @abstractmethod
    def by_file_hash_sign(self, _file:bytes, sign:str, hash_alg:int):
        pass
    
    @abstractmethod
    def by_hash_sign(self, hash:str, sign:str, hash_alg:int):
        pass