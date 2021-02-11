import json

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

    def dumps(self, indent=None):
        dic = {}
        for key, value in self.__dict__.items():
            if isinstance(value, JSONObject):
                dic[key] = value.dumps()
            elif isinstance(value,list):
                dic.setdefault(key, [])
                for item in value:
                    if isinstance(item, JSONObject):
                        dic[key].append(item.dumps())
                    else:
                        dic[key].append(item)
            else:
                dic[key] = value
        return json.dumps(dic, indent=indent)

    @staticmethod
    def loads(dto_str:str):
        return json.loads(dto_str, object_hook=JSONObject)