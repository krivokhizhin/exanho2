import datetime
import decimal

from ..dto import JSONObject
from ...utils import json64 as json_util

# from .payload import Payload, PayloadCommand
from ..ui.payload import PayloadCommand, Payload
from .message import PrivateMessage, ClientInfo, MessageNew, MessageReply, MessageEvent
from .vkpay_transaction import VkpayTransaction

# ---------- begin payload ----------------

def get_payload(dto) -> Payload:
    if dto is None: return None
    if isinstance(dto, str):
        dto = json_util.convert_json_str_to_obj(dto.replace('\\"', '"').replace('\"', '"'), JSONObject)
    payload = Payload()
    fill_payload(payload, dto)
    return payload

def fill_payload(payload:Payload, dto:JSONObject):
    if hasattr(dto, 'command') and isinstance(dto.command, str):
        try:
            payload.command = PayloadCommand[dto.command]
        except:
            pass

    if hasattr(dto, 'product') and isinstance(dto.product, str): payload.product = dto.product
    if hasattr(dto, 'page') and isinstance(dto.page, int): payload.page = dto.page
    if hasattr(dto, 'order') and isinstance(dto.order, int): payload.order = dto.order
    if hasattr(dto, 'add_info') and isinstance(dto.add_info, int): payload.add_info = dto.add_info
    if hasattr(dto, 'par_number') and isinstance(dto.par_number, int): payload.par_number = dto.par_number
    if hasattr(dto, 'par_value'): payload.par_value = str(dto.par_value)
    if hasattr(dto, 'content'): payload.content = str(dto.content)
    if hasattr(dto, 'go_to') and isinstance(dto.go_to, int): payload.go_to = dto.go_to
    if hasattr(dto, 'event') and isinstance(dto.event, str): payload.event = dto.event

# ---------- end payload ----------------

# ---------- begin message event ----------------

def get_message_new(dto:JSONObject) -> MessageNew:
    if not isinstance(dto, JSONObject): return None
    event = MessageNew()
    fill_message_new(event, dto)
    return event

def get_message_reply(dto:JSONObject) -> MessageReply:
    if not isinstance(dto, JSONObject): return None
    event = MessageReply()
    fill_private_message(event, dto)
    return event

def get_message_event(dto:JSONObject) -> MessageEvent:
    if not isinstance(dto, JSONObject): return None
    event = MessageEvent()
    fill_message_event(event, dto)
    return event

def fill_message_new(event:MessageNew, dto:JSONObject):
    if hasattr(dto, 'message'): event.message = get_private_message(dto.message)
    if hasattr(dto, 'client_info'): event.client_info = get_message_client_info(dto.client_info)    

def get_private_message(dto:JSONObject) -> PrivateMessage:
    if not isinstance(dto, JSONObject): return None
    message = PrivateMessage()
    fill_private_message(message, dto)
    return message

def fill_private_message(event:PrivateMessage, dto:JSONObject):
    if hasattr(dto, 'id') and isinstance(dto.id, int): event.id = dto.id
    if hasattr(dto, 'date') and isinstance(dto.date, int): event.date = datetime.datetime.fromtimestamp(dto.date)
    if hasattr(dto, 'peer_id') and isinstance(dto.peer_id, int): event.peer_id = dto.peer_id
    if hasattr(dto, 'from_id') and isinstance(dto.from_id, int): event.from_id = dto.from_id
    if hasattr(dto, 'text') and isinstance(dto.text, str): event.text = dto.text
    if hasattr(dto, 'random_id') and isinstance(dto.random_id, int): event.random_id = dto.random_id
    if hasattr(dto, 'ref') and isinstance(dto.ref, str): event.ref = dto.ref
    if hasattr(dto, 'ref_source') and isinstance(dto.ref_source, str): event.ref_source = dto.ref_source
    # attachments
    if hasattr(dto, 'important') and isinstance(dto.important, bool): event.important = dto.important
    # geo
    if hasattr(dto, 'payload'): event.payload = get_payload(dto.payload)
    # keyboard
    if hasattr(dto, 'fwd_messages') and isinstance(dto.fwd_messages, list):
        for fwd_message in dto.fwd_messages:
            event.fwd_messages.append(get_message_new(fwd_message))
    if hasattr(dto, 'reply_message'): event.reply_message = get_message_new(dto.reply_message)
    # action
    if hasattr(dto, 'admin_author_id') and isinstance(dto.admin_author_id, int): event.admin_author_id = dto.admin_author_id
    if hasattr(dto, 'conversation_message_id') and isinstance(dto.conversation_message_id, int): event.conversation_message_id = dto.conversation_message_id
    if hasattr(dto, 'is_cropped') and isinstance(dto.is_cropped, bool): event.is_cropped = dto.is_cropped
    if hasattr(dto, 'members_count') and isinstance(dto.members_count, int): event.members_count = dto.members_count
    if hasattr(dto, 'update_time') and isinstance(dto.update_time, int): event.update_time = datetime.date.fromtimestamp(dto.update_time)
    if hasattr(dto, 'was_listened') and isinstance(dto.was_listened, bool): event.was_listened = dto.was_listened
    if hasattr(dto, 'pinned_at') and isinstance(dto.pinned_at, int): event.pinned_at = datetime.date.fromtimestamp(dto.pinned_at)
    if hasattr(dto, 'message_tag') and isinstance(dto.message_tag, str): event.message_tag = dto.message_tag

# def get_message_new_dto(event:message_new.MessageNew) -> JSONObject:
#     pass

def get_message_client_info(dto:JSONObject) -> ClientInfo:
    if not isinstance(dto, JSONObject): return None
    client_info = ClientInfo()
    fill_message_client_info(client_info, dto)
    return client_info

def fill_message_client_info(client_info:ClientInfo, dto:JSONObject):
    if hasattr(dto, 'button_actions') and isinstance(dto.button_actions, list):
        for button_action in dto.button_actions:
            client_info.button_actions.append(button_action)
    if hasattr(dto, 'keyboard') and isinstance(dto.keyboard, bool): client_info.keyboard = dto.keyboard
    if hasattr(dto, 'inline_keyboard') and isinstance(dto.inline_keyboard, bool): client_info.inline_keyboard = dto.inline_keyboard
    if hasattr(dto, 'carousel') and isinstance(dto.carousel, bool): client_info.carousel = dto.carousel
    if hasattr(dto, 'lang_id') and isinstance(dto.lang_id, int): client_info.lang_id = dto.lang_id

def fill_message_event(event:MessageEvent, dto:JSONObject):
    if hasattr(dto, 'user_id') and isinstance(dto.user_id, int): event.user_id = dto.user_id
    if hasattr(dto, 'peer_id') and isinstance(dto.peer_id, int): event.peer_id = dto.peer_id
    if hasattr(dto, 'event_id') and isinstance(dto.event_id, str): event.event_id = dto.event_id
    if hasattr(dto, 'payload'): event.payload = get_payload(dto.payload)
    if hasattr(dto, 'conversation_message_id') and isinstance(dto.conversation_message_id, int): event.conversation_message_id = dto.conversation_message_id


# ---------- end message event ----------------

# ---------- begin vkpay_transaction event ----------------

def get_vkpay_transaction(dto:JSONObject) -> VkpayTransaction:
    if not isinstance(dto, JSONObject): return None
    event = VkpayTransaction()
    fill_vkpay_transaction(event, dto)
    return event

def fill_vkpay_transaction(event:VkpayTransaction, dto:JSONObject):
    if hasattr(dto, 'from_id') and isinstance(dto.from_id, int): event.from_id = dto.from_id
    if hasattr(dto, 'amount'): event.amount = decimal.Decimal(str(dto.amount))
    if hasattr(dto, 'description') and isinstance(dto.description, str): event.description = dto.description
    if hasattr(dto, 'date') and isinstance(dto.date, int): event.date = datetime.date.fromtimestamp(dto.date)

# ---------- end vkpay_transaction event ----------------