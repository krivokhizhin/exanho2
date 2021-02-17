from sqlalchemy.orm.session import Session as OrmSession
from exanho.orm.domain import Domain

from exanho.purchbot.model import ProductKind, Product, Tariff, VkProductContent

def run():

    product_code = 'REP_PAR_ACT'

    d = Domain('postgresql+psycopg2://kks:Nata1311@localhost/purchbot_test')
    with d.session_scope() as session:
        assert isinstance(session, OrmSession)

        product = session.query(Product).filter(Product.code == product_code).one_or_none()
        if product is None:
            product = Product(
                kind = ProductKind.REPORT,
                code = product_code,
                name = 'Текущая активность участника'
            )
            session.add(product)
            session.flush()

        tariff = session.query(Tariff).filter(Tariff.product == product).one_or_none()
        if tariff is None:
            tariff = Tariff(value = 4)
            tariff.product = product
            session.add(tariff)

        vk_content = session.query(VkProductContent).filter(VkProductContent.product_id == product.id).one_or_none()
        if vk_content is None:
            vk_content = VkProductContent(
                product_id = product.id,
                list_desc='Потребуется указать ИНН и КПП (при наличии) участника',
                list_button='Получить'
            )
            session.add(vk_content)