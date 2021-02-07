import logging
from collections import namedtuple

from exanho.orm.domain import Sessional
from exanho.core.common import Error, Timer
from exanho.core.manager_context import Context as ExanhoContext

from exanho.purchbot.vk import VkApiSession, UiTemplates
from exanho.purchbot.vk.drivers import BuildInDriver
from exanho.purchbot.vk.dto import JSONObject

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'access_token',
    'group_id',
    'ui_templates',
    'vk_api_session'
    ], defaults = [None])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)
    
    driver = BuildInDriver()
    vk_api_session = VkApiSession(driver, context.access_token)

    ui_templates = UiTemplates(context.ui_templates)
    ui_templates.init_element('main_menu')

    context = context._replace(ui_templates=ui_templates, vk_api_session=vk_api_session)

    log.info('Initialized')
    return context

def work(context:Context, event_obj:JSONObject):

    if hasattr(event_obj, 'message'):

        ui_templates:UiTemplates = context.ui_templates 
        vk_api_session:VkApiSession = context.vk_api_session

        try:

            resp = vk_api_session.messages_send(
                user_id=event_obj.message.from_id,
                random_id=0,
                keyboard=ui_templates.get_element('main_menu'),
                group_id=context.group_id,
                message='Выберите, пожалуйста, действие...'
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