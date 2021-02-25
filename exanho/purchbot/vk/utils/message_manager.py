import logging
import re
from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error

from .vk_bot_context import VkBotContext
from .client_context import ClientContext
from ..dto import util, JSONObject
from ..ui import PayloadCommand, Payload

from ...utils import account_manager as acc_mngr
from ...utils import get_account
from ...utils import eis_service
from ..utils import ui_manager as ui_mngr

from ...model import ProductKind, Product, Client, VkUser, Tariff, TradeStatus, Trade, ProductAddInfo, AddInfoCode, LastTradeDetailing

log = logging.getLogger(__name__)

def handle_message_new(session:OrmSession, context:VkBotContext, message_new:JSONObject):

    if hasattr(message_new, 'message'):

        client_context = get_client_context(session, message_new.message.from_id)

        if not hasattr(message_new.message, 'payload'):
            
            if client_context.payload:
                match_payload(session, client_context.payload, client_context, context, message_new)
            else:
                ui_mngr.show_main_menu(session, context, client_context)
            return

        payload_obj = message_new.message.payload
        if isinstance(payload_obj, str):
            payload_obj = util.convert_json_str_to_obj(payload_obj.replace('\\"', '"').replace('\"', '"'), JSONObject)
        
        if not hasattr(payload_obj, 'command'):
            ui_mngr.show_main_menu(session, context, client_context)
            return

        payload = Payload()
        payload.fill(
                payload_obj.command,
                product = payload_obj.product if hasattr(payload_obj, 'product') else None,
                page = int(payload_obj.page) if hasattr(payload_obj, 'page') else None,
                trade = int(payload_obj.trade) if hasattr(payload_obj, 'trade') else None,
                add_info = payload_obj.add_info if hasattr(payload_obj, 'add_info') else None,
                par_number = int(payload_obj.par_number) if hasattr(payload_obj, 'par_number') else None,
                par_value = payload_obj.par_value if hasattr(payload_obj, 'par_value') else None,
                go_to = payload_obj.go_to if hasattr(payload_obj, 'go_to') else None
            )

        match_payload(session, payload, client_context, context, message_new)

    else:
        raise Error('There is not "message" element in "message_new" event')

def handle_message_event(session:OrmSession, context:VkBotContext, message_event:JSONObject):  

    if hasattr(message_event, 'payload'):

        client_context = get_client_context(session, message_event.user_id)

        payload_obj = message_event.payload
        if isinstance(payload_obj, str):
            payload_obj = util.convert_json_str_to_obj(payload_obj.replace('\\"', '"').replace('\"', '"'), JSONObject)
        
        if not hasattr(payload_obj, 'command'):
            ui_mngr.show_main_menu(session, context, client_context)
            return

        payload = Payload()
        payload.fill(
                payload_obj.command,
                product = payload_obj.product if hasattr(payload_obj, 'product') else None,
                page = int(payload_obj.page) if hasattr(payload_obj, 'page') else None,
                trade = int(payload_obj.trade) if hasattr(payload_obj, 'trade') else None,
                add_info = payload_obj.add_info if hasattr(payload_obj, 'add_info') else None,
                par_number = int(payload_obj.par_number) if hasattr(payload_obj, 'par_number') else None,
                par_value = payload_obj.par_value if hasattr(payload_obj, 'par_value') else None,
                go_to = payload_obj.go_to if hasattr(payload_obj, 'go_to') else None
            )

        match_payload(session, payload, client_context, context, message_event)

    else:
        raise Error('There is not "payload" element in "message_event" event')

def handle_message_reply(session:OrmSession, context:VkBotContext, message_reply:JSONObject):

    if hasattr(message_reply, 'payload'):

        client_context = get_client_context(session, message_reply.peer_id)

        payload_obj = message_reply.payload
        if isinstance(payload_obj, str):
            payload_obj = util.convert_json_str_to_obj(payload_obj.replace('\\"', '"').replace('\"', '"'), JSONObject)
        
        if not hasattr(payload_obj, 'command'):
            return

        payload = Payload()
        payload.fill(
                payload_obj.command,
                product = payload_obj.product if hasattr(payload_obj, 'product') else None,
                page = int(payload_obj.page) if hasattr(payload_obj, 'page') else None,
                trade = int(payload_obj.trade) if hasattr(payload_obj, 'trade') else None,
                add_info = payload_obj.add_info if hasattr(payload_obj, 'add_info') else None,
                par_number = int(payload_obj.par_number) if hasattr(payload_obj, 'par_number') else None,
                par_value = payload_obj.par_value if hasattr(payload_obj, 'par_value') else None,
                go_to = payload_obj.go_to if hasattr(payload_obj, 'go_to') else None
            )

        match_payload(session, payload, client_context, context, message_reply)

def match_payload(session:OrmSession, payload:Payload, client_context:ClientContext, context:VkBotContext, event_obj:JSONObject):
    if payload is None or payload.command is None or payload.command == PayloadCommand.start or payload.command == PayloadCommand.empty:
        ui_mngr.show_main_menu(session, context, client_context)
        return

    if payload.command == PayloadCommand.get_balance:
        log.debug(f'VK user (id={client_context.vk_user_id}) pressed {PayloadCommand.get_balance.name.upper()}')
    elif payload.command == PayloadCommand.go_to_page:
        go_to(session, payload, client_context, context, event_obj)
    elif payload.command == PayloadCommand.request_product:
        request_product(session, context, client_context, payload.product)
    elif payload.command == PayloadCommand.detailing_trade:
        detailing_trade(session, context, client_context, payload, event_obj)
    elif payload.command == PayloadCommand.selection_add_info:
        selection_add_info(session, context, client_context, payload)
    elif payload.command == PayloadCommand.confirm_trade:
        confirm_trade(session, context, client_context, payload)
    elif payload.command == PayloadCommand.edit_trade:
        edit_trade(session, context, client_context, payload)
    elif payload.command == PayloadCommand.cancel_trade:
        cancel_trade(session, context, client_context, payload)
    elif payload.command == PayloadCommand.trade_executed:
        trade_execute(session, context, client_context, payload)
    elif payload.command == PayloadCommand.menu_section_queries:
        ui_mngr.show_products_by_kind(session, context, client_context, ProductKind.QUERY, payload)
    elif payload.command == PayloadCommand.menu_section_subscriptions:
        ui_mngr.show_products_by_kind(session, context, client_context, ProductKind.SUBSCRIPTION, payload)
    elif payload.command == PayloadCommand.menu_section_reports:
        ui_mngr.show_products_by_kind(session, context, client_context, ProductKind.REPORT, payload)
    elif payload.command == PayloadCommand.menu_section_my_subscriptions:
        log.debug(f'VK user (id={client_context.vk_user_id}) pressed {PayloadCommand.menu_section_my_subscriptions.name.upper()}')
    elif payload.command == PayloadCommand.menu_section_history:
        log.debug(f'VK user (id={client_context.vk_user_id}) pressed {PayloadCommand.menu_section_history.name.upper()}')
    else:
        ui_mngr.show_main_menu(session, context, client_context)

def get_client_context(session:OrmSession, user_id:int) -> ClientContext:

    vk_user = session.query(VkUser).filter(VkUser.user_id == user_id).one_or_none()

    if vk_user is None:
        client = Client()
        vk_user = VkUser(user_id = user_id)
        vk_user.client = client
        session.add_all([client, vk_user])
        session.flush()

        promo(session, client.id)

    free_balance = acc_mngr.get_free_balance(session, vk_user.client.id)
    promo_balance = acc_mngr.get_promo_balance(session, vk_user.client.id)

    payload = None
    last_trade_detail = session.query(LastTradeDetailing).filter(LastTradeDetailing.client_id == vk_user.client.id).\
        filter(LastTradeDetailing.handled == False).one_or_none()
    if last_trade_detail:
        payload = Payload(
            command = PayloadCommand.detailing_trade,
            page = 1,
            trade = last_trade_detail.trade_id,
            par_number = last_trade_detail.par_number,
            add_info = last_trade_detail.add_info.value
        )

    return ClientContext(client_id=vk_user.client.id, vk_user_id=user_id, payload=payload, free_balance=free_balance, promo_balance=promo_balance)        

def promo(session:OrmSession, client_id:int):
    PROMO_AMOUNT = Decimal('999.00')
    promo_remain = acc_mngr.get_promo_balance(session, client_id)

    if promo_remain > 0:
        return

    acc_mngr.deposit_promo_funds(session, client_id, PROMO_AMOUNT)

def go_to(session:OrmSession, payload:Payload, client_context:ClientContext, context:VkBotContext, event_obj:JSONObject):
    try:
        payload.command = PayloadCommand[payload.go_to]
    except:
        return

    match_payload(session, payload, client_context, context, event_obj)

def request_product(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, product_code:str):
    trade_id = None
    par_number = None

    product = session.query(Product).filter(Product.code == product_code).one_or_none()
    if product is None:
        return

    amount = session.query(Tariff.value).filter(Tariff.product == product).scalar()

    trade = session.query(Trade).\
        filter(Trade.client_id == client_context.client_id, Trade.product_id == product.id, Trade.status.in_([TradeStatus.NEW, TradeStatus.FILLING])).\
            first()
    if trade:
        trade.amount = amount
    else:
        trade = Trade(
            status = TradeStatus.NEW,
            client_id = client_context.client_id,
            product_id = product.id,
            amount = amount,
            paid = False
        )
        session.add(trade)
        session.flush()

    trade_id = trade.id

    parameters = [p.par_number for p in session.query(ProductAddInfo).filter(ProductAddInfo.product_id == product.id)]

    if trade.parameter1 is None and 1 in parameters:
        par_number = 1
    elif trade.parameter2 is None and 2 in parameters:
        par_number = 2
    elif trade.parameter3 is None and 3 in parameters:
        par_number = 3
    else:
        par_number = None

    if par_number is None:
        trade.status = TradeStatus.FILLING

    if par_number:
        ui_mngr.show_detailing_trade_message(session, vk_context, client_context, trade_id, par_number)
    else:
        ui_mngr.show_confirmation_trade(session, vk_context, client_context, trade_id)

def detailing_trade(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, event_obj:JSONObject):
    text = None
    if hasattr(event_obj, 'message') and hasattr(event_obj.message, 'text'):
        text = event_obj.message.text
    if payload.par_value:
        text = payload.par_value

    if text is None:
        return

    if payload.add_info is None:
        return

    if payload.add_info == AddInfoCode.PARTICIPANT.value:
        inn, kpp = extract_inn_kpp_from_text(text)
        if inn is None:
            return
        payload.par_value = '{} {}'.format(inn, kpp) if kpp else inn
        ui_mngr.detailing_trade_by_participant(session, vk_context, client_context, payload, inn, kpp)
    elif payload.add_info == AddInfoCode.CUSTOMER.value:
        pass
    elif payload.add_info == AddInfoCode.NOTIFICATION.value:
        pass
    elif payload.add_info == AddInfoCode.CONTRACT.value:
        pass
    else:
        return

def extract_inn_kpp_from_text(text:str):
    pattern = r'(?P<inn>\d{10}|\d{12})(?:\D+(?P<kpp>\d{9}))?'
    match = re.search(pattern, text)

    if match:
        return match.group('inn'), match.group('kpp')
    else:
        return None, None

def selection_add_info(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    trade_id:int = payload.trade
    par_number:int = payload.par_number
    par_value:int = payload.par_value

    trade = session.query(Trade).get(trade_id)
    if trade is None:
        return

    if par_number == 1:
        trade.parameter1 = str(par_value)
    elif par_number == 2:
        trade.parameter2 = str(par_value)
    elif par_number == 3:
        trade.parameter3 = str(par_value)
    else:
        par_number = None

    parameters = [p.par_number for p in session.query(ProductAddInfo).filter(ProductAddInfo.product_id == trade.product_id)]

    if trade.parameter1 is None and 1 in parameters:
        par_number = 1
    elif trade.parameter2 is None and 2 in parameters:
        par_number = 2
    elif trade.parameter3 is None and 3 in parameters:
        par_number = 3
    else:
        par_number = None

    if par_number is None:
        trade.status = TradeStatus.FILLING

    if par_number:
        ui_mngr.show_detailing_trade_message(session, vk_context, client_context, trade_id, par_number)
    else:
        ui_mngr.show_confirmation_trade(session, vk_context, client_context, trade_id)

def confirm_trade(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    trade_id:int = payload.trade

    trade = session.query(Trade).get(trade_id)
    if trade is None:
        return

    promo_balance = acc_mngr.get_promo_balance(session, client_context.client_id)
    free_balance = acc_mngr.get_free_balance(session, client_context.client_id)
    if promo_balance >= trade.amount:
        acc_mngr.make_payment(
            session,
            get_account.for_client_promo_payment(session, client_context.client_id, trade_id),
            get_account.promo_by_client(session, client_context.client_id),
            trade.amount
        )
    elif promo_balance > 0 and free_balance >= trade.amount - promo_balance:
        acc_mngr.make_payment(
            session,
            get_account.for_client_promo_payment(session, client_context.client_id, trade_id),
            get_account.promo_by_client(session, client_context.client_id),
            promo_balance
        )
        acc_mngr.make_payment(
            session,
            get_account.for_client_payment(session, client_context.client_id, trade_id),
            get_account.free_balance_by_client(session, client_context.client_id),
            trade.amount - promo_balance
        )
    elif free_balance >= trade.amount:
        acc_mngr.make_payment(
            session,
            get_account.for_client_payment(session, client_context.client_id, trade_id),
            get_account.free_balance_by_client(session, client_context.client_id),
            trade.amount
        )
    else:
        ui_mngr.show_main_menu(session, vk_context, client_context, 'Недостаточно средств! Пополните, пожалуйста, баланс.')
        return

    trade.paid = True
    trade.status = TradeStatus.CONFIRMED

    execute_trade(session, vk_context, client_context, payload, trade_id)
    trade.status = TradeStatus.DURING

def execute_trade(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, trade_id:int):
    trade = session.query(Trade).get(trade_id)
    product_code = session.query(Product.code).filter(Product.id == trade.product_id).scalar()

    result = None
    ui_method = None

    try:

        if product_code == 'QUE_PAR_ACT':
            result = eis_service.get_current_participant_activity(vk_context.participant_service, int(trade.parameter1))
            if isinstance(result, Error):
                raise result
            ui_method = ui_mngr.show_que_par_act_result

        if product_code == 'QUE_PAR_HIS':
            pass

        if product_code == 'SUB_PAR':
            pass

        if product_code == 'REP_PAR_ACT':
            pass

        if product_code == 'REP_PAR_HIS':
            pass

        if product_code == 'REP_PARS_CON':
            pass

    except Error as er:
        log.error(f'eis_service: "{er.message}" method call error')
        ui_mngr.show_main_menu(session, vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        session.rollback()
        return
    except Exception as ex:
        log.exception(f'eis_service: method for trade_id={trade_id} call error', ex.args)
        ui_mngr.show_main_menu(session, vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        session.rollback()
        return

    exec_payload = Payload(
        command = PayloadCommand.trade_executed,
        trade = trade_id
    )
    ui_method(session, vk_context, client_context, exec_payload, result)

def edit_trade(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    trade_id:int = payload.trade
    product_code = None

    trade = session.query(Trade).get(trade_id)
    if trade is None:
        return

    trade.status = TradeStatus.NEW
    trade.parameter1 = None
    trade.parameter2 = None
    trade.parameter3 = None

    product_code = trade.product.code

    request_product(session, vk_context, client_context, product_code)

def cancel_trade(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    trade_id:int = payload.trade

    trade = session.query(Trade).get(trade_id)
    if trade is None:
        return

    trade.status = TradeStatus.REJECTED

    ui_mngr.show_main_menu(session, vk_context, client_context, f'Заказ №{trade_id} отменен')

def trade_execute(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload):
    trade_id:int = payload.trade

    trade = session.query(Trade).get(trade_id)
    if trade is None:
        return

    promo_pay_acc = get_account.for_client_promo_payment(session, client_context.client_id, trade_id)
    promo_pay_acc_amount = acc_mngr.get_remain_amount(session, promo_pay_acc)

    pay_acc = get_account.for_client_payment(session, client_context.client_id, trade_id)
    pay_acc_amount = acc_mngr.get_remain_amount(session, pay_acc)

    if promo_pay_acc_amount >= trade.amount:
        acc_mngr.make_payment(
            session,
            get_account.product_promo_revenue(session, trade_id),
            promo_pay_acc,
            trade.amount
        )
    elif promo_pay_acc_amount > 0 and pay_acc_amount >= trade.amount - promo_pay_acc_amount:
        acc_mngr.make_payment(
            session,
            get_account.product_promo_revenue(session, trade_id),
            promo_pay_acc,
            promo_pay_acc_amount
        )
        acc_mngr.make_payment(
            session,
            get_account.product_revenue(session, trade_id),
            pay_acc,
            trade.amount - promo_pay_acc_amount
        )
    elif pay_acc_amount >= trade.amount:
        acc_mngr.make_payment(
            session,
            get_account.product_revenue(session, trade_id),
            pay_acc,
            trade.amount
        )
    else:
        return

    trade.status = TradeStatus.COMPLETED

    free_balance = acc_mngr.get_free_balance(session, client_context.client_id)
    promo_balance = acc_mngr.get_promo_balance(session, client_context.client_id)

    client_context = client_context._replace(free_balance=free_balance, promo_balance=promo_balance)

    ui_mngr.show_main_menu(session, vk_context, client_context, 'Благодарим Вас за использование нашего сервиса!')
