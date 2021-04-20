from sqlalchemy import desc, or_
from sqlalchemy.orm.session import Session as OrmSession

from ..model import *

from ..vk.utils import VkBotContext, ClientContext
from ..vk.ui import Payload
from ..vk.utils import message_manager as msg_mngr

def set_order_status_wo_conditions(session:OrmSession, order_id:int, old_status:OrderStatus, new_status:OrderStatus):
    assert isinstance(order_id, int)
    assert isinstance(old_status, OrderStatus)
    assert isinstance(new_status, OrderStatus)

    order = session.query(Order).get(order_id)

    assert order is not None and order.status == old_status

    print(f'OLD: {order}')
    order.status = new_status
    print(f'NEW: {order}')

def manual_order_executed(session:OrmSession, order_id:int):
    assert isinstance(order_id, int)

    order = session.query(Order).get(order_id)

    assert order is not None and order.status == OrderStatus.DURING

    client_context = ClientContext(
        client_id=order.client_id,
        vk_user_id=None,
        free_balance=None,
        promo_balance=None
    )

    payload = Payload(
        order = order_id
    )

    msg_mngr.order_executed(session, None, client_context, payload)