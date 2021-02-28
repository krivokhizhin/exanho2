from .. import IVkDto, JSONObject

class SaveDocsOptions(IVkDto):

    def __init__(self, **kwargs) -> None:
        self.file = kwargs.get('file', None)
        self.title = kwargs.get('title', None)
        self.tags = kwargs.get('tags', self.title)
        self.return_tags = kwargs.get('return_tags', 0)

    def fill(self, json_obj: JSONObject):
        self.__dict__.update(json_obj.__dict__)