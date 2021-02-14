import logging

from exanho.core.common import Error

from exanho.purchbot.vk.utils import VkApiContext
from exanho.purchbot.vk import VkApiSession
from exanho.purchbot.vk.drivers import BuildInDriver
from exanho.purchbot.vk.dto import JSONObject

from exanho.purchbot.vk.utils.message_manager import handle_message_event

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context):
    context = VkApiContext(**appsettings)
    
    driver = BuildInDriver()
    vk_api_session = VkApiSession(driver, context.access_token)

    context = context._replace(vk_api_session=vk_api_session)

    log.info('Initialized')
    return context

def work(context:VkApiContext, event_obj:JSONObject):
    try:
        handle_message_event(context, event_obj)
    except Error as er:
        log.error(er.message)
    except Exception as ex:
        log.exception(event_obj.dumps(), ex)

    return context
    log.debug(event_obj.dumps())

    user_id = None
    if not hasattr(event_obj, 'user_id'):
        return context

    user_id = event_obj.user_id

    payload = None
    if not hasattr(event_obj, 'payload'):
        return context

    payload = event_obj.payload
    if isinstance(payload, str):
        payload = JSONObject.loads(event_obj.payload.replace('\"', '"'))

    if hasattr(payload, 'command'):
        vk_api_session:VkApiSession = context.vk_api_session

        try:

            if payload.command == 'get_balance':

                resp = vk_api_session.messages_send(
                    user_id=user_id,
                    random_id=0,
                    group_id=context.group_id,
                    message='Ваш баланс: 999\nДля пополнения баланса нажмите на кнопку "Оплатить через VK pay"'
                    )

                if resp.error:
                    raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')

            else:

                resp = vk_api_session.messages_send(
                    user_id=user_id,
                    random_id=0,
                    group_id=context.group_id,
                    message='На данный момент раздел находится в разработке...'
                    )

                if resp.error:
                    raise Error(f'VK messages.send error: code={resp.error.error_code}, msg={resp.error.error_msg}')


        except Error as er:
            log.error(er.message)
        except Exception as ex:
            log.exception(ex)


    return context 

def finalize(context):
    log.info('Finalized')