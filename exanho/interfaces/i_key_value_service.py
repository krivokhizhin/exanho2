from abc import ABC, abstractmethod

class IKeyValueService(ABC):
    
    @abstractmethod
    def create(self, value):
        pass
    
    @abstractmethod
    def read(self, key):
        pass
    
    @abstractmethod
    def update(self, key, value):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass