from .. import IVkDto, JSONObject

class SendMessageEventAnswerOptions(IVkDto):

    def __init__(self, **kwargs) -> None:
        self.event_id = kwargs.get('event_id', None)
        self.user_id = kwargs.get('user_id', None)
        self.peer_id = kwargs.get('peer_id', None)
        self.event_data = kwargs.get('event_data', list())

    def fill(self, json_obj: JSONObject):
        self.__dict__.update(json_obj.__dict__)