from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from .client_context import ClientContext

from ...utils import account_manager as acc_mngr

from ...model import Client, VkUser

PROMO_AMOUNT = Decimal('99.00')

def get_client_context(session:OrmSession, user_id:int, promo:bool=False) -> ClientContext:

    vk_user = session.query(VkUser).filter(VkUser.user_id == user_id).one_or_none()

    if vk_user is None:
        client = Client()
        vk_user = VkUser(user_id = user_id)
        vk_user.client = client
        session.add_all([client, vk_user])
        session.flush()

        if promo:
            deposit_promo_funds(session, client.id)

    free_balance = acc_mngr.free_balance_by_client(session, vk_user.client.id)
    promo_balance = acc_mngr.promo_balance_by_client(session, vk_user.client.id)

    return ClientContext(client_id=vk_user.client.id, vk_user_id=user_id, free_balance=free_balance, promo_balance=promo_balance)        

def deposit_promo_funds(session:OrmSession, client_id:int):    
    promo_remain = acc_mngr.promo_balance_by_client(session, client_id)

    if promo_remain > 0:
        return

    acc_mngr.deposit_promo_funds(session, client_id, PROMO_AMOUNT)
