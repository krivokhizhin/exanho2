from decimal import Decimal
from datetime import datetime
from exanho.purchbot.model.common.client import Client

from exanho.core.common import Error
from exanho.purchbot.model.account.account import BalAccCode
from sqlalchemy.orm.session import Session as OrmSession

from ..model.account import *

def get_account_name(balance_code:BalAccCode, analitic1, analitic2):
    analitic1 = '' if analitic1 is None else str(analitic1).rjust(LEN_ANALITIC, '0')
    analitic2 = '' if analitic2 is None else str(analitic2).rjust(LEN_ANALITIC, '0')

    return '{}{}{}'.format(balance_code.value, analitic1, analitic2)

def get_account(session:OrmSession, balance_code:BalAccCode, analitic1=None, analitic2=None) -> AccAccount:
    account_name = get_account_name(balance_code, analitic1, analitic2)
    account = session.query(AccAccount).filter(AccAccount.account == account_name).one_or_none()

    if account is None:
        account = AccAccount(balance_code, analitic1, analitic2)        
        session.add(account)
        session.flush()

    return account

def get_remain(session:OrmSession, account:AccAccount) -> AccRemain:
    remain = session.query(AccRemain).filter(AccRemain.account_id == account.id).one_or_none()

    if remain is None:
        remain = AccRemain(account)       
        session.add(remain)
        session.flush()

    return remain

def make_payment(session:OrmSession, dt:AccAccount, cr:AccAccount, amount:Decimal, credit=True) -> AccRecord:
    with session.begin_nested():
        dt_remain = get_remain(session, dt)
        cr_remain = get_remain(session, cr)

        remain_amount = cr_remain.dt - cr_remain.cr
        if not credit and remain_amount < amount:
            raise Error(f'The account balance ({cr_remain.account}) is less than the requested amount ({remain_amount} < {amount})')

        record = AccRecord(dt.id, cr.id, amount)
        session.merge(record)

        dt_remain.dt += amount
        dt_remain.last_payment_id = record.id

        cr_remain.cr += amount
        cr_remain.last_payment_id = record.id
       
        return record

def get_remain_amount(session:OrmSession, account:AccAccount) -> Decimal:
    remain = get_remain(session, account)
    return remain.dt - remain.cr


# ************ free balance ******************************

def get_free_balance(session:OrmSession, client:Client) -> Decimal:
    account = get_account(session, BalAccCode.C101, client.id)
    return get_remain_amount(session, account)


# ************ promo **************************************

def get_promo_balance(session:OrmSession, client:Client) -> Decimal:
    account = get_account(session, BalAccCode.C107, client.id)
    return get_remain_amount(session, account)

def deposit_promo_funds(session:OrmSession, client:Client, amount:Decimal):
    if amount > 0:
        dt_account = get_account(session, BalAccCode.C107, client.id)
        cr_account = get_account(session, BalAccCode.C107)
        record = make_payment(session, dt_account, cr_account, amount)
        record.date = datetime.now()