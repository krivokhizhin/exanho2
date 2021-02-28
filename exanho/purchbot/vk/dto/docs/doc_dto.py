from .. import JSONObject, IVkDto

class DocDto(IVkDto):

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id', None)
        self.owner_id = kwargs.get('owner_id', None)
        self.title = kwargs.get('title', None)
        self.size = kwargs.get('size', None)
        self.ext = kwargs.get('ext', None)
        self.url = kwargs.get('url', None)
        self.date = kwargs.get('date', None)
        self.type = kwargs.get('type', None)
        self.preview = kwargs.get('preview', None)

    def fill(self, json_obj: JSONObject):
        self.__dict__.update(json_obj.__dict__)