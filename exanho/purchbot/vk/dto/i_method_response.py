from abc import abstractmethod

from . import IVkDto, JSONObject

class IMethodResponse(IVkDto):
    
    @abstractmethod
    def fill_error(self, json_obj:JSONObject):
        pass