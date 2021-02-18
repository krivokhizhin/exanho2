import logging

from exanho.core.manager_context import Context as ExanhoContext

from exanho.core.common import Error
from exanho.purchbot.vk.drivers import BuildInDriver
from exanho.purchbot.vk.dto import JSONObject
from exanho.purchbot.vk.dto.groups import GetLongPollServerResponse
from exanho.purchbot.vk.dto.bot import GroupEvent
from exanho.purchbot.vk.utils import VkApiContext
from exanho.purchbot.vk import VkApiSession, VkBotSession

import exanho.purchbot.vk.utils.message_manager as msg_mngr
import exanho.purchbot.vk.dto.util as dto_mngr

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context:ExanhoContext):
    context = VkApiContext(**appsettings)

    call_queue = exanho_context.joinable_queues[context.call_queue]

    driver = BuildInDriver()
    bot_data = _get_bot_data(driver, context.access_token, context.group_id)
    bot_session = VkBotSession(driver, bot_data.server, bot_data.key, bot_data.ts)
    log.debug(dto_mngr.convert_obj_to_json_str(bot_data, JSONObject))

    context = context._replace(vk_session=bot_session, call_queue=call_queue)
    
    log.info(f'Initialized bot for {context.group_id} group')
    return context

def work(context:VkApiContext):
    bot_session:VkBotSession = context.vk_session

    try:
        events = bot_session.pool_events()
        log.debug(f'events.ts: {events.ts}')

        if events.failed:
            if events.failed == 1:
                log.warning(f'failed=1: ts will be reassigned from {bot_session.ts} to {events.ts}')
                bot_session.ts = events.ts
            elif events.failed == 2:
                log.warning('failed=2: key will be reassigned')
                bot_data = _get_bot_data(bot_session.driver, context.access_token, context.group_id)
                bot_session.key = bot_data.key
            elif events.failed == 3:
                log.warning('failed=3: key and ts will be reassigned')
                bot_data = _get_bot_data(bot_session.driver, context.access_token, context.group_id)
                bot_session.key = bot_data.key
                bot_session.ts = bot_data.ts
            else:
                raise Error(f'unknown failed value: {events.failed}')
        else:            
            for new_event in events.updates:
                assert isinstance(new_event, GroupEvent)
                if new_event.group_id != context.group_id:
                    log.warning(f'received "{new_event.type_}" event from group {new_event.group_id}, expected from group {context.group_id}')
                    continue

                try:
                    _handle_event(context, new_event)
                    log.info(f'received "{new_event.type_}" event')
                    if new_event.type_ != 'message_reply':
                        log.debug(dto_mngr.convert_obj_to_json_str(new_event.object_, JSONObject))
                except Error as er:
                    log.error(er.message)
                except TypeError:
                    log.warning(new_event.object_.__dict__)
                except Exception as ex:
                    log.exception(dto_mngr.convert_obj_to_json_str(new_event.object_, JSONObject), ex)

            bot_session.ts = events.ts

    except Error as er:
        log.error(er.message)
    except Exception as ex:
        log.exception(ex)

    return context 

def finalize(context:VkApiContext):
    context.call_queue.put(None)
    log.info('Finalized')


def _get_bot_data(driver, access_token, group_id) -> GetLongPollServerResponse:
    vk_api_session = VkApiSession(driver, access_token)
    bot_data = vk_api_session.groups_getLongPollServer(group_id)
    if bot_data.error:
        raise Error(f'VK groups.getLongPollServer error: code={bot_data.error.error_code}, msg={bot_data.error.error_msg}')
    return bot_data

def _handle_event(context:VkApiContext, new_event:GroupEvent):    

    if new_event.type_ == 'message_new':
        msg_mngr.handle_message_new(context, new_event.object_)
    elif new_event.type_ == 'message_reply':
        pass
    elif new_event.type_ == 'message_event':
        msg_mngr.handle_message_event(context, new_event.object_)
    elif new_event.type_ == 'vkpay_transaction':
        pass