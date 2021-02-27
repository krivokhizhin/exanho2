import logging
import time

from collections import namedtuple
from multiprocessing import JoinableQueue
from queue import Empty

from exanho.core.common import Error

from exanho.purchbot.vk import VkApiSession
from exanho.purchbot.vk.drivers import RequestsDriver
from exanho.purchbot.vk.dto import MethodResponseBase, VkMethodCall, IVkDto
import exanho.purchbot.vk.dto.util as dto_mngr

log = logging.getLogger(__name__)

VkApiContext = namedtuple('VkApiContext', [
    'access_token',
    'group_id',
    'call_queue',
    'max_calls',
    'timeout',
    'vk_session'
    ], defaults = [20, 1, None])

def initialize(appsettings, exanho_context):
    context = VkApiContext(**appsettings)

    call_queue = exanho_context.joinable_queues[context.call_queue]
    
    driver = RequestsDriver()
    vk_api_session = VkApiSession(driver, context.access_token)

    if not isinstance(context.max_calls, int):
        raise Error('The max_calls must have an integer value')

    context = context._replace(vk_session=vk_api_session, call_queue=call_queue)

    log.info('Initialized')
    return context

def work(context:VkApiContext):
    vk_api_session:VkApiSession = context.vk_session
    call_queue:JoinableQueue = context.call_queue
    call_counter = 0

    method_call = call_queue.get()
    if method_call is None:
        return context

    while call_counter < context.max_calls:
        if method_call is None:
            try:
                method_call = call_queue.get(block=True, timeout=context.timeout)
            except Empty:
                return context
            if method_call is None:
                return context

            assert isinstance(method_call, VkMethodCall)

        try:
            weight = vk_api_session.method_weight(method_call.form_vk_api_method_name())
            call_counter += weight
            if call_counter > context.max_calls:
                log.warning(f'Calls were forced to pause ({call_counter+weight} > {context.max_calls})')
                time.sleep(context.timeout)
                call_counter = weight

            match_method_call(context, method_call)

        except Error as er:
            log.error(method_call)
            log.error(er.message)
        except Exception as ex:
            log.error(method_call)
            log.exception(ex)

        call_queue.task_done()
        method_call = None

    if call_counter == context.max_calls:
        log.warning(f'Calls per second limit has been reached: {call_counter}')

    return context 

def finalize(context):
    log.info('Finalized')

def match_method_call(context:VkApiContext, method_call:VkMethodCall):
    vk_api_session:VkApiSession = context.vk_session

    vk_api_method_name = method_call.form_vk_api_method_name()

    if hasattr(vk_api_session, vk_api_method_name) and callable(getattr(vk_api_session, vk_api_method_name)):
        vk_api_method = getattr(vk_api_session, vk_api_method_name)
        resp = vk_api_method(method_call.options)
        if resp.error:
            raise Error(f'VK api_method call failed with error: code={resp.error.error_code}, msg={resp.error.error_msg}')
        else:
            log.debug(dto_mngr.convert_obj_to_json_str(resp, IVkDto))
    else:
        log.warning(f'{method_call} | Not supported section and/or method')