import json

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

    @staticmethod
    def loads(dto_str:str) -> dict:
        return json.loads(dto_str, object_hook=JSONObject)