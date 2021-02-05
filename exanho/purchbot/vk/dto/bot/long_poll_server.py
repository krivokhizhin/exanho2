from ..json_object import JSONObject
from ..method_response_base import MethodResponseBase
from .group_event import GroupEvent

class LongPollResponse(MethodResponseBase):
    
    def __init__(self) -> None:
        self.ts = None
        self.updates = list()
        self.failed = None
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'ts'):
            self.ts = json_obj.ts

        if hasattr(json_obj, 'updates') and len(json_obj.updates)>0:
            for event_json_obj in json_obj.updates:
                event = GroupEvent()
                event.fill(event_json_obj)
                self.updates.append(event)

        if hasattr(json_obj, 'failed'):
            self.failed = json_obj.failed