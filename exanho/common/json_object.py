import json

class JsonObject:

    def __init__(self, dic_dto):
        if not isinstance(dic_dto, dict):
            raise TypeError('Expected a dict, but {} is received.'.format(type(dic_dto)))

        #TODO: check dict key by class dto fields

        self.__dict__ = dic_dto

    def json_dumps(self):
        return json.dumps(self.__dict__)

    @classmethod
    def create_from_file(cls, filename):
        with open(filename, 'r') as f:
            dto = json.load(f, object_hook=cls)

        return dto