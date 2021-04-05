from sqlalchemy import desc, or_
from sqlalchemy.orm.session import Session as OrmSession

from ..model import *

def accumulated_accounts(session:OrmSession, show_promo=False):    
    for acc in session.query(AccAccount).filter(AccAccount.analitic1 == None).order_by(AccAccount.account):
        if not show_promo and _is_promo(acc.balance_code):
            continue
        print(f'{acc.remain} | {acc}')

def client_accounts(session:OrmSession, show_promo=False):    
    for acc, rem in session.query(AccAccount, AccRemain).join(AccRemain).\
        filter(AccAccount.analitic1 != None).filter(AccAccount.analitic2 == None).order_by(desc(AccRemain.dt - AccRemain.cr)):
        if not show_promo and _is_promo(acc.balance_code):
            continue
        print(f'{rem} | {acc}')

def transit_account_remains(session:OrmSession, show_promo=False):  
    for acc, rem in session.query(AccAccount, AccRemain).join(AccRemain).\
        filter(AccAccount.analitic1 != None).filter(AccAccount.analitic2 != None).\
            filter(AccRemain.dt - AccRemain.cr != 0).order_by(desc(AccRemain.dt - AccRemain.cr), AccAccount.account):
        if not show_promo and _is_promo(acc.balance_code):
            continue
        print(f'{rem} | {acc}')

def during_orders(session:OrmSession):   
    for order in session.query(Order).filter(Order.status == OrderStatus.DURING).order_by(Order.amount.desc(), Order.id):
        print(f'{order.id:>6} | {order.client_id:>6} | {order.product} | {order.amount:18.2f} | {order.paid:>5}')

def acc_record_by_order(session:OrmSession, order_id:int, show_promo=False):
    assert isinstance(order_id, int)

    order = session.query(Order).get(order_id)
    assert order is not None
    print(order)

    transit_client_account_ids = list()

    for ca in session.query(AccAccount).\
        filter(AccAccount.analitic1 == order.client_id).\
            filter(or_(AccAccount.analitic2 == order_id, AccAccount.analitic2 == None)).\
                order_by(AccAccount.id):

        if not show_promo and _is_promo(ca.balance_code):
            continue

        print(f'{ca.remain} | {ca}')

        if ca.analitic2:
            transit_client_account_ids.append(ca.id)

    for rec in session.query(AccRecord).filter(or_(AccRecord.dt.in_(transit_client_account_ids), AccRecord.cr.in_(transit_client_account_ids))).\
        order_by(AccRecord.id):
        print(f'{rec}')



def _is_promo(code:BalAccCode):
    bal_codes = [
        BalAccCode.C907,
        BalAccCode.C107,
        BalAccCode.C701,
        BalAccCode.C702,
        BalAccCode.C731,
        BalAccCode.C761,
        BalAccCode.C762,
        BalAccCode.C763
    ]

    return code in bal_codes