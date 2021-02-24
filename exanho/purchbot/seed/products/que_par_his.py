from sqlalchemy.orm.session import Session as OrmSession

from exanho.purchbot.model import ProductKind, Product, Tariff, AddInfoCode, AddInfoSettings, ProductAddInfo

def seed(session:OrmSession):

    product_code = 'QUE_PAR_HIS'

    product = session.query(Product).filter(Product.code == product_code).one_or_none()
    if product is None:
        product = Product(
            kind = ProductKind.QUERY,
            code = product_code,
            name = 'Опыт участника'
        )
        session.add(product)
        session.flush()

    tariff = session.query(Tariff).filter(Tariff.product == product).one_or_none()
    if tariff is None:
        tariff = Tariff(value = 1)
        tariff.product = product
        session.add(tariff)

    add_info = session.query(AddInfoSettings).filter(AddInfoSettings.code == AddInfoCode.PARTICIPANT).one()
    if add_info not in [info.add_info for info in product.add_infos]:
        product_add_info = ProductAddInfo(
            product_id = product.id,
            add_info_id = add_info.id,
            par_number = 1
        )
        product.add_infos.append(product_add_info)

    session.flush()