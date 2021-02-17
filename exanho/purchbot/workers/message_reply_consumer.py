import logging
from collections import namedtuple

from exanho.orm.domain import Sessional
from exanho.core.common import Error, Timer
from exanho.core.manager_context import Context as ExanhoContext

from exanho.purchbot.vk import VkApiSession
from exanho.purchbot.vk.drivers import BuildInDriver
from exanho.purchbot.vk.dto import JSONObject

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'access_token',
    'group_id',
    'vk_api_session'
    ], defaults = [None])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)
    
    driver = BuildInDriver()
    vk_api_session = VkApiSession(driver, context.access_token)

    context = context._replace(vk_api_session=vk_api_session)

    log.info('Initialized')
    return context

def work(context:Context, event_obj:JSONObject):
    return context 

def finalize(context):
    log.info('Finalized')