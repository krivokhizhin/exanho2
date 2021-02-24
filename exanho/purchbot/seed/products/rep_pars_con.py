from sqlalchemy.orm.session import Session as OrmSession

from exanho.purchbot.model import ProductKind, Product, Tariff

def seed(session:OrmSession):

    product_code = 'REP_PARS_CON'

    product = session.query(Product).filter(Product.code == product_code).one_or_none()
    if product is None:
        product = Product(
            kind = ProductKind.REPORT,
            code = product_code,
            name = 'Опыт исполнения контрактов по всем участникам'
        )
        session.add(product)
        session.flush()

    tariff = session.query(Tariff).filter(Tariff.product == product).one_or_none()
    if tariff is None:
        tariff = Tariff(value = 390)
        tariff.product = product
        session.add(tariff)

    session.flush()