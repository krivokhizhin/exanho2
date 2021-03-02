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

def during_trades(session:OrmSession):   
    for trade in session.query(Trade).filter(Trade.status == TradeStatus.DURING).order_by(Trade.amount.desc(), Trade.id):
        print(f'{trade.id:>6} | {trade.client_id:>6} | {trade.product} | {trade.amount:18.2f} | {trade.paid:>5}')

def acc_record_by_trade(session:OrmSession, trade_id:int, show_promo=False):
    assert isinstance(trade_id, int)

    trade = session.query(Trade).get(trade_id)
    assert trade is not None
    print(trade)

    transit_client_account_ids = list()

    for ca in session.query(AccAccount).\
        filter(AccAccount.analitic1 == trade.client_id).\
            filter(or_(AccAccount.analitic2 == trade_id, AccAccount.analitic2 == None)).\
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