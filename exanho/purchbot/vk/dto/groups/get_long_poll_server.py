from ..json_object import JSONObject
from ..i_vk_dto import IVkDto
from ..method_response_base import MethodResponseBase

class GetLongPollServerResponse(MethodResponseBase):

    def __init__(self) -> None:
        super().__init__()
        self.key = None
        self.server = None
        self.ts = None
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'response'):
            self.key = json_obj.response.key
            self.server = json_obj.response.server
            self.ts = json_obj.response.ts
        else:
            self.fill_error(json_obj)