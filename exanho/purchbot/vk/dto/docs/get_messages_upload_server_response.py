from .. import JSONObject, MethodResponseBase

class GetMessagesUploadServerResponse(MethodResponseBase):

    def __init__(self) -> None:
        super().__init__()
        self.upload_url = None
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'error'):
            self.fill_error(json_obj)
        elif hasattr(json_obj, 'response'):
            if isinstance(json_obj.response, JSONObject):
                self.upload_url = json_obj.response.upload_url
            else:
                self.upload_url = json_obj.response
        else:
            pass