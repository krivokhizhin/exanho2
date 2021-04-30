import logging
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.manager_context import Context as ExanhoContext
from exanho.core.common import Error
from exanho.orm.domain import Sessional

import exanho.purchbot.utils.json64 as json_util
import exanho.purchbot.utils.account_manager as acc_mngr
import exanho.purchbot.vk.events.provider as event_provider
from exanho.purchbot.vk.utils import client as clt_eng
from exanho.purchbot.vk.utils import ui_manager as ui_mngr
from exanho.purchbot.vk.dto import JSONObject
from exanho.purchbot.vk.dto.bot import GroupEvent
from exanho.purchbot.vk.events.vkpay_transaction import VkpayTransaction
from exanho.purchbot.vk.utils.vk_bot_context import VkBotContext

log = logging.getLogger(__name__)

def initialize(appsettings, exanho_context:ExanhoContext):
    context = VkBotContext(**appsettings)
    
    call_queue = exanho_context.joinable_queues[context.call_queue]

    context = context._replace(call_queue=call_queue, participant_service=None)

    log.info('Initialized')
    return context

def work(context:VkBotContext, new_event_str:str):
    log.info(f'received: {new_event_str}')
    
    new_event_obj:JSONObject = json_util.convert_json_str_to_obj(new_event_str, JSONObject)
    new_event = GroupEvent()
    new_event.fill(new_event_obj)

    if new_event.type != 'vkpay_transaction':
        log.warning(f'not expected event type received: {new_event.type}')
        return context    

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)
        try:
            _handle_vkpay_transaction(session, context, event_provider.get_vkpay_transaction(new_event.object))
            log.debug(f'handled "{new_event.type}" event')
        except Error as er:
            session.rollback()
            log.error(er.message)
        except Exception as ex:
            session.rollback()
            log.exception(new_event_str, ex)
        
    return context 

def finalize(context):
    log.info('Finalized')

def _handle_vkpay_transaction(session:OrmSession, context:VkBotContext, vkpay_transaction:VkpayTransaction):
    client_context = clt_eng.get_client_context(session, vkpay_transaction.from_id,promo=False)

    acc_mngr.deposit_funds_by_vkpay(session, client_context.client_id, vkpay_transaction.amount, vkpay_transaction.date, vkpay_transaction.description)

    free_balance = acc_mngr.free_balance_by_client(session, client_context.client_id)
    promo_balance = acc_mngr.promo_balance_by_client(session, client_context.client_id)
    client_context = client_context._replace(free_balance=free_balance, promo_balance=promo_balance)

    message = ''
    try:
        message += f'Получен перевод на сумму {vkpay_transaction.amount} р. Баланс Вашего счета обновлен.'
        ui_mngr.show_main_menu(session, context, client_context, message)
    except Exception as ex:
        log.exception(message, ex)