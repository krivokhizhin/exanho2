from .. import IVkDto, JSONObject

class SendAttachmentsOptions(IVkDto):

    def __init__(self, **kwargs) -> None:
        self.shm_name = kwargs.get('shm_name', None)
        self.shm_size = kwargs.get('shm_size', None)
        self.filename = kwargs.get('filename', None)
        self.peer_id = kwargs.get('peer_id', None)
        self.type = kwargs.get('type', None)
        self.group_id = kwargs.get('group_id', None)
        self.random_id = kwargs.get('random_id', None)
        self.payload = kwargs.get('payload', None)

    def fill(self, json_obj: JSONObject):
        self.__dict__.update(json_obj.__dict__)