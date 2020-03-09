from ..common import JsonObject

class UnitConfig():

    def __init__(self, json_obj: JsonObject):
        self._name = json_obj.name
        self._kind = json_obj.kind

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @classmethod
    def create_instance(cls, json_obj : JsonObject):
        return cls(json_obj)

class HasDbConnect():
    def __init__(self, json_obj: JsonObject):
        super().__init__(json_obj)
        
        self._db_url = json_obj.db_url if hasattr(json_obj, 'db_url') else None

    @property
    def db_url(self):
        return self._db_url

class HasHandler():

    def __init__(self, json_obj: JsonObject):
        super().__init__(json_obj)

        self._handler = json_obj.handler_module

    @property
    def handler(self):
        return self._handler