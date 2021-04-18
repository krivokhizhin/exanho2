import enum

class MessageNew:

    def __init__(self) -> None:
        self.message = None
        self.client_info = None

class PrivateMessage:

    def __init__(self) -> None:
        self.id = None
        self.date = None
        self.peer_id = None
        self.from_id = None
        self.text = None
        self.random_id = None
        self.ref = None
        self.ref_source = None
        self.attachments = list()
        self.important = None
        self.geo = None
        self.payload = None
        self.keyboard = None
        self.fwd_messages = list()
        self.reply_message = None
        self.action = None
        self.admin_author_id = None
        self.conversation_message_id = None
        self.is_cropped = None
        self.members_count = None
        self.update_time = None
        self.was_listened = None
        self.pinned_at = None
        self.message_tag = None

class ClientInfo:

    def __init__(self) -> None:
        self.button_actions = list()
        self.keyboard = None
        self.inline_keyboard = None
        self.carousel = None
        self.lang_id = None

class Geo:

    def __init__(self) -> None:
        self.type_ = None
        self.latitude = None
        self.longitude = None
        self.place_id = None
        self.place_title = None
        self.place_latitude = None
        self.place_longitude = None
        self.place_created = None
        self.place_icon = None
        self.place_country = None
        self.place_city = None
        self.showmap = None

class Action:

    def __init__(self) -> None:
        self.type_ = None
        self.member_id = None
        self.text = None
        self.email = None
        self.photo_50 = None
        self.photo_100 = None
        self.photo_200 = None

class ActionType(enum.Enum):
    chat_photo_update = 1 # обновлена фотография беседы
    chat_photo_remove = 2 # удалена фотография беседы
    chat_create = 3 # создана беседа
    chat_title_update = 4 # обновлено название беседы
    chat_invite_user = 5 # приглашен пользователь
    chat_kick_user = 6 # исключен пользователь
    chat_pin_message = 7 # закреплено сообщение
    chat_unpin_message = 8 # откреплено сообщение
    chat_invite_user_by_link = 9 # пользователь присоединился к беседе по ссылке

        
class MessageReply(PrivateMessage):
    pass

class MessageEvent:

    def __init__(self) -> None:
        self.user_id = None
        self.peer_id = None
        self.event_id = None
        self.payload = None
        self.conversation_message_id = None