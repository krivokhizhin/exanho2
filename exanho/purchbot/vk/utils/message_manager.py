from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error
from exanho.orm.domain import Sessional

from .vk_api_context import VkApiContext
from .client_context import ClientContext
from ..dto import JSONObject
from ..ui.payload import PayloadCommand, Payload
from ...utils import account_manager as acc_mngr
from ..utils import ui_manager as ui_mngr

from ...model import Client, VkUser

def handle_message_new(context:VkApiContext, message_new:JSONObject):    

    if hasattr(message_new, 'message'):

        client_context = get_client_context(message_new.message.from_id)

        if not hasattr(message_new.message, 'payload'):
            ui_mngr.show_main_menu(context, client_context)
            return

        payload = Payload()
        payload.fill(message_new.message.payload)

        payload_obj = message_new.message.payload
        if isinstance(payload_obj, str):
            payload_obj = JSONObject.loads(payload_obj.replace('\\"', '"').replace('\"', '"'))
        
        if hasattr(payload_obj, 'command'):
            ui_mngr.show_main_menu(context, client_context)
            return

        payload = Payload()
        payload.fill(
                payload_obj.command,
                context = payload_obj.context if hasattr(payload_obj, 'context') else None,
                page = payload_obj.page if hasattr(payload_obj, 'page') else None
            )

        match_payload()

    else:
        raise Error('There is not "message" element in "message_new" event')

def match_payload(payload:Payload, client_context:ClientContext, context:VkApiContext, message_new:JSONObject):
    if payload is None or payload.command is None or payload.command == PayloadCommand.start or payload.command == PayloadCommand.empty:
        ui_mngr.show_main_menu(context, client_context)
        return

    if payload.command == PayloadCommand.get_balance:
        pass
    elif payload.command == PayloadCommand.go_to_page:
        pass
    elif payload.command == PayloadCommand.menu_section_queries:
        pass
    elif payload.command == PayloadCommand.menu_section_subscriptions:
        pass
    elif payload.command == PayloadCommand.menu_section_reports:
        pass
    elif payload.command == PayloadCommand.menu_section_my_subscriptions:
        pass
    elif payload.command == PayloadCommand.menu_section_history:
        pass
    else:
        ui_mngr.show_main_menu(context, client_context)

def get_client_context(user_id:int) -> ClientContext:

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)
        vk_user = session.query(VkUser).filter(VkUser.user_id == user_id).one_or_none()

        if vk_user is None:
            client = Client()
            vk_user = VkUser(user_id = user_id)
            vk_user.client = client
            session.add_all([client, vk_user])
            session.flush()

            promo(session, client)

        free_balance = acc_mngr.get_free_balance(session, vk_user.client)
        promo_balance = acc_mngr.get_promo_balance(session, vk_user.client)

        return ClientContext(client=vk_user.client, vk_user_id=user_id, free_balance=free_balance, promo_balance=promo_balance)        

def promo(session:OrmSession, client:Client):
    PROMO_AMOUNT = Decimal('999.00')
    promo_remain = acc_mngr.get_promo_balance(session, client)

    if promo_remain > 0:
        return

    acc_mngr.deposit_promo_funds(session, client, PROMO_AMOUNT)