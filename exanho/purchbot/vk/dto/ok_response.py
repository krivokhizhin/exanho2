from .json_object import JSONObject
from .method_response_base import MethodResponseBase

class OkResponse(MethodResponseBase):

    def __init__(self) -> None:
        super().__init__()
        self.id = None
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'response'):
            self.id = json_obj.response
        else:
            self.fill_error(json_obj)