from collections import namedtuple
from multiprocessing import JoinableQueue
import logging

from sqlalchemy.orm.session import Session as OrmSession
from exanho.orm.domain import Sessional

from ..dto import util as dto_util
from ..dto.method_call import VkMethodCall
from ..dto.messages import *
from .vk_api_context import VkApiContext
from .client_context import ClientContext

from exanho.purchbot.model import ProductKind, Product, VkProductContent, Tariff, AddInfoCode, AddInfoSettings
from exanho.purchbot.vk.ui import PayloadCommand, Payload, ProductList, MainMenu, UIElementBuilder
from exanho.core.common import Error

log = logging.getLogger(__name__)

NUMBER_ELEMENTS_PER_PAGE = 10

VkMenuPagination = namedtuple('VkMenuPagination', 'first prev page next last context')

def show_main_menu(vk_context:VkApiContext, client_context:ClientContext, menu_message:str='Меню (см. клавиатуру под строкой ввода)', pagination:VkMenuPagination=None):    

    ui_menu = MainMenu()
    ui_menu.set_label_for_balance(client_context.free_balance, client_context.promo_balance)

    if pagination:
        ui_menu.set_payload_for_first_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                context = pagination.context,
                page = pagination.first)
        )

        ui_menu.set_payload_for_prev_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                context = pagination.context,
                page = pagination.prev)
        )

        ui_menu.set_label_for_page_btn('{}/{}'.format(pagination.page, pagination.last))

        ui_menu.set_payload_for_next_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                context = pagination.context,
                page = pagination.next)
        )

        ui_menu.set_payload_for_last_btn(
            Payload(
                command = PayloadCommand.go_to_page,
                context = pagination.context,
                page = pagination.last)
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

def get_command_by_product_kind(product_kind:ProductKind) -> PayloadCommand:
    if product_kind == ProductKind.QUERY:
        return PayloadCommand.menu_section_queries
    if product_kind == ProductKind.SUBSCRIPTION:
        return PayloadCommand.menu_section_subscriptions
    if product_kind == ProductKind.REPORT:
        return PayloadCommand.menu_section_reports
    raise Error(f'Unknown product kind: {product_kind}')

def show_products_by_kind(vk_context:VkApiContext, client_context:ClientContext, product_kind:ProductKind, payload:Payload):
    page:int = payload.page if payload.page else 1

    ui_product_list = ProductList()
    pagination = None

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)

        command = get_command_by_product_kind(product_kind)
        product_count = session.query(Product).filter(Product.kind == product_kind).count()

        if True:#product_count > NUMBER_ELEMENTS_PER_PAGE:
            last = product_count // NUMBER_ELEMENTS_PER_PAGE if product_count % NUMBER_ELEMENTS_PER_PAGE == 0 else (product_count // NUMBER_ELEMENTS_PER_PAGE) + 1
            pagination = VkMenuPagination(
                first=1,
                prev=page-1 if page>1 else 1,
                page=page,
                next=page+1 if page<last else last,
                last=last,
                context=command.name
            )

        product_number = 0
        for name, code, desc, btn_label, tariff in session.query(Product.name, Product.code, VkProductContent.list_desc, VkProductContent.list_button, Tariff.value).\
            join(VkProductContent, Product.id==VkProductContent.product_id).\
                join(Tariff).\
                    filter(Product.kind == product_kind).\
                        order_by(Product.id).limit(NUMBER_ELEMENTS_PER_PAGE).offset((page-1)*NUMBER_ELEMENTS_PER_PAGE):

            product_number += 1
            product_name = '{}. {} ({:.0f}р)'.format(((page-1)*NUMBER_ELEMENTS_PER_PAGE)+product_number, name, tariff)

            payload = Payload(command = PayloadCommand.request_product, context=code)
            ui_product_list.add_product(product_name, desc, btn_label, payload)


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
        show_main_menu(vk_context, client_context, menu_message='Для выбора нажмите соответствующую кнопку', pagination=pagination)

def show_detailing_product(vk_context:VkApiContext, client_context:ClientContext, trade_id:int, add_info_code:AddInfoCode):

    message = 'Уточнение'

    ui_menu = MainMenu()
    ui_menu.set_label_for_balance(client_context.free_balance, client_context.promo_balance)
    builder = UIElementBuilder()
    builder.build_ui_element(ui_menu.content)

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)
        message = session.query(AddInfoSettings.ui_prompt).filter(AddInfoSettings.code == add_info_code).scalar()

    payload = Payload(command = PayloadCommand.detailing_product, context=trade_id, page=add_info_code.value)

    send_options = SendOptions(
        user_id=client_context.vk_user_id,
        random_id=0,
        keyboard=builder.form(),
        group_id=vk_context.group_id,
        message=message,
        payload=payload.form()
    )

    call_queue:JoinableQueue = vk_context.call_queue
    call_queue.put(
        VkMethodCall(
            'messages',
            'send',
            dto_util.form(send_options, SendOptions)
        )
    )

def show_confirmation_product(vk_context:VkApiContext, client_context:ClientContext, trade_id:int):
    pass