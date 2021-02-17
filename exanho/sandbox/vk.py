from multiprocessing import JoinableQueue
from exanho.purchbot.vk.dto import util as dto_util
from exanho.purchbot.vk.dto.method_call import VkMethodCall
from exanho.purchbot.vk.dto.messages.send_options import SendOptions
from exanho.purchbot.vk.ui.payload import Payload, PayloadCommand
from exanho.purchbot.vk.ui.element_builder import UIElementBuilder
from exanho.purchbot.vk import VkApiSession, VkBotSession
from exanho.purchbot.vk.drivers import BuildInDriver
from exanho.purchbot.vk.dto import JSONObject

from exanho.purchbot.vk.ui.element_content import *
from exanho.purchbot.vk.ui.elements import *

ACCESS_TOKEN = '843e477baaa13e3022776a9a5cd7544cfeeda9f3262a5516decbf681f896f008cc9c502eebcd37ca79417'
SEND_ACCESS_TOKEN = 'ece8ae0bd980d4ced850b3be6ad8002792e1bfd614d725232ad3f7d6a6bae91188a50d993813be3d84f71'
GROUP_ID = 202308925
ui_template_path = '/home/kks/git/exanho/exanho/purchbot/vk/ui'

def match_method_call(method_call:VkMethodCall):
    driver = BuildInDriver()
    vk_api_session = VkApiSession(driver, ACCESS_TOKEN)

    vk_api_method_name = method_call.form_vk_api_method_name()

    if hasattr(vk_api_session, vk_api_method_name) and callable(getattr(vk_api_session, vk_api_method_name)):
        vk_api_method = getattr(vk_api_session, vk_api_method_name)
        resp = vk_api_method(method_call.options)
    else:
        print(f'{method_call} | Not supported section and/or method')

def run():
    
    # ui_menu = MainMenu()
    # ui_menu.set_label_for_balance(0, 999)

    # builder = UIElementBuilder()
    # builder.build_ui_element(ui_menu.content)

    # send_options = SendOptions(
    #     user_id=888888,
    #     random_id=0,
    #     keyboard=builder.form(),
    #     group_id=333333,
    #     message='Меню (см. клавиатуру под строкой ввода)'
    # )

    # method_call = VkMethodCall(
    #         'messages',
    #         'send',
    #         dto_util.form(send_options, SendOptions)
    #     )
    
    # print(method_call)

    # call_queue = JoinableQueue()
    # call_queue.put(method_call)

    # method_call = None
    # method_call = call_queue.get()

    # match_method_call(method_call)


    # ui_templates = UiTemplates(ui_template_path)
    # ui_templates.init_element('main_menu')
    # print(ui_templates.get_element('main_menu'))

    # ui_templates.set_balance_in_main_menu(777)
    # print(ui_templates.get_element('main_menu'))
    
    # menu = MainMenu()
    # payload1 = Payload(
    #     command = PayloadCommand.go_to_page,
    #     context = 1
    # )
    # payload2 = Payload()
    # payload2.fill('go_to_page', page='2')

    # menu.set_payload_for_first_btn(payload1)
    # menu.set_payload_for_last_btn(payload2)
    # menu.set_label_for_page_btn('1/2')

    # builder = UIElementBuilder()
    # builder.build_ui_element(menu.content)
    # print(builder.form())

    driver = BuildInDriver()
    session = VkApiSession(driver, ACCESS_TOKEN)
    resp = session.groups_getLongPollServer(GROUP_ID)
    print(resp)

    # if resp.error is None:
    #     bot_session = VkBotSession(driver, resp.server, resp.key, resp.ts)
    #     events = bot_session.pool_events()
    #     print(events)

    # dto = '{"ts":"10","updates":[{"type":"message_new","object":{"message":{"date":1612685621,"from_id":326596496,"id":9,"out":0,"peer_id":326596496,"text":"Добрый день!","conversation_message_id":9,"fwd_messages":[],"important":false,"random_id":0,"attachments":[],"is_hidden":false},"client_info":{"button_actions":["text","vkpay","open_app","location","open_link","open_photo","callback","intent_subscribe","intent_unsubscribe"],"keyboard":true,"inline_keyboard":true,"carousel":true,"lang_id":0}},"group_id":202308925,"event_id":"810c3002e50fb85d205fdbbfa23c03a7dd05706b"}]}\r\n'
    # json_object = JSONObject.loads(dto)
    # print(json_object)
    # print(json_object.dumps(4))

    # vk_api_session = VkApiSession(driver, SEND_ACCESS_TOKEN)
    # resp = vk_api_session.messages_send(user_id=326596496, random_id=0, group_id=202308925, message='sent from code yet')
    # print(resp)

# '{"ts":"4","updates":[{"type":"message_new","object":{"id":3,"date":1612543491,"out":0,"user_id":326596496,"read_state":0,"title":"","body":"Ну как?","owner_ids":[]},"group_id":202308925,"event_id":"68ee4b473e298e049b608f317a26230f8f9e6da3"}]}\r\n'
# '{"ts":"10","updates":[{"type":"message_new","object":{"message":{"date":1612685621,"from_id":326596496,"id":9,"out":0,"peer_id":326596496,"text":"Добрый день!","conversation_message_id":9,"fwd_messages":[],"important":false,"random_id":0,"attachments":[],"is_hidden":false},"client_info":{"button_actions":["text","vkpay","open_app","location","open_link","open_photo","callback","intent_subscribe","intent_unsubscribe"],"keyboard":true,"inline_keyboard":true,"carousel":true,"lang_id":0}},"group_id":202308925,"event_id":"810c3002e50fb85d205fdbbfa23c03a7dd05706b"}]}\r\n'