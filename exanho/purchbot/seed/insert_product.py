from sqlalchemy.orm.session import Session as OrmSession
from exanho.orm.domain import Domain

from exanho.purchbot.model import ProductKind, Product, Tariff

def run():

    d = Domain('postgresql+psycopg2://kks:Nata1311@localhost/purchbot_test')
    with d.session_scope() as session:
        assert isinstance(session, OrmSession)

        product1 = session.query(Product).filter(Product.code == 'QUE_PAR_ACT').one_or_none()
        if product1 is None:
            product1 = Product(
                kind = ProductKind.QUERY,
                code = 'QUE_PAR_ACT',
                name = 'Текущая активность участника'
            )
            session.add(product1)
            session.flush()

        tariff1 = session.query(Tariff).filter(Tariff.product == product1).one_or_none()
        if tariff1 is None:
            tariff1 = Tariff(value = 1)
            tariff1.product = product1
            session.add(tariff1)

        product2 = session.query(Product).filter(Product.code == 'QUE_HIS_ACT').one_or_none()
        if product2 is None:
            product2 = Product(
                kind = ProductKind.QUERY,
                code = 'QUE_HIS_ACT',
                name = 'Опыт участник'
            )
            session.add(product2)
            session.flush()

        tariff2 = session.query(Tariff).filter(Tariff.product == product2).one_or_none()
        if tariff2 is None:
            tariff2 = Tariff(value = 1)
            tariff2.product = product2
            session.add(tariff2)

        product3 = session.query(Product).filter(Product.code == 'SUB_PAR').one_or_none()
        if product3 is None:
            product3 = Product(
                kind = ProductKind.SUBSCRIPTION,
                code = 'SUB_PAR',
                name = 'События по участнику'
            )
            session.add(product3)
            session.flush()

        tariff3 = session.query(Tariff).filter(Tariff.product == product3).one_or_none()
        if tariff3 is None:
            tariff3 = Tariff(value = 5)
            tariff3.product = product3
            session.add(tariff3)

        product4 = session.query(Product).filter(Product.code == 'REP_CON_PAR').one_or_none()
        if product4 is None:
            product4 = Product(
                kind = ProductKind.REPORT,
                code = 'REP_CON_PAR',
                name = 'Опыт исполнения контрактов по всем участникам'
            )
            session.add(product4)
            session.flush()

        tariff4 = session.query(Tariff).filter(Tariff.product == product4).one_or_none()
        if tariff4 is None:
            tariff4 = Tariff(value = 1000)
            tariff4.product = product4
            session.add(tariff4)