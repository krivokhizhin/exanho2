from collections import namedtuple
import logging
from multiprocessing.queues import JoinableQueue

from exanho.core.manager_context import Context as ExanhoContext

from exanho.core.common import Error
from exanho.purchbot.vk.drivers import RequestsDriver
from exanho.purchbot.vk.dto import JSONObject
from exanho.purchbot.vk.dto.groups import GetLongPollServerResponse
from exanho.purchbot.vk.dto.bot import GroupEvent
from exanho.purchbot.vk import VkApiSession, VkBotSession

import exanho.purchbot.utils.json64 as json_util

log = logging.getLogger(__name__)

VkLongPollContext = namedtuple('VkLongPollContext', [
    'access_token',
    'group_id',
    'work_types',
    'default_work_queue',
    'vkpay_like',
    'vkpay_work_queue',
    'queue_filters',
    'work_queues',
    'bot_session'
    ], defaults = [[], [], None])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = VkLongPollContext(**appsettings)

    if len(context.queue_filters) != len(context.work_queues):
        raise Error(f'len(context.filters) not match len(context.work_queues): {len(context.filters)} != {len(context.work_queues)}')

    default_work_queue = exanho_context.joinable_queues[context.default_work_queue]
    vkpay_work_queue = exanho_context.joinable_queues[context.vkpay_work_queue]

    work_queues = dict()
    queue_filters = dict()
    for work_queue_name, queue_filter in zip(context.work_queues, context.queue_filters):
        work_queues[work_queue_name] = exanho_context.joinable_queues[work_queue_name]
        queue_filters[work_queue_name] = queue_filter

    driver = RequestsDriver()
    bot_data = _get_bot_data(driver, context.access_token, context.group_id)
    bot_session = VkBotSession(driver, bot_data.server, bot_data.key, bot_data.ts)
    log.debug(json_util.convert_obj_to_json_str(bot_data, JSONObject))

    context = context._replace(
        bot_session=bot_session,
        queue_filters=queue_filters,
        work_queues=work_queues,
        default_work_queue=default_work_queue,
        vkpay_work_queue=vkpay_work_queue
    )
    
    log.info(f'Initialized bot for {context.group_id} group')
    return context

def work(context:VkLongPollContext):
    bot_session:VkBotSession = context.bot_session

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
                    log.warning(f'received "{new_event.type}" event from group {new_event.group_id}, expected from group {context.group_id}')
                    continue

                if new_event.type not in context.work_types:
                    log.warning(f'got an unhandled type: {new_event.type}')
                    continue

                try:

                    if str(new_event.type).startswith(context.vkpay_like):
                        vkpay_queue:JoinableQueue = context.vkpay_work_queue
                        vkpay_queue.put(json_util.convert_obj_to_json_str(new_event, GroupEvent, JSONObject))
                        continue

                    # TODO: extract vk_user_id and filtration 

                    new_event_str = json_util.convert_obj_to_json_str(new_event, GroupEvent, JSONObject)
                    default_work_queue:JoinableQueue = context.default_work_queue
                    default_work_queue.put(new_event_str)

                    log.info(f'received "{new_event.type}" event')
                    log.debug(new_event_str)
                except Error as er:
                    log.error(er.message)
                except TypeError:
                    log.warning(new_event.object.__dict__)
                except Exception as ex:
                    log.exception(json_util.convert_obj_to_json_str(new_event.object, JSONObject), ex)

            bot_session.ts = events.ts

    except Error as er:
        log.error(er.message)
    except Exception as ex:
        log.exception(ex)

    return context 

def finalize(context:VkLongPollContext):
    context.call_queue.put(None)
    log.info('Finalized')


def _get_bot_data(driver, access_token, group_id) -> GetLongPollServerResponse:
    vk_api_session = VkApiSession(driver, access_token)
    bot_data = vk_api_session.groups_getLongPollServer(group_id)
    if bot_data.error:
        raise Error(f'VK groups.getLongPollServer error: code={bot_data.error.error_code}, msg={bot_data.error.error_msg}')
    return bot_data