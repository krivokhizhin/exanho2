from sqlalchemy import desc, or_
from sqlalchemy.orm.session import Session as OrmSession

from ..model import *

from ..vk.utils import VkBotContext, ClientContext
from ..vk.ui import Payload
from ..vk.utils import message_manager as msg_mngr

def set_trade_status_wo_conditions(session:OrmSession, trade_id:int, old_status:TradeStatus, new_status:TradeStatus):
    assert isinstance(trade_id, int)
    assert isinstance(old_status, TradeStatus)
    assert isinstance(new_status, TradeStatus)

    trade = session.query(Trade).get(trade_id)

    assert trade is not None and trade.status == old_status

    print(f'OLD: {trade}')
    trade.status = new_status
    print(f'NEW: {trade}')

def manual_trade_executed(session:OrmSession, trade_id:int):
    assert isinstance(trade_id, int)

    trade = session.query(Trade).get(trade_id)

    assert trade is not None and trade.status == TradeStatus.DURING

    client_context = ClientContext(
        client_id=trade.client_id,
        vk_user_id=None,
        payload=None,
        free_balance=None,
        promo_balance=None
    )

    payload = Payload(
        trade = trade_id
    )

    msg_mngr.trade_executed(session, None, client_context, payload)