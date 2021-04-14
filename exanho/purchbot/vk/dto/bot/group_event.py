from .. import IVkDto, JSONObject

class GroupEvent(IVkDto):

    def __init__(self) -> None:
        self.type = None
        self.object = None
        self.group_id = None

    def fill(self, json_obj: JSONObject):
        self.type = json_obj.type
        self.object = json_obj.object
        self.group_id = json_obj.group_id