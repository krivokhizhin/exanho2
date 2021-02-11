from exanho.purchbot.vk.ui.element_builder import UIElementBuilder
from exanho.purchbot.vk.ui.elements.main_menu import MainMenu
from exanho.core.common import Error

from .vk_api_context import VkApiContext
from .client_context import ClientContext
from .. import VkApiSession

def show_main_menu(vk_context:VkApiContext, client_context:ClientContext):    

    vk_api_session:VkApiSession = vk_context.vk_api_session

    menu = MainMenu()
    menu.set_label_for_balance(client_context.free_balance, client_context.promo_balance)

    builder = UIElementBuilder()
    builder.build_ui_element(menu.content)

    resp = vk_api_session.messages_send(
        user_id=client_context.vk_user_id,
        random_id=0,
        keyboard=builder.form(),
        group_id=vk_context.group_id,
        message='Меню (см. клавиатуру под строкой ввода)'
        )

    if resp.error:
        raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')
