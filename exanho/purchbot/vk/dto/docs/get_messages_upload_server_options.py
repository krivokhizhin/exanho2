from .. import IVkDto, JSONObject

class GetMessagesUploadServerOptions(IVkDto):

    def __init__(self, **kwargs) -> None:
        self.type = kwargs.get('type', None)
        self.peer_id = kwargs.get('peer_id', None)

    def fill(self, json_obj: JSONObject):
        self.__dict__.update(json_obj.__dict__)