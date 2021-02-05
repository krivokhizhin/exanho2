from abc import abstractmethod

from .i_vk_dto import IVkDto
from .json_object import JSONObject

class IMethodResponse(IVkDto):
    
    @abstractmethod
    def fill_error(self, json_obj:JSONObject):
        pass