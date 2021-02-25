from collections import namedtuple
from multiprocessing import JoinableQueue
import logging

from sqlalchemy.orm.session import Session as OrmSession

from exanho.eis44.interfaces import ParticipantInfo, SummaryContractsByStateInfo

from ..dto import util as dto_util
from ..dto.method_call import VkMethodCall
from ..dto.messages import *
from ...utils import eis_service
from .vk_bot_context import VkBotContext
from .client_context import ClientContext

from exanho.purchbot.model import ProductKind, Product, VkDialogContent, Tariff, AddInfoCode, AddInfoSettings, LastTradeDetailing, ProductAddInfo, Trade
from exanho.purchbot.vk.ui import PayloadCommand, Payload, ParticipantList, ProductList, MainMenu, ConfirmTrade, UIElementBuilder
from exanho.core.common import Error

log = logging.getLogger(__name__)

NUMBER_ELEMENTS_PER_PAGE = 10

VkMenuPagination = namedtuple('VkMenuPagination', 'first prev page next last payload')

def show_main_menu(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, menu_message:str='Меню (см. клавиатуру под строкой ввода)', pagination:VkMenuPagination=None):    

    ui_menu = MainMenu()
    ui_menu.set_label_for_balance(client_context.free_balance, client_context.promo_balance)

    if pagination:
        ui_menu.set_payload_for_first_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                product = pagination.payload.product,
                page = pagination.first,
                trade = pagination.payload.trade,
                add_info = pagination.payload.add_info,
                par_number = pagination.payload.par_number,
                par_value = pagination.payload.par_value,
                content = pagination.payload.content,
                go_to = pagination.payload.command)
        )

        ui_menu.set_payload_for_prev_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                page = pagination.prev,
                trade = pagination.payload.trade,
                add_info = pagination.payload.add_info,
                par_number = pagination.payload.par_number,
                par_value = pagination.payload.par_value,
                content = pagination.payload.content,
                go_to = pagination.payload.command)
        )

        ui_menu.set_label_for_page_btn('{}/{}'.format(pagination.page, pagination.last))

        ui_menu.set_payload_for_next_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                page = pagination.next,
                trade = pagination.payload.trade,
                add_info = pagination.payload.add_info,
                par_number = pagination.payload.par_number,
                par_value = pagination.payload.par_value,
                content = pagination.payload.content,
                go_to = pagination.payload.command)
        )

        ui_menu.set_payload_for_last_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                page = pagination.last,
                trade = pagination.payload.trade,
                add_info = pagination.payload.add_info,
                par_number = pagination.payload.par_number,
                par_value = pagination.payload.par_value,
                content = pagination.payload.content,
                go_to = pagination.payload.command)
        )

    builder = UIElementBuilder()
    builder.build_ui_element(ui_menu.content)

    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        keyboard=builder.form(),
        group_id=vk_context.group_id,
        message=menu_message
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )

def get_title_by_product_kind(product_kind:ProductKind) -> str:
    if product_kind == ProductKind.QUERY:
        return 'Запросы:'
    if product_kind == ProductKind.SUBSCRIPTION:
        return 'Подписки:'
    if product_kind == ProductKind.REPORT:
        return 'Отчеты:'
    raise Error(f'Unknown product kind: {product_kind}')

def show_products_by_kind(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, product_kind:ProductKind, payload:Payload):
    page:int = payload.page if payload.page else 1

    ui_product_list = ProductList()
    pagination = None

    product_count = session.query(Product).filter(Product.kind == product_kind).count()

    if product_count > NUMBER_ELEMENTS_PER_PAGE:
        last = product_count // NUMBER_ELEMENTS_PER_PAGE if product_count % NUMBER_ELEMENTS_PER_PAGE == 0 else (product_count // NUMBER_ELEMENTS_PER_PAGE) + 1
        pagination = VkMenuPagination(
            first=1,
            prev=page-1 if page>1 else 1,
            page=page,
            next=page+1 if page<last else last,
            last=last,
            payload=payload
        )

    product_number = 0
    for name, code, tariff in session.query(Product.name, Product.code, Tariff.value).\
        join(Tariff).\
            filter(Product.kind == product_kind).\
                order_by(Product.id).limit(NUMBER_ELEMENTS_PER_PAGE).offset((page-1)*NUMBER_ELEMENTS_PER_PAGE):

        list_desc = session.query(VkDialogContent.content).filter(VkDialogContent.group == code, VkDialogContent.topic == 'list_desc').scalar()
        btn_label = session.query(VkDialogContent.content).filter(VkDialogContent.group == code, VkDialogContent.topic == 'list_button').scalar()

        product_number += 1
        product_name = '{}. {} ({:.0f}р)'.format(((page-1)*NUMBER_ELEMENTS_PER_PAGE)+product_number, name, tariff)

        pr_payload = Payload(command = PayloadCommand.request_product, product=code)
        ui_product_list.add_product(product_name, list_desc, btn_label, pr_payload)


    builder = UIElementBuilder()
    builder.build_ui_element(ui_product_list.content)

    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        template=builder.form(),
        group_id=vk_context.group_id,
        message=get_title_by_product_kind(product_kind)
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )

    if pagination:
        show_main_menu(session, vk_context, client_context, menu_message='Для выбора нажмите соответствующую кнопку', pagination=pagination)

def show_detailing_trade_message(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, trade_id:int, par_number:int):

    message = 'Уточнение'

    # ui_menu = MainMenu()
    # ui_menu.set_label_for_balance(client_context.free_balance, client_context.promo_balance)
    # builder = UIElementBuilder()
    # builder.build_ui_element(ui_menu.content)

    product_id = session.query(Trade).get(trade_id).product_id
    add_info_id = session.query(ProductAddInfo).get((product_id, par_number)).add_info_id
    add_info_code:AddInfoCode = session.query(AddInfoSettings).get(add_info_id).code
    message = session.query(VkDialogContent.content).filter(VkDialogContent.group == AddInfoCode.__name__, VkDialogContent.topic == add_info_code.name).scalar()

    last_trade_detail = session.query(LastTradeDetailing).\
        filter(LastTradeDetailing.client_id == client_context.client_id).\
            one_or_none()

    if last_trade_detail is None:
        last_trade_detail = LastTradeDetailing(
            client_id = client_context.client_id,
            trade_id = trade_id,
            par_number = par_number,
            add_info = add_info_code,
            handled = False
        )
        session.add(last_trade_detail)
    else:
        last_trade_detail.trade_id = trade_id
        last_trade_detail.par_number = par_number
        last_trade_detail.add_info = add_info_code
        last_trade_detail.handled = False
        

    # payload = Payload(command = PayloadCommand.detailing_product, context=trade_id, page=add_info_code.value)

    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        # keyboard=builder.form(),
        group_id=vk_context.group_id,
        message=message
        # payload=payload.form()
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )

def detailing_trade_by_participant(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, inn:str, kpp:str):
    page:int = payload.page if payload.page else 1
    
    result = None
    try:
        result = eis_service.get_participant_list(vk_context.participant_service,inn, kpp, page, NUMBER_ELEMENTS_PER_PAGE)
        if isinstance(result, Error):
            raise result
    except Error as er:
        log.error(f'participant_service: "{er.message}" method call error')
        show_main_menu(session, vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        return
    except Exception as ex:
        log.exception(f'participant_service: "get_participant_list" method call error', ex.args)
        show_main_menu(session, vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        return

    participants, participant_count = result

    ui_participant_list = ParticipantList()
    pagination = None

    if participant_count > NUMBER_ELEMENTS_PER_PAGE:
        last = participant_count // NUMBER_ELEMENTS_PER_PAGE if participant_count % NUMBER_ELEMENTS_PER_PAGE == 0 else (participant_count // NUMBER_ELEMENTS_PER_PAGE) + 1
        pagination = VkMenuPagination(
            first=1,
            prev=page-1 if page>1 else 1,
            page=page,
            next=page+1 if page<last else last,
            last=last,
            payload=payload
        )

    participant_number = 0
    for participant in participants:
        assert isinstance(participant, ParticipantInfo)

        participant_number += 1

        list_desc = 'ИНН: {}\nКПП: {}'.format(participant.inn, participant.kpp) if participant.kpp else 'ИНН: {}'.format(participant.inn)
        btn_label = 'Выбрать'
        participant_name = '{}. {}'.format(((page-1)*NUMBER_ELEMENTS_PER_PAGE)+participant_number, participant.name)

        part_payload = Payload(
            command = PayloadCommand.selection_add_info,
            trade=payload.trade,
            add_info=payload.add_info,
            par_number=payload.par_number,
            par_value=participant.id,
            content='{} {}'.format(participant.inn, participant.kpp) if participant.kpp else participant.inn
        )
        ui_participant_list.add_participant(participant_name, list_desc, btn_label, part_payload)


    builder = UIElementBuilder()
    builder.build_ui_element(ui_participant_list.content)

    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        template=builder.form(),
        group_id=vk_context.group_id,
        message='По Вашему критерию подходят:'
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )

    if pagination:
        show_main_menu(session, vk_context, client_context, menu_message='Для выбора нажмите соответствующую кнопку', pagination=pagination)

def show_confirmation_trade(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, trade_id:int):
    message = get_message_for_confirm(session, vk_context, client_context, trade_id)

    ui_confirm_trade = ConfirmTrade()
    ui_confirm_trade.set_trade(trade_id)

    builder = UIElementBuilder()
    builder.build_ui_element(ui_confirm_trade.content)

    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        keyboard=builder.form(),
        group_id=vk_context.group_id,
        message=message
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )

def get_message_for_confirm(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, trade_id:int) -> str:
    message = 'Подтвердите заказ:'
    
    trade = session.query(Trade).get(trade_id)
    product = session.query(Product).get(trade.product_id)
    act:str = session.query(VkDialogContent.content).filter(VkDialogContent.group == product.code, VkDialogContent.topic == 'list_button').scalar()
    if product.kind == ProductKind.REPORT:
        message += f'\n{act.lower()} отчет "{product.name}"'
    else:
        message += f'\n{act.lower()} "{product.name}"'

    if product.code in ('QUE_PAR_ACT', 'QUE_PAR_HIS', 'REP_PAR_ACT', 'REP_PAR_HIS', 'SUB_PAR'):
        message += get_participant_info_for_confirm(vk_context, client_context, int(trade.parameter1))
    elif product.code == 'REP_PARS_CON':
        pass
    else:
        pass

    tariff = session.query(Tariff.value).filter(Tariff.product_id == trade.product_id).scalar()
    message += f'\nБудет списано {tariff:.0f}р'

    return message

def get_participant_info_for_confirm(vk_context:VkBotContext, client_context:ClientContext, participant_id:int) -> str:
    
    participant = None
    try:
        resp = eis_service.get_participant(vk_context.participant_service, participant_id)
        if isinstance(resp, Error):
            raise participant
        participant:ParticipantInfo = resp
    except Error as er:
        log.error(f'participant_service.get_participant: {er.message}')
        show_main_menu(vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        return
    except Exception as ex:
        log.exception('participant_service.get_participant: method call error', ex.args)
        show_main_menu(vk_context, client_context, 'Удаленный сервер не ответил, попробуйте позже. Приносим свои извинения (:')
        return

    if participant.kpp:
        return f'\n{participant.name}\nИНН: {participant.inn}\nКПП: {participant.kpp}'
    else:
        return f'\n{participant.name}\nИНН: {participant.inn}'

def show_que_par_act_result(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, result:list):
    answer = 'Статус Кол-во Сумма'

    for summary_by_state in result:
        assert isinstance(summary_by_state, SummaryContractsByStateInfo)

        answer += f'\n{summary_by_state.state} {summary_by_state.count} {summary_by_state.sum} {summary_by_state.currency}'
    
    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        group_id=vk_context.group_id,
        message=answer,
        payload = payload.form()
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )