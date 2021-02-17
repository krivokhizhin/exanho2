from sqlalchemy.orm.session import Session as OrmSession

from exanho.purchbot.model import ProductKind, Product, Tariff, VkProductContent

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

    vk_content = session.query(VkProductContent).filter(VkProductContent.product_id == product.id).one_or_none()
    if vk_content is None:
        vk_content = VkProductContent(
            product_id = product.id,
            list_desc='+ учет незавершенных контрактов',
            list_button='Получить'
        )
        session.add(vk_content)

    session.flush()