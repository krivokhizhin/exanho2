from .. import JSONObject, MethodResponseBase

class UploadFileResponse(MethodResponseBase):

    def __init__(self) -> None:
        super().__init__()
        self.file = None
    
    def fill(self, json_obj: JSONObject):
        if hasattr(json_obj, 'error'):
            self.fill_error(json_obj)
        elif hasattr(json_obj, 'file'):
            self.file = json_obj.file
        else:
            pass