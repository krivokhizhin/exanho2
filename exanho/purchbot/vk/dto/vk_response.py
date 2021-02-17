from . import JSONObject, MethodResponseBase
from . import util as dto_util

class VkResponse:

    def __init__(self, response:MethodResponseBase) -> None:
        self.response = response

    @classmethod
    def create(cls, dto:str, response_cls:type):
        assert issubclass(response_cls, MethodResponseBase)
        json_obj = dto_util.convert_json_str_to_obj(dto, JSONObject)
        obj = response_cls()
        obj.fill(json_obj)
        return cls(obj)