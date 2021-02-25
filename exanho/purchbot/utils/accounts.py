from decimal import Decimal

from exanho.core.common import Error
from exanho.purchbot.model.account.account import BalAccCode
from sqlalchemy.orm.session import Session as OrmSession

from ..model.account import *

def get_account_name(balance_code:BalAccCode, analitic1, analitic2):
    # if analitic2 and analitic1 is None:
    assert not (analitic2 and analitic1 is None)

    analitic1 = '' if analitic1 is None else str(analitic1).rjust(LEN_ANALITIC, '0')
    analitic2 = '' if analitic2 is None else str(analitic2).rjust(LEN_ANALITIC, '0')

    return '{}{}{}'.format(balance_code.value, analitic1, analitic2)

def get_account(session:OrmSession, balance_code:BalAccCode, analitic1=None, analitic2=None, **kwargs) -> AccAccount:
    account_name = get_account_name(balance_code, analitic1, analitic2)
    account = session.query(AccAccount).filter(AccAccount.account == account_name).one_or_none()

    if account is None:
        account = AccAccount(balance_code, analitic1, analitic2)        
        account.desc = kwargs.get('desc', None)
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

def get_remain_amount(session:OrmSession, account:AccAccount) -> Decimal:
    remain = get_remain(session, account)
    return remain.dt - remain.cr

def make_payment(session:OrmSession, dt:AccAccount, cr:AccAccount, amount:Decimal, credit=False) -> AccRecord:
    if amount <= 0:
        raise Error(f'Invalid amount for the transaction: {amount}')

    with session.begin_nested():
        dt_remain = get_remain(session, dt)
        cr_remain = get_remain(session, cr)

        remain_amount = cr_remain.dt - cr_remain.cr
        if not credit and remain_amount < amount:
            raise Error(f'The account balance is less than the requested amount ({cr_remain.account.account}: {remain_amount} < {amount})')

        record = AccRecord(dt.id, cr.id, amount)
        session.add(record)
        session.flush([record])

        dt_remain.dt += amount
        dt_remain.updated_by = record.id

        cr_remain.cr += amount
        cr_remain.updated_by = record.id
       
        return record