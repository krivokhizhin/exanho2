from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error

from ..utils import accounts as acc_util
from ..utils import account_manager as acc_mngr
from ..model import AddInfoSettings, Product, Tariff, OrderStatus, Order, ProductAddInfo, AddInfoCode, LastOrderDetailing

def create_or_get_order(session:OrmSession, product_code:str, client_id:int) -> int:
    product = session.query(Product).filter(Product.code == product_code).one_or_none()
    if product is None:
        raise Error(f'unknown product code: {product_code}')

    amount = session.query(Tariff.value).filter(Tariff.product == product).scalar()

    order = session.query(Order).\
        filter(Order.client_id == client_id, Order.product_id == product.id, Order.status.in_([OrderStatus.NEW, OrderStatus.FILLING])).\
            first()
    if order:
        order.amount = amount
    else:
        order = Order(
            status = OrderStatus.NEW,
            client_id = client_id,
            product_id = product.id,
            amount = amount,
            paid = False
        )
        session.add(order)
        session.flush()

    return order.id

def reset(session:OrmSession, order_id:int):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    order.status = OrderStatus.NEW
    order.parameter1 = None
    order.parameter2 = None
    order.parameter3 = None

def check_status(session:OrmSession, order_id:int, *statuses) -> bool:

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    return order.status in statuses
     
def check_actual_order(session:OrmSession, order_id:int) -> int:

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    if order.status not in (OrderStatus.NEW, OrderStatus.FILLING):
        clone_order = Order(
            status = OrderStatus.NEW,
            client_id = order.client_id,
            product_id = order.product_id,
            amount = session.query(Tariff.value).filter(Tariff.product_id == order.product_id).scalar(),
            paid = False,
            parameter1 = order.parameter1,
            parameter2 = order.parameter2,
            parameter3 = order.parameter3
        )
        session.add(clone_order)
        session.flush()
        order_id = clone_order.id

    return order_id

def get_orders_by_client(session:OrmSession, client_id:int):
    yield from session.query(Order.id, Order.updated_at, Product.kind, Product.name, Order.amount).\
        join(Product).filter(Order.client_id == client_id).\
            filter(Order.status.in_([OrderStatus.CONFIRMED, OrderStatus.DURING, OrderStatus.COMPLETED])).\
                order_by(Product.kind, Product.name, Order.id)

def mark_as_filling(session:OrmSession, order_id:int):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    last_order_detail = session.query(LastOrderDetailing).filter(LastOrderDetailing.client_id == order.client_id).\
        filter(LastOrderDetailing.handled == False).one_or_none()
    if last_order_detail:
        last_order_detail.handled = True

    order.status = OrderStatus.FILLING

def mark_as_during(session:OrmSession, order_id:int):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    order.status = OrderStatus.DURING

def mark_as_completed(session:OrmSession, order_id:int) -> bool:

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    if order.paid:
        promo_pay_acc = acc_mngr.client_promo_payment_acc(session, order.client_id, order_id)
        promo_pay_acc_amount = acc_util.get_remain_amount(session, promo_pay_acc)

        pay_acc = acc_mngr.client_payment_acc(session, order.client_id, order_id)
        pay_acc_amount = acc_util.get_remain_amount(session, pay_acc)

        if promo_pay_acc_amount >= order.amount:
            acc_util.make_payment(
                session,
                acc_mngr.product_promo_income_acc(session, order_id),
                promo_pay_acc,
                order.amount
            )
        elif promo_pay_acc_amount > 0 and pay_acc_amount >= order.amount - promo_pay_acc_amount:
            acc_util.make_payment(
                session,
                acc_mngr.product_promo_income_acc(session, order_id),
                promo_pay_acc,
                promo_pay_acc_amount
            )
            acc_util.make_payment(
                session,
                acc_mngr.product_income_acc(session, order_id),
                pay_acc,
                order.amount - promo_pay_acc_amount
            )
        elif pay_acc_amount >= order.amount:
            acc_util.make_payment(
                session,
                acc_mngr.product_income_acc(session, order_id),
                pay_acc,
                order.amount
            )
        else:
            return False

    order.status = OrderStatus.COMPLETED

    return True

def mark_as_rejected(session:OrmSession, order_id:int):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    last_order_detail = session.query(LastOrderDetailing).filter(LastOrderDetailing.client_id == order.client_id).\
        filter(LastOrderDetailing.handled == False).one_or_none()
    if last_order_detail:
        last_order_detail.handled = True

    order.status = OrderStatus.REJECTED

def hold_fee(session:OrmSession, order_id:int) -> bool:

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')
    
    if not order.paid and order.amount > 0:
        promo_balance = acc_mngr.promo_balance_by_client(session, order.client_id)
        free_balance = acc_mngr.free_balance_by_client(session, order.client_id)
        if promo_balance >= order.amount:
            acc_util.make_payment(
                session,
                acc_mngr.client_promo_payment_acc(session, order.client_id, order_id),
                acc_mngr.promo_by_client_acc(session, order.client_id),
                order.amount
            )
        elif promo_balance > 0 and free_balance >= order.amount - promo_balance:
            acc_util.make_payment(
                session,
                acc_mngr.client_promo_payment_acc(session, order.client_id, order_id),
                acc_mngr.promo_by_client_acc(session, order.client_id),
                promo_balance
            )
            acc_util.make_payment(
                session,
                acc_mngr.client_payment_acc(session, order.client_id, order_id),
                acc_mngr.free_balance_by_client_acc(session, order.client_id),
                order.amount - promo_balance
            )
        elif free_balance >= order.amount:
            acc_util.make_payment(
                session,
                acc_mngr.client_payment_acc(session, order.client_id, order_id),
                acc_mngr.free_balance_by_client_acc(session, order.client_id),
                order.amount
            )
        else:
            return False
        
        order.paid = True

    order.status = OrderStatus.CONFIRMED

    return True

def get_first_empty_num_parameter_or_none(session:OrmSession, order_id:int) -> int:

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    par_number = None    
    parameters = [p.par_number for p in session.query(ProductAddInfo).filter(ProductAddInfo.product_id == order.product_id)]

    if order.parameter1 is None and 1 in parameters:
        par_number = 1
    elif order.parameter2 is None and 2 in parameters:
        par_number = 2
    elif order.parameter3 is None and 3 in parameters:
        par_number = 3
    else:
        par_number = None

    return par_number

def get_add_info_code(session:OrmSession, order_id:int, par_number:int) -> AddInfoCode:

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')
    
    add_info = session.query(ProductAddInfo).get((order.product_id, par_number))
    if add_info is None:
        raise Error(f'no add_info with this product_id={order.product_id} and par_number={par_number}')

    add_info_settings = session.query(AddInfoSettings).get(add_info.add_info_id)
    if add_info_settings is None:
        raise Error(f'no add_info_settings with this id={add_info.add_info_id}')

    return add_info_settings.code

def update_last_order_detailing(session:OrmSession, client_id:int, order_id:int, par_number:int, add_info_code:AddInfoCode):

    last_order_detail = session.query(LastOrderDetailing).\
        filter(LastOrderDetailing.client_id == client_id).\
            one_or_none()

    if last_order_detail is None:
        last_order_detail = LastOrderDetailing(
            client_id = client_id,
            order_id = order_id,
            par_number = par_number,
            add_info = add_info_code,
            handled = False
        )
        session.add(last_order_detail)
    else:
        last_order_detail.order_id = order_id
        last_order_detail.par_number = par_number
        last_order_detail.add_info = add_info_code
        last_order_detail.handled = False
   
def set_parameter_by_number(session:OrmSession, order_id:int, par_number:int, value:str):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    if par_number == 1:
        order.parameter1 = value
    elif par_number == 2:
        order.parameter2 = value
    elif par_number == 3:
        order.parameter3 = value

def get_product_code(session:OrmSession, order_id:int):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    return order.product.code

def get_parameters(session:OrmSession, order_id:int):

    order = session.query(Order).get(order_id)
    if order is None:
        raise Error(f'no order with this id={order_id}')

    return order.parameter1, order.parameter2, order.parameter3