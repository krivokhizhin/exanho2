import csv
from datetime import datetime
import io
import logging
from collections import defaultdict, namedtuple
from decimal import Decimal
from multiprocessing import JoinableQueue, shared_memory

from sqlalchemy.orm.session import Session as OrmSession

from exanho.eis44.interfaces import ParticipantInfo, ParticipantCurrentActivityInfo, ParticipantExperienceInfo, ContractInfo, ParticipantEventInfo

from ...utils import json64 as json_util
from ..dto.method_call import VkMethodCall
from ..dto.messages import *
from ..dto.attachments import *
from ...utils import eis_service
from .vk_bot_context import VkBotContext
from .client_context import ClientContext
from ...utils import order_manager as order_mngr

from exanho.purchbot.model import ProductKind, Product, VkDialogContent, Tariff, AddInfoCode, Order
from exanho.purchbot.vk.ui import PayloadCommand, Payload, ParticipantList, ProductList, MainMenu, ConfirmOrder, UIElementBuilder, SnackbarNotice, ParticipantEvent
from exanho.core.common import Error

log = logging.getLogger(__name__)

csv.register_dialect('vk_excel', delimiter=';', quoting=csv.QUOTE_MINIMAL)

NUMBER_ELEMENTS_PER_PAGE = 10
CSV_ENCODING = '1251'

VkMenuPagination = namedtuple('VkMenuPagination', 'first prev page next last payload')

def show_main_menu(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, menu_message:str='\ud83d\ude0e', pagination:VkMenuPagination=None):    

    ui_menu = MainMenu()
    ui_menu.set_label_for_balance(client_context.free_balance, client_context.promo_balance)

    if pagination:
        ui_menu.set_payload_for_first_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                product = pagination.payload.product,
                page = pagination.first,
                order = pagination.payload.order,
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
                order = pagination.payload.order,
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
                order = pagination.payload.order,
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
                order = pagination.payload.order,
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
            json_util.form(send_options, SendOptions)
        )
    )

def show_snackbar_notice(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, event_id:str, text:str='OK'):
    if event_id:

        ui_snackbar = SnackbarNotice()
        ui_snackbar.set_text(text)

        builder = UIElementBuilder()
        builder.build_ui_element(ui_snackbar.content)

        send_options = SendMessageEventAnswerOptions(
            event_id = event_id,
            user_id=client_context.vk_user_id,
            peer_id=client_context.vk_user_id,
            event_data=builder.form()
        )

        log.debug(f'{event_id}: {send_options.event_data}')

        call_queue:JoinableQueue = vk_context.call_queue
        call_queue.put(
            VkMethodCall(
                'messages',
                'sendMessageEventAnswer',
                json_util.form(send_options, SendMessageEventAnswerOptions)
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
        message='Для выбора нажмите соответствующую кнопку' #get_title_by_product_kind(product_kind)
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            json_util.form(send_options, SendOptions)
        )
    )

    show_main_menu(session, vk_context, client_context, menu_message='?', pagination=pagination)

def show_detailing_order_message(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, order_id:int, par_number:int):

    add_info_code = order_mngr.get_add_info_code(session, order_id, par_number)
    message = session.query(VkDialogContent.content).filter(VkDialogContent.group == AddInfoCode.__name__, VkDialogContent.topic == add_info_code.name).scalar()

    order_mngr.update_last_order_detailing(session, client_context.client_id, order_id, par_number, add_info_code)

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
            json_util.form(send_options, SendOptions)
        )
    )

def detailing_order_by_participant(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, inn:str, kpp:str):
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

    if participant_count == 0:

        send_options = SendOptions(
            user_id=client_context.vk_user_id,
            random_id=0,
            group_id=vk_context.group_id,
            message='По Вашим критериям участник не найден. Проверьте корректность введенных данных.'
        )

        call_queue:JoinableQueue = vk_context.call_queue
        call_queue.put(
            VkMethodCall(
                'messages',
                'send',
                json_util.form(send_options, SendOptions)
            )
        )
        return

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
            order=payload.order,
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
            json_util.form(send_options, SendOptions)
        )
    )

    if pagination:
        show_main_menu(session, vk_context, client_context, menu_message='Для выбора нажмите соответствующую кнопку', pagination=pagination)

def show_confirmation_order(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, order_id:int):
    message = get_message_for_confirm(session, vk_context, client_context, order_id)

    ui_confirm_order = ConfirmOrder()
    ui_confirm_order.set_order(order_id)

    builder = UIElementBuilder()
    builder.build_ui_element(ui_confirm_order.content)

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
            json_util.form(send_options, SendOptions)
        )
    )

def get_message_for_confirm(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, order_id:int) -> str:
    message = 'Подтвердите заказ:'
    
    order = session.query(Order).get(order_id)
    product = session.query(Product).get(order.product_id)
    act:str = session.query(VkDialogContent.content).filter(VkDialogContent.group == product.code, VkDialogContent.topic == 'list_button').scalar()
    if product.kind == ProductKind.REPORT:
        message += f'\n{act.lower()} отчет "{product.name}"'
    else:
        message += f'\n{act.lower()} "{product.name}"'

    if product.code in ('QUE_PAR_ACT', 'QUE_PAR_HIS', 'REP_PAR_ACT', 'REP_PAR_HIS', 'SUB_PAR'):
        message += get_participant_info_for_confirm(vk_context, client_context, int(order.parameter1))
    elif product.code == 'REP_PARS_CON':
        pass
    else:
        pass

    tariff = session.query(Tariff.value).filter(Tariff.product_id == order.product_id).scalar()
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

def show_que_par_act_result(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, result:ParticipantCurrentActivityInfo):
    answer = 'В данный момент участник:\n'
    if result.cntr_count > 0:
        answer += '- исполняет контракты:\n{} шт., на сумму {} руб.'.format(result.cntr_count, result.cntr_rur_sum)
        if result.cntr_currencies:
            for currency, cur_count, cur_sum in zip(result.cntr_currencies, result.cntr_cur_count, result.cntr_cur_sum):
                answer += ', {} {} ({} шт)'.format(currency, cur_count, cur_sum)
        if result.cntr_right_to_conclude_count > 0:
            answer += ', в т.ч. {} шт. с правом на заключение'.format(result.cntr_right_to_conclude_count)
        if result.cntr_first_start_date:
            answer += ', с {} по {} (план)'.format(result.cntr_first_start_date, result.cntr_last_end_date) if result.cntr_last_end_date else '\nс {}'.format(result.cntr_first_start_date)
    else:
        answer += '- никакие контракты не исполняет'
    
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
            json_util.form(send_options, SendOptions)
        )
    )

def show_rep_par_act_result(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, result:list):
    order_id:int = payload.order
    shm_name = None
    shm_size = None
    filename = f'rep_par_act_{order_id}.csv'

    with io.StringIO() as buffer:
        fieldnames = ['N', 'reg_num', 'state', 'publish_dt', 'subject', 'price', 'currency_code', 'right_to_conclude', 'start_date', 'end_date', 'supplier_number', 'href']
        writer = csv.DictWriter(buffer, fieldnames=fieldnames,  dialect=csv.excel)
        writer.writeheader()

        sort_number = 0

        for exec_cntr in result:
            assert isinstance(exec_cntr, ContractInfo)
            sort_number += 1
            writer.writerow({
                'N': sort_number,
                'reg_num': f'\'{exec_cntr.reg_num}',
                'state': exec_cntr.state,
                'publish_dt': exec_cntr.publish_dt,
                'subject': exec_cntr.subject,
                'price': exec_cntr.price,
                'currency_code': exec_cntr.currency_code,
                'right_to_conclude': exec_cntr.right_to_conclude,
                'start_date': exec_cntr.start_date,
                'end_date': exec_cntr.end_date,
                'supplier_number': exec_cntr.supplier_number,
                'href': exec_cntr.href
            })

        content = buffer.getvalue().encode(encoding='utf-8')
        shm_size = len(content)

        shm_a = shared_memory.SharedMemory(create=True, size=shm_size)
        shm_name = shm_a.name
        shm_a.buf[:shm_size] = content
        shm_a.close()
    
    send_options = SendAttachmentsOptions(
        shm_name = shm_name,
        shm_size = shm_size,
        filename = filename,
        peer_id = client_context.vk_user_id,
        type = 'doc',
        group_id = vk_context.group_id,
        random_id = 0,
        payload = payload.form()
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'attachment',
            'send',
            json_util.form(send_options, SendAttachmentsOptions)
        )
    )

def show_que_par_his_result(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, result:ParticipantExperienceInfo):
    answer = 'Опыт участника:\n'
    answer += '- КОНТРАКТЫ, исполнение'
    if result.cntr_ec_count > 0 or result.cntr_et_count > 0 or result.cntr_in_count > 0:
        if result.cntr_first_start_date:
            answer += ' (с {} по {}):'.format(result.cntr_first_start_date, result.cntr_last_end_date) if result.cntr_last_end_date else '\nс {}'.format(result.cntr_first_start_date)
        else:
            answer += ':'
        if result.cntr_ec_count > 0:
            answer += '\nзавершено: {} шт, на сумму {} руб.'.format(result.cntr_ec_count, result.cntr_ec_rur_sum)
            if result.cntr_ec_cur_count > 0:
                answer += ', в т.ч. в валюте {} шт.'.format(result.cntr_ec_cur_count)
        if result.cntr_et_count > 0:
            answer += '\nпрекращено: {} шт, на сумму {} руб.'.format(result.cntr_et_count, result.cntr_et_rur_sum)
            if result.cntr_ec_cur_count > 0:
                answer += ', в т.ч. в валюте {} шт.'.format(result.cntr_et_cur_count)
        if result.cntr_in_count > 0:
            answer += '\nаннулировано: {} шт, на сумму {} руб.'.format(result.cntr_in_count, result.cntr_in_rur_sum)
            if result.cntr_ec_cur_count > 0:
                answer += ', в т.ч. в валюте {} шт.'.format(result.cntr_in_cur_count)
    else:
        answer += 'отсутствует'
    
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
            json_util.form(send_options, SendOptions)
        )
    )

def show_rep_par_his_result(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, result:list):
    order_id:int = payload.order
    shm_name = None
    shm_size = None
    filename = f'rep_par_his_{order_id}.csv'

    with io.StringIO() as buffer:
        fieldnames = ['N', 'regnum', 'Состояние', 'Опубликовано', 'Предмет', 'Цена', 'Валюта', 'Право на заключение', 'Начало', 'Конец', 'Кол-во поставщиков', 'href']
        writer = csv.DictWriter(buffer, fieldnames=fieldnames, dialect='vk_excel')
        writer.writeheader()

        sort_number = 0

        for exec_cntr in result:
            assert isinstance(exec_cntr, ContractInfo)
            sort_number += 1
            writer.writerow({
                'N': sort_number,
                'regnum': f'\'{exec_cntr.reg_num}',
                'Состояние': exec_cntr.state,
                'Опубликовано': exec_cntr.publish_dt,
                'Предмет': exec_cntr.subject,
                'Цена': exec_cntr.price,
                'Валюта': exec_cntr.currency_code,
                'Право на заключение': exec_cntr.right_to_conclude,
                'Начало': exec_cntr.start_date,
                'Конец': exec_cntr.end_date,
                'Кол-во поставщиков': exec_cntr.supplier_number,
                'href': exec_cntr.href
            })

        content = buffer.getvalue().encode(encoding=CSV_ENCODING)
        shm_size = len(content)

        shm_a = shared_memory.SharedMemory(create=True, size=shm_size)
        shm_name = shm_a.name
        shm_a.buf[:shm_size] = content
        shm_a.close()
    
    send_options = SendAttachmentsOptions(
        shm_name = shm_name,
        shm_size = shm_size,
        filename = filename,
        peer_id = client_context.vk_user_id,
        type = 'doc',
        group_id = vk_context.group_id,
        random_id = 0,
        payload = payload.form()
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'attachment',
            'send',
            json_util.form(send_options, SendAttachmentsOptions)
        )
    )

def show_sub_par_subscription(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext, payload:Payload, result:list):
    order_id:int = payload.order
    message = 'Вы подписались на события по участнику:'

    participant_id, _, _ = order_mngr.get_parameters(session, order_id)
    participant_info = get_participant_info_for_confirm(vk_context, client_context, int(participant_id))
    message += participant_info
    
    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        group_id=vk_context.group_id,
        message=message
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            json_util.form(send_options, SendOptions)
        )
    )

    if result:
        event_info:ParticipantEventInfo = result[0]

        ui_participant_event = ParticipantEvent()
        ui_participant_event.fill_event(event_info.href)

        message = 'Последнее событие по участнику:' + participant_info
        message += f'\nДата события:\n{event_info.publish_dt}'
        message += '\nТип события:\n'+event_info.event_name

        builder = UIElementBuilder()
        builder.build_ui_element(ui_participant_event.content)

        send_options = SendOptions(
            user_id=client_context.vk_user_id,
            random_id=0,
            keyboard=builder.form(),
            group_id=vk_context.group_id,
            message=message
        )

        call_queue.put(
            VkMethodCall(
                'messages',
                'send',
                json_util.form(send_options, SendOptions)
            )
        )

def show_history(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext):
    
    shm_name = None
    shm_size = None
    orders = dict()
    tmst = datetime.today().strftime('%Y%m%d%H%M%S')
    filename = f'history_{tmst}.csv'

    with io.StringIO() as buffer:
        fieldnames = ['N', 'ID', 'Дата', 'Продукт', 'Стоимость', 'Контекст']
        writer = csv.DictWriter(buffer, fieldnames=fieldnames, dialect='vk_excel')
        writer.writeheader()

        sort_number = 0

        for order_id, order_updated_at, order_product, order_amount in order_mngr.get_orders_by_client(session, client_context.client_id):
            sort_number += 1
            writer.writerow({
                'N': sort_number,
                'ID': order_id,
                'Дата': order_updated_at,
                'Продукт': order_product,
                'Стоимость': order_amount,
                'Контекст': '<пусто>'
            })

            cnt, sum_amount = orders.get(order_product, (0, 0))
            orders[order_product] = (cnt+1, sum_amount+order_amount)

        content = buffer.getvalue().encode(encoding=CSV_ENCODING)
        shm_size = len(content)

        log.debug(f'{shm_size}: {content}')

        shm_in = shared_memory.SharedMemory(create=True, size=shm_size)
        shm_name = shm_in.name
        shm_in.buf[:shm_size] = content
        shm_in.close()
    
    if orders:

        history_message = '\n'.join([f'- {prdt}: {tot_by_prdt[0]} раз на сумму {tot_by_prdt[1]} р.' for prdt, tot_by_prdt in orders.items()])
        history_message += 'Перечень во вложении'

        send_options = SendOptions(
            user_id=client_context.vk_user_id,
            random_id=0,
            group_id=vk_context.group_id,
            message=history_message
        )

        call_queue:JoinableQueue = vk_context.call_queue
        call_queue.put(
            VkMethodCall(
                'messages',
                'send',
                json_util.form(send_options, SendOptions)
            )
        )

        send_options = SendAttachmentsOptions(
            shm_name = shm_name,
            shm_size = shm_size,
            filename = filename,
            peer_id = client_context.vk_user_id,
            type = 'doc',
            group_id = vk_context.group_id,
            random_id = 0,
            payload = Payload.empty()
        )

        call_queue:JoinableQueue = vk_context.call_queue
        call_queue.put(
            VkMethodCall(
                'attachment',
                'send',
                json_util.form(send_options, SendAttachmentsOptions)
            )
        )

    else:
        shm_out = shared_memory.SharedMemory(shm_name)
        shm_out.close()
        shm_out.unlink()

        send_options = SendOptions(
            user_id=client_context.vk_user_id,
            random_id=0,
            group_id=vk_context.group_id,
            message='Вы пока не воспользовались сервисами'
        )

        call_queue:JoinableQueue = vk_context.call_queue
        call_queue.put(
            VkMethodCall(
                'messages',
                'send',
                json_util.form(send_options, SendOptions)
            )
        )

def show_balance(session:OrmSession, vk_context:VkBotContext, client_context:ClientContext):

    balance_message = 'Свободный остаток на счете: {:.0f} р.'.format(client_context.free_balance)
    if client_context.promo_balance and client_context.promo_balance > 0:
        balance_message += '\nСвободный остаток на промо-счете: {:.0f} р.'.format(client_context.promo_balance)
 
    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        group_id=vk_context.group_id,
        message=balance_message
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            json_util.form(send_options, SendOptions)
        )
    )