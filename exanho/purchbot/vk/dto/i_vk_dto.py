from abc import ABC, abstractmethod

from .json_object import JSONObject

class IVkDto(ABC):
    
    @abstractmethod
    def fill(self, json_obj:JSONObject):
        pass