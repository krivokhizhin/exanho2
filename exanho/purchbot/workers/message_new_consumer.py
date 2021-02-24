import logging

from exanho.core.common import Error

from exanho.purchbot.vk.utils import VkBotContext
from exanho.purchbot.vk import VkApiSession
from exanho.purchbot.vk.drivers import BuildInDriver
from exanho.purchbot.vk.dto import JSONObject

from exanho.purchbot.vk.utils.message_manager import handle_message_new

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context):
    context = VkBotContext(**appsettings)
    
    driver = BuildInDriver()
    vk_api_session = VkApiSession(driver, context.access_token)

    context = context._replace(vk_api_session=vk_api_session)

    log.info('Initialized')
    return context

def work(context:VkBotContext, event_obj:JSONObject):
    try:
        handle_message_new(context, event_obj)
    except Error as er:
        log.error(er.message)
    except Exception as ex:
        log.exception(event_obj.dumps(), ex)

    return context 

def finalize(context):
    log.info('Finalized')