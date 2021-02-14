from collections import namedtuple
import logging

from exanho.purchbot.model.common.product import Product, ProductKind
from exanho.purchbot.vk.ui.elements.product_list import ProductList
from exanho.purchbot.vk.ui.payload import Payload, PayloadCommand
from exanho.purchbot.vk.ui.element_builder import UIElementBuilder
from exanho.purchbot.vk.ui.elements.main_menu import MainMenu
from exanho.core.common import Error

from sqlalchemy.orm.session import Session as OrmSession
from exanho.orm.domain import Sessional

from .vk_api_context import VkApiContext
from .client_context import ClientContext
from .. import VkApiSession

log = logging.getLogger(__name__)

NUMBER_ELEMENTS_PER_PAGE = 10

VkMenuPagination = namedtuple('VkMenuPagination', 'first prev page next last context')

def show_main_menu(vk_context:VkApiContext, client_context:ClientContext, menu_message:str='Меню (см. клавиатуру под строкой ввода)', pagination:VkMenuPagination=None):    

    vk_api_session:VkApiSession = vk_context.vk_api_session

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

    resp = vk_api_session.messages_send(
        user_id=client_context.vk_user_id,
        random_id=0,
        keyboard=builder.form(),
        group_id=vk_context.group_id,
        message=menu_message
        )

    if resp.error:
        raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')

def show_query_products(vk_context:VkApiContext, client_context:ClientContext, payload:Payload, page:int=1):
    assert page>0

    ui_product_list = ProductList()
    pagination = None

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)

        product_count = session.query(Product).filter(Product.kind == ProductKind.QUERY).count()

        if True:#product_count > NUMBER_ELEMENTS_PER_PAGE:
            last = product_count // NUMBER_ELEMENTS_PER_PAGE if product_count % NUMBER_ELEMENTS_PER_PAGE == 0 else (product_count // NUMBER_ELEMENTS_PER_PAGE) + 1
            pagination = VkMenuPagination(
                first=1,
                prev=page-1 if page>1 else 1,
                page=page,
                next=page+1 if page<last else last,
                last=last,
                context=PayloadCommand.menu_section_queries.name
            )

        product_number = 0
        for name, code in session.query(Product.name, Product.code).filter(Product.kind == ProductKind.QUERY).\
            order_by(Product.id).limit(NUMBER_ELEMENTS_PER_PAGE).offset((page-1)*NUMBER_ELEMENTS_PER_PAGE):

            product_number += 1
            product_name = '{}. {}'.format(((page-1)*NUMBER_ELEMENTS_PER_PAGE)+product_number, name)

            payload = Payload(command = PayloadCommand.request_product, context=code)
            ui_product_list.add_product(product_name, 'Потребуется указать ИНН и КПП (при наличии) участника', 'Запросить', payload)


    builder = UIElementBuilder()
    builder.build_ui_element(ui_product_list.content)

    log.debug(builder.form())

    vk_api_session:VkApiSession = vk_context.vk_api_session
    resp = vk_api_session.messages_send(
        user_id=client_context.vk_user_id,
        random_id=0,
        template=builder.form(),
        group_id=vk_context.group_id,
        message='Запросы:'
        )

    if resp.error:
        raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')

    if pagination:
        show_main_menu(vk_context, client_context, menu_message='Для выбора запроса нажмите соответствующую кнопку "Запросить"')

def show_subscription_products(vk_context:VkApiContext, client_context:ClientContext, payload:Payload, page:int=1):
    assert page>0

    ui_product_list = ProductList()
    pagination = None

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)

        product_count = session.query(Product).filter(Product.kind == ProductKind.SUBSCRIPTION).count()

        if True:#product_count > NUMBER_ELEMENTS_PER_PAGE:
            last = product_count // NUMBER_ELEMENTS_PER_PAGE if product_count % NUMBER_ELEMENTS_PER_PAGE == 0 else (product_count // NUMBER_ELEMENTS_PER_PAGE) + 1
            pagination = VkMenuPagination(
                first=1,
                prev=page-1 if page>1 else 1,
                page=page,
                next=page+1 if page<last else last,
                last=last,
                context=PayloadCommand.menu_section_queries.name
            )

        product_number = 0
        for name, code in session.query(Product.name, Product.code).filter(Product.kind == ProductKind.SUBSCRIPTION).\
            order_by(Product.id).limit(NUMBER_ELEMENTS_PER_PAGE).offset((page-1)*NUMBER_ELEMENTS_PER_PAGE):

            product_number += 1
            product_name = '{}. {}'.format(((page-1)*NUMBER_ELEMENTS_PER_PAGE)+product_number, name)

            payload = Payload(command = PayloadCommand.request_product, context=code)
            ui_product_list.add_product(product_name, 'Потребуется указать ИНН и КПП (при наличии) участника', 'Подписаться', payload)


    builder = UIElementBuilder()
    builder.build_ui_element(ui_product_list.content)

    log.debug(builder.form())

    vk_api_session:VkApiSession = vk_context.vk_api_session
    resp = vk_api_session.messages_send(
        user_id=client_context.vk_user_id,
        random_id=0,
        template=builder.form(),
        group_id=vk_context.group_id,
        message='Подписки:'
        )

    if resp.error:
        raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')

    if pagination:
        show_main_menu(vk_context, client_context, menu_message='Для выбора подписки нажмите соответствующую кнопку "Подписаться"')

def show_report_products(vk_context:VkApiContext, client_context:ClientContext, payload:Payload, page:int=1):
    assert page>0

    ui_product_list = ProductList()
    pagination = None

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)

        product_count = session.query(Product).filter(Product.kind == ProductKind.REPORT).count()

        if True:#product_count > NUMBER_ELEMENTS_PER_PAGE:
            last = product_count // NUMBER_ELEMENTS_PER_PAGE if product_count % NUMBER_ELEMENTS_PER_PAGE == 0 else (product_count // NUMBER_ELEMENTS_PER_PAGE) + 1
            pagination = VkMenuPagination(
                first=1,
                prev=page-1 if page>1 else 1,
                page=page,
                next=page+1 if page<last else last,
                last=last,
                context=PayloadCommand.menu_section_queries.name
            )

        product_number = 0
        for name, code in session.query(Product.name, Product.code).filter(Product.kind == ProductKind.REPORT).\
            order_by(Product.id).limit(NUMBER_ELEMENTS_PER_PAGE).offset((page-1)*NUMBER_ELEMENTS_PER_PAGE):

            product_number += 1
            product_name = '{}. {}'.format(((page-1)*NUMBER_ELEMENTS_PER_PAGE)+product_number, name)

            payload = Payload(command = PayloadCommand.request_product, context=code)
            ui_product_list.add_product(product_name, '+ учет незавершенных контрактов', 'Получить', payload)


    builder = UIElementBuilder()
    builder.build_ui_element(ui_product_list.content)

    log.debug(builder.form())

    vk_api_session:VkApiSession = vk_context.vk_api_session
    resp = vk_api_session.messages_send(
        user_id=client_context.vk_user_id,
        random_id=0,
        template=builder.form(),
        group_id=vk_context.group_id,
        message='Отчеты:'
        )

    if resp.error:
        raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')

    if pagination:
        show_main_menu(vk_context, client_context, menu_message='Для выбора отчета нажмите соответствующую кнопку "Получить"')