from . import JSONObject, IVkDto

class MethodResponseError(IVkDto):

    def __init__(self) -> None:
        self.error_code = None
        self.error_msg = None
        self.request_params = dict()
    
    def fill(self, json_obj: JSONObject):
        self.error_code = json_obj.error_code
        self.error_msg = json_obj.error_msg
        self.request_params.update([(param.key, param.value) for param in json_obj.request_params])