from . import JSONObject, IMethodResponse, MethodResponseError

class MethodResponseBase(IMethodResponse):

    def __init__(self) -> None:
        self.error = None
    
    def fill_error(self, json_obj: JSONObject):
        self.error = MethodResponseError()
        if hasattr(json_obj, 'error'):
            self.error.fill(json_obj.error)
        else:
            self.error.error_code = -100
            self.error.error_msg = 'root element "error" not found'
            self.error.request_params = json_obj.__dict__