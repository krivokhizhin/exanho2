from .. import JSONObject, MethodResponseBase

class SendResponse(MethodResponseBase):

    def __init__(self) -> None:
        super().__init__()
        self.id = None
        self.peer_id = None
        self.message_id = None
        self.conversation_message_id = None
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'error'):
            self.fill_error(json_obj)
        elif hasattr(json_obj, 'response'):
            if isinstance(json_obj.response, JSONObject):
                self.peer_id = json_obj.response.peer_id
                self.message_id = json_obj.response.message_id
                self.conversation_message_id = json_obj.response.conversation_message_id
            else:
                self.id = json_obj.response
        else:
            pass