import logging
from collections import namedtuple
from multiprocessing import JoinableQueue

from exanho.core.common import Error
from exanho.purchbot.vk import VkApiSession, VkBotSession
from exanho.purchbot.vk.drivers import BuildInDriver

from exanho.core.manager_context import Context as ExanhoContext
from exanho.purchbot.vk.dto.groups import GetLongPollServerResponse
from exanho.purchbot.vk.dto.bot.group_event import GroupEvent

log = logging.getLogger(__name__)

Context = namedtuple('Context', [
    'groups_events',
    'queues_by_events',
    'access_token',
    'group_id',
    'bot_session'
    ], defaults=[None])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)

    if len(context.groups_events) != len(context.queues_by_events):
        raise RuntimeError(f'The number of "groups_events" and "queues_by_events" must match ({len(context.groups_events)}!={len(context.queues_by_events)})')
   
    queues_by_events = dict()
    for group_event, queue_name in zip(context.groups_events, context.queues_by_events):
        queues_by_events[group_event] = exanho_context.joinable_queues[queue_name]

    driver = BuildInDriver()
    bot_data = _get_bot_data(driver, context.access_token, context.group_id)
    bot_session = VkBotSession(driver, bot_data.server, bot_data.key, bot_data.ts)

    context = context._replace(queues_by_events=queues_by_events, bot_session=bot_session)
    
    log.info(f'Initialized bot for {context.group_id} group')
    return context

def work(context:Context):
    bot_session:VkBotSession = context.bot_session
    queues_by_events:dict = context.queues_by_events

    try:
        events = bot_session.pool_events()

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

                jq:JoinableQueue = queues_by_events.get(new_event.type_, None)
                if jq:
                    jq.put(new_event.object_)
                    log.info(f'received "{new_event.type_}" event')
                else:
                    log.warning(f'No consumer(queue) for {new_event.type_} event type')

            bot_session.ts = events.ts

    except Error as er:
        log.error(er.message)
    except Exception as ex:
        log.exception(ex)

    return context 

def finalize(context):
    log.info('Finalized')


def _get_bot_data(driver, access_token, group_id) -> GetLongPollServerResponse:
    vk_api_session = VkApiSession(driver, access_token)
    bot_data = vk_api_session.groups_getLongPollServer(group_id)
    if bot_data.error:
        raise Error(f'VK getLongPollServer error: code={bot_data.error.error_code}, msg={bot_data.error.error_msg}')
    return bot_data
