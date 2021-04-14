from exanho.purchbot.vk.dto.json_object import JSONObject
import logging
from xmlrpc.client import ServerProxy
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.manager_context import Context as ExanhoContext
from exanho.core.common import Error
from exanho.orm.domain import Sessional

import exanho.purchbot.utils.json64 as json_util
import exanho.purchbot.vk.utils.message_manager as msg_mngr
from exanho.purchbot.vk.dto import JSONObject
from exanho.purchbot.vk.dto.bot import GroupEvent
from exanho.purchbot.vk.utils.vk_bot_context import VkBotContext

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context:ExanhoContext):
    context = VkBotContext(**appsettings)
    
    call_queue = exanho_context.joinable_queues[context.call_queue]

    host, port = exanho_context.get_service_endpoint(context.participant_service)
    part_uri = f'http://{host}:{port}/RPC2'
    participant_service = ServerProxy(part_uri, allow_none=True, use_builtin_types=True)

    context = context._replace(call_queue=call_queue, participant_service=participant_service)

    log.info('Initialized')
    return context

def work(context:VkBotContext, new_event_str:str):
    
    new_event_obj:JSONObject = json_util.convert_json_str_to_obj(new_event_str, JSONObject)
    new_event = GroupEvent()
    new_event.fill(new_event_obj)

    try:
        with Sessional.domain.session_scope() as session:
            assert isinstance(session, OrmSession)
            _handle_event(session, context, new_event)
        log.debug(f'handled "{new_event.type}" event')
    except Error as er:
        log.error(er.message)
    except Exception as ex:
        log.exception(new_event_str, ex)
        
    return context 

def finalize(context):
    log.info('Finalized')

def _handle_event(session:OrmSession, context:VkBotContext, new_event:GroupEvent):    

    if new_event.type == 'message_new':
        msg_mngr.handle_message_new(session, context, new_event.object)
    elif new_event.type == 'message_reply':
        msg_mngr.handle_message_reply(session, context, new_event.object)
    elif new_event.type == 'message_event':
        msg_mngr.handle_message_event(session, context, new_event.object)
    elif new_event.type == 'vkpay_transaction':
        pass