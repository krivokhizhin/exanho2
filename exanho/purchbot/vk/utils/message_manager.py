import logging
import re
from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error

from .vk_bot_context import VkBotContext
from .client_context import ClientContext
from ..dto import JSONObject
from ..ui import PayloadCommand, Payload

from ...utils import json64 as json_util
from ...utils import account_manager as acc_mngr
from ...utils import order_manager as order_mngr
from ...utils import eis_service
from ..utils import client as clt_eng
from ..utils import ui_manager as ui_mngr

from ..events.message import MessageEvent, MessageReply, PrivateMessage, MessageNew

from ...model import ProductKind, Product, Client, VkUser, OrderStatus, Order, AddInfoCode, LastOrderDetailing

log = logging.getLogger(__name__)

def handle_message_new(session:OrmSession, context:VkBotContext, message_new:MessageNew):
    message:PrivateMessage = message_new.message

    client_context = clt_eng.get_client_context(session, message.from_id, promo=True)

    if message.payload is None:
        last_order_detail = session.query(LastOrderDetailing).filter(LastOrderDetailing.client_id == client_context.client_id).\
            filter(LastOrderDetailing.handled == False).one_or_none()
        if last_order_detail:
            message.payload = Payload(
                command = PayloadCommand.detailing_order,
                page = 1,
                order = last_order_detail.order_id,
                par_number = last_order_detail.par_number,
                add_info = last_order_detail.add_info.value,
                content = message.text
            )

    if message.payload is None:
        ui_mngr.show_main_menu(session, context, client_context, 'Меню (см. клавиатуру под строкой ввода)')
        return

    match_payload(session, message.payload, client_context, context)

def handle_message_event(session:OrmSession, context:VkBotContext, message_event:MessageEvent):     

    client_context = clt_eng.get_client_context(session, message_event.user_id, promo=True)

    if message_event.payload is None:
        last_order_detail = session.query(LastOrderDetailing).filter(LastOrderDetailing.client_id == client_context.client_id).\
            filter(LastOrderDetailing.handled == False).one_or_none()
        if last_order_detail:
            message_event.payload = Payload(
                command = PayloadCommand.detailing_order,
                page = 1,
                order = last_order_detail.order_id,
                par_number = last_order_detail.par_number,
                add_info = last_order_detail.add_info.value,
                event = message_event.event_id
            )

    if message_event.payload is None:
        ui_mngr.show_main_menu(session, context, client_context)
        return

    message_event.payload.event = message_event.event_id

    match_payload(session, message_event.payload, client_context, context)

def handle_message_reply(session:OrmSession, context:VkBotContext, message_reply:MessageReply):

    client_context = clt_eng.get_client_context(session, message_reply.peer_id, promo=True)

    match_payload(session, message_reply.payload, client_context, context)


def match_payload(session:OrmSession, payload:Payload, client_context:ClientContext, context:VkBotContext):
    if payload is None or payload.command is None or payload.command == PayloadCommand.empty:
        return

    if payload.command == PayloadCommand.get_balance:
        ui_mngr.show_balance(session, context, client_context)
    elif payload.command == PayloadCommand.menu_section_queries:
        ui_mngr.show_products_by_kind(session, context, client_context, ProductKind.QUERY, payload)
    elif payload.command == PayloadCommand.menu_section_subscriptions:
        ui_mngr.show_products_by_kind(session, context, client_context, ProductKind.SUBSCRIPTION, payload)
    elif payload.command == PayloadCommand.menu_section_reports:
        ui_mngr.show_products_by_kind(session, context, client_context, ProductKind.REPORT, payload)
    elif payload.command == PayloadCommand.go_to_page:
        go_to(session, payload, client_context, context)
    elif payload.command == PayloadCommand.request_product:
        request_product(session, context, client_context, payload)
    elif payload.command == PayloadCommand.detailing_order:
        detailing_order(session, context, client_context, payload)
    elif payload.command == PayloadCommand.selection_add_info:
        selection_add_info(session, context, client_context, payload)
    elif payload.command == PayloadCommand.confirm_order:
        confirm_order(session, context, client_context, payload)
    elif payload.command == PayloadCommand.edit_order:
        edit_order(session, context, client_context, payload)
    elif payload.command == PayloadCommand.cancel_order:
        cancel_order(session, context, client_context, payload)
    elif payload.command == PayloadCommand.order_executed:
        order_executed(session, context, client_context, payload)
    elif payload.command == PayloadCommand.menu_section_my_subscriptions:
        log.debug(f'VK user (id={client_context.vk_user_id}) pressed {PayloadCommand.menu_section_my_subscriptions.name.upper()}')
    elif payload.command == PayloadCommand.menu_section_history:
        ui_mngr.show_history(session, context, client_context)
    else:
        ui_mngr.show_main_menu(session, context, client_context)

def go_to(session:OrmSession, payload:Payload, client_context:ClientContext, context:VkBotContext):
    try:
        payload.command = PayloadCommand[payload.go_to]
    except:
        return

    match_payload(session, payload, client_context, context)

def request_product(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    product_code:str = payload.product

    order_id = order_mngr.create_or_get_order(session, product_code, client_context.client_id)

    par_number = order_mngr.get_first_empty_num_parameter_or_none(session, order_id)

    ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Принято')
    if par_number:
        ui_mngr.show_detailing_order_message(session, vk_context, client_context, order_id, par_number)
    else:
        order_mngr.mark_as_filling(session, order_id)
        ui_mngr.show_confirmation_order(session, vk_context, client_context, order_id)

def detailing_order(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    text = payload.content

    if text is None:
        return

    if payload.add_info is None:
        return

    if payload.add_info == AddInfoCode.PARTICIPANT.value:
        inn, kpp = extract_inn_kpp_from_text(text)
        if inn:            
            payload.content = '{} {}'.format(inn, kpp) if kpp else inn
            ui_mngr.detailing_order_by_participant(session, vk_context, client_context, payload, inn, kpp)
        else:
            ui_mngr.show_main_menu(session, vk_context, client_context, 'В сообщении как минимум должны быть указаны 10 или 12 цифр подряд (формат ИНН)')
    elif payload.add_info == AddInfoCode.CUSTOMER.value:
        pass
    elif payload.add_info == AddInfoCode.NOTIFICATION.value:
        pass
    elif payload.add_info == AddInfoCode.CONTRACT.value:
        pass
    else:
        return

def extract_inn_kpp_from_text(text:str):
    pattern = r'(?P<inn>\d{12}|\d{10})(?:\D+(?P<kpp>\d{9}))?'
    match = re.search(pattern, text)

    if match:
        return match.group('inn'), match.group('kpp')
    else:
        return None, None

def selection_add_info(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    order_id:int = payload.order
    par_number:int = payload.par_number
    par_value:str = str(payload.par_value)

    order_id = order_mngr.check_actual_order(session, order_id)
    order_mngr.set_parameter_by_number(session, order_id, par_number, par_value)
    par_number = order_mngr.get_first_empty_num_parameter_or_none(session, order_id)

    if par_number:
        ui_mngr.show_detailing_order_message(session, vk_context, client_context, order_id, par_number)
    else:
        order_mngr.mark_as_filling(session, order_id)
        ui_mngr.show_confirmation_order(session, vk_context, client_context, order_id)

def confirm_order(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    order_id:int = payload.order

    if not order_mngr.check_status(session, order_id, OrderStatus.FILLING):
        ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Подтверждение невозможно. Отредактируйте заказ или оформите услугу заново.')
        return
    
    if order_mngr.hold_fee(session, order_id):
        log.debug(f'order_mngr.hold_fee, event: {payload.event}')
        ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Принято')
    else:
        ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Недостаточно средств! Пополните, пожалуйста, баланс.')
        return

    free_balance = acc_mngr.free_balance_by_client(session, client_context.client_id)
    promo_balance = acc_mngr.promo_balance_by_client(session, client_context.client_id)

    client_context = client_context._replace(free_balance=free_balance, promo_balance=promo_balance)

    execute_order(session, vk_context, client_context, payload, order_id)

    order_mngr.mark_as_during(session, order_id)

def execute_order(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, order_id:int):
    order = session.query(Order).get(order_id)
    product_code = session.query(Product.code).filter(Product.id == order.product_id).scalar()

    result = None
    ui_method = None

    try: # TODO: to separeted module

        if product_code == 'QUE_PAR_ACT':
            result = eis_service.get_current_participant_activity(vk_context.participant_service, int(order.parameter1))
            if isinstance(result, Error):
                raise result
            ui_method = ui_mngr.show_que_par_act_result

        if product_code == 'QUE_PAR_HIS':
            result = eis_service.get_participant_experience(vk_context.participant_service, int(order.parameter1))
            if isinstance(result, Error):
                raise result
            ui_method = ui_mngr.show_que_par_his_result

        if product_code == 'SUB_PAR':
            result = eis_service.get_last_participant_events(vk_context.participant_service, int(order.parameter1))
            if isinstance(result, Error):
                raise result
            ui_method = ui_mngr.show_sub_par_subscription

        if product_code == 'REP_PAR_ACT':
            result = eis_service.get_current_participant_activity_report(vk_context.participant_service, int(order.parameter1))
            if isinstance(result, Error):
                raise result
            ui_method = ui_mngr.show_rep_par_act_result

        if product_code == 'REP_PAR_HIS':
            result = eis_service.get_participant_experience_report(vk_context.participant_service, int(order.parameter1))
            if isinstance(result, Error):
                raise result
            ui_method = ui_mngr.show_rep_par_his_result

        if product_code == 'REP_PARS_CON':
            pass

    except Error as er:
        log.error(f'eis_service: "{er.message}" method call error')
        ui_mngr.show_main_menu(session, vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        session.rollback()
        return
    except Exception as ex:
        log.exception(f'eis_service: method for order_id={order_id} call error', ex.args)
        ui_mngr.show_main_menu(session, vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        session.rollback()
        return

    exec_payload = Payload(
        command = PayloadCommand.order_executed,
        order = order_id,
        event = payload.event
    )
    ui_method(session, vk_context, client_context, exec_payload, result)

def edit_order(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    order_id:int = payload.order

    if not order_mngr.check_status(session, order_id, OrderStatus.DURING, OrderStatus.COMPLETED):
        ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Редактирование невозможно. Услуга оказана ранее.')
        return

    order_mngr.reset(session, order_id)
    ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, f'Заказ №{order_id} доступен для редактирования.')

    payload.product = order_mngr.get_product_code(session, order_id)
    request_product(session, vk_context, client_context, payload)

def cancel_order(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    order_id:int = payload.order

    order = session.query(Order).get(order_id)
    if order is None:
        return

    if not order_mngr.check_status(session, order_id, OrderStatus.DURING, OrderStatus.COMPLETED):
        ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Отмена невозможна. Услуга оказана ранее.')
        return

    order_mngr.mark_as_rejected(session, order_id)

    ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, f'Заказ №{order_id} отменен')

def order_executed(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    order_id:int = payload.order

    if not order_mngr.check_status(session, order_id, OrderStatus.DURING):
        return

    if not order_mngr.mark_as_completed(session, order_id):
        return

    if vk_context is None: # For test only !!!
        return

    if payload.event:
        ui_mngr.show_snackbar_notice(session, vk_context, client_context, payload.event, 'Благодарим Вас за использование нашего сервиса!')
    
    ui_mngr.show_main_menu(session, vk_context, client_context)