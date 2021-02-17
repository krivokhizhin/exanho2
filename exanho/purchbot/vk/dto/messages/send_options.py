from .. import IVkDto, JSONObject

class SendOptions(IVkDto):

    def __init__(self, **kwargs) -> None:
        self.user_id = kwargs.get('user_id', None)
        self.random_id = kwargs.get('random_id', None)
        self.peer_id = kwargs.get('peer_id', None)
        self.peer_ids = kwargs.get('peer_ids', list())
        self.domain = kwargs.get('domain', None)
        self.chat_id = kwargs.get('chat_id', None)
        self.message = kwargs.get('message', None)
        self.lat = kwargs.get('lat', None)
        self.long = kwargs.get('long', None)
        self.attachment = kwargs.get('attachment', list())
        self.reply_to = kwargs.get('reply_to', None)
        self.forward_messages = kwargs.get('forward_messages', list())
        self.forward = kwargs.get('forward', None)
        self.sticker_id = kwargs.get('sticker_id', None)
        self.group_id = kwargs.get('group_id', None)
        self.keyboard = kwargs.get('keyboard', None)
        self.template = kwargs.get('template', None)
        self.payload = kwargs.get('payload', None)
        self.content_source = kwargs.get('content_source', None)
        self.dont_parse_links = kwargs.get('dont_parse_links', None)
        self.disable_mentions = kwargs.get('disable_mentions', None)
        self.intent = kwargs.get('intent', None)
        self.subscribe_id = kwargs.get('subscribe_id', None)

    def fill(self, json_obj: JSONObject):
        self.__dict__.update(json_obj.__dict__)