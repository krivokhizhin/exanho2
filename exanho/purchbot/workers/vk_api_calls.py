from exanho.purchbot.vk.dto.ok_response import OkResponse
from exanho.purchbot.vk.dto.method_call import VkMethodCall
import logging

from multiprocessing import JoinableQueue

from exanho.core.common import Error

from exanho.purchbot.vk.utils import VkApiContext
from exanho.purchbot.vk import VkApiSession
from exanho.purchbot.vk.drivers import BuildInDriver

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context):
    context = VkApiContext(**appsettings)

    call_queue = exanho_context.joinable_queues[context.call_queue]
    
    driver = BuildInDriver()
    vk_api_session = VkApiSession(driver, context.access_token)

    if not isinstance(context.max_calls, int):
        raise Error('The max_calls must have an integer value')

    context = context._replace(vk_session=vk_api_session, call_queue=call_queue)

    log.info('Initialized')
    return context

def work(context:VkApiContext):
    call_queue:JoinableQueue = context.call_queue
    call_counter = 0

    method_call = call_queue.get()
    if method_call is None:
        return context

    while call_counter < context.max_calls:
        if method_call is None:
            method_call = call_queue.get()
            if method_call is None:
                return context

        try:
            match_method_call(context, method_call)
        except Error as er:
            log.error(method_call)
            log.error(er.message)
        except Exception as ex:
            log.error(method_call)
            log.exception(ex)

        call_counter += 1
        call_queue.task_done()
        method_call = None

    if context.max_calls <= call_counter:
        log.warning(f'Calls per minute limit has been reached: {call_counter}')

    return context 

def finalize(context):
    log.info('Finalized')

def match_method_call(context:VkApiContext, method_call:VkMethodCall):
    vk_api_session:VkApiSession = context.vk_session

    vk_api_method_name = method_call.form_vk_api_method_name()

    if hasattr(vk_api_session, vk_api_method_name) and callable(getattr(vk_api_session, vk_api_method_name)):
        vk_api_method = getattr(vk_api_session, vk_api_method_name)
        resp:OkResponse = vk_api_method(method_call.options)
        if resp.error:
            raise Error(f'VK api_method call failed with error: code={resp.error.error_code}, msg={resp.error.error_msg}')
    else:
        log.warning(f'{method_call} | Not supported section and/or method')