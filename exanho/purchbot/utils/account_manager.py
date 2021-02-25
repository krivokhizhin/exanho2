from decimal import Decimal
from sqlalchemy.orm.session import Session as OrmSession

from exanho.purchbot.model import BalAccCode, AccAccount, Product, Trade

from . import accounts as util


# ************ free balance ******************************

def free_balance_by_client(session:OrmSession, client_id:int) -> Decimal:
    account = util.get_account(session, BalAccCode.C101, client_id, desc=f'Свободный остаток клиента id={client_id}')
    return util.get_remain_amount(session, account)

def free_balance_by_client_acc(session:OrmSession, client_id:int) -> AccAccount:
    return util.get_account(session, BalAccCode.C101, client_id)


# *********** product ***************************************

def client_payment_acc(session:OrmSession, client_id:int, trade_id:int) -> AccAccount:
    trade = session.query(Trade).get(trade_id)
    product_code = session.query(Product.code).filter(Product.id == trade.product_id).scalar()
    desc=f'Счет оплаты услуги {product_code} для клиента id={client_id}'

    if product_code == 'QUE_PAR_ACT':
        return util.get_account(session, BalAccCode.C301, client_id, trade_id, desc=desc)

    if product_code == 'QUE_PAR_HIS':
        return util.get_account(session, BalAccCode.C302, client_id, trade_id, desc=desc)

    if product_code == 'SUB_PAR':
        return util.get_account(session, BalAccCode.C331, client_id, trade_id, desc=desc)

    if product_code == 'REP_PAR_ACT':
        return util.get_account(session, BalAccCode.C361, client_id, trade_id, desc=desc)

    if product_code == 'REP_PAR_HIS':
        return util.get_account(session, BalAccCode.C362, client_id, trade_id, desc=desc)

    if product_code == 'REP_PARS_CON':
        return util.get_account(session, BalAccCode.C363, client_id, trade_id, desc=desc)

def product_revenue_acc(session:OrmSession, trade_id:int) -> AccAccount:
    trade = session.query(Trade).get(trade_id)
    product_code = session.query(Product.code).filter(Product.id == trade.product_id).scalar()
    desc=f'Счет оплат по услуге {product_code}'

    if product_code == 'QUE_PAR_ACT':
        return util.get_account(session, BalAccCode.C301, desc=desc)

    if product_code == 'QUE_PAR_HIS':
        return util.get_account(session, BalAccCode.C302, desc=desc)

    if product_code == 'SUB_PAR':
        return util.get_account(session, BalAccCode.C331, desc=desc)

    if product_code == 'REP_PAR_ACT':
        return util.get_account(session, BalAccCode.C361, desc=desc)

    if product_code == 'REP_PAR_HIS':
        return util.get_account(session, BalAccCode.C362, desc=desc)

    if product_code == 'REP_PARS_CON':
        return util.get_account(session, BalAccCode.C363, desc=desc)


# ************ promo **************************************

def deposit_promo_funds(session:OrmSession, client_id:int, amount:Decimal):
    if amount > 0:
        dt_account = util.get_account(session, BalAccCode.C107, client_id, desc=f'Промо счет клиента id={client_id}')
        cr_account = util.get_account(session, BalAccCode.C907, desc='Промо счет оператора')
        record = util.make_payment(session, dt_account, cr_account, amount, True)

def promo_balance_by_client(session:OrmSession, client_id:int) -> Decimal:
    account = util.get_account(session, BalAccCode.C107, client_id, desc=f'Промо счет клиента id={client_id}')
    return util.get_remain_amount(session, account)

def promo_by_client_acc(session:OrmSession, client_id:int) -> AccAccount:
    return util.get_account(session, BalAccCode.C107, client_id)

def client_promo_payment_acc(session:OrmSession, client_id:int, trade_id:int) -> AccAccount:
    trade = session.query(Trade).get(trade_id)
    product_code = session.query(Product.code).filter(Product.id == trade.product_id).scalar()
    desc=f'Промо-счет оплаты услуги {product_code} для клиента id={client_id}'

    if product_code == 'QUE_PAR_ACT':
        return util.get_account(session, BalAccCode.C701, client_id, trade_id, desc=desc)

    if product_code == 'QUE_PAR_HIS':
        return util.get_account(session, BalAccCode.C702, client_id, trade_id, desc=desc)

    if product_code == 'SUB_PAR':
        return util.get_account(session, BalAccCode.C731, client_id, trade_id, desc=desc)

    if product_code == 'REP_PAR_ACT':
        return util.get_account(session, BalAccCode.C761, client_id, trade_id, desc=desc)

    if product_code == 'REP_PAR_HIS':
        return util.get_account(session, BalAccCode.C762, client_id, trade_id, desc=desc)

    if product_code == 'REP_PARS_CON':
        return util.get_account(session, BalAccCode.C763, client_id, trade_id, desc=desc)

def product_promo_revenue_acc(session:OrmSession, trade_id:int) -> AccAccount:
    trade = session.query(Trade).get(trade_id)
    product_code = session.query(Product.code).filter(Product.id == trade.product_id).scalar()
    desc=f'Промо-счет оплат по услуге {product_code}'

    if product_code == 'QUE_PAR_ACT':
        return util.get_account(session, BalAccCode.C701, desc=desc)

    if product_code == 'QUE_PAR_HIS':
        return util.get_account(session, BalAccCode.C702, desc=desc)

    if product_code == 'SUB_PAR':
        return util.get_account(session, BalAccCode.C731, desc=desc)

    if product_code == 'REP_PAR_ACT':
        return util.get_account(session, BalAccCode.C761, desc=desc)

    if product_code == 'REP_PAR_HIS':
        return util.get_account(session, BalAccCode.C762, desc=desc)

    if product_code == 'REP_PARS_CON':
        return util.get_account(session, BalAccCode.C763, desc=desc)
