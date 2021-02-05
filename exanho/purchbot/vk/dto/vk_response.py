from .json_object import JSONObject
from .method_response_base import MethodResponseBase

class VkResponse:

    def __init__(self, response:MethodResponseBase) -> None:
        self.response = response

    @classmethod
    def create(cls, dto:str, response_cls:type):
        assert issubclass(response_cls, MethodResponseBase)
        json_obj = JSONObject.loads(dto)
        obj = response_cls()
        obj.fill(json_obj)
        return cls(obj)