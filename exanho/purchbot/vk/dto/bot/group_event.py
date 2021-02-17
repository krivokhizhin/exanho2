from .. import IVkDto, JSONObject

class GroupEvent(IVkDto):

    def __init__(self) -> None:
        self.type_ = None
        self.object_ = None
        self.group_id = None

    def fill(self, json_obj: JSONObject):
        self.type_ = json_obj.type
        self.object_ = json_obj.object
        self.group_id = json_obj.group_id