from sqlalchemy.orm.session import Session as OrmSession
from exanho.orm.domain import Domain

from exanho.purchbot.model import ProductKind, Product, Tariff, VkProductContent, AddInfoCode, AddInfoSettings, ProductAddInfo

def seed(session:OrmSession):

    product_code = 'REP_PAR_ACT'

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

    add_info = session.query(AddInfoSettings).filter(AddInfoSettings.code == AddInfoCode.PARTICIPANT).one()
    if add_info not in [info.add_info for info in product.add_infos]:
        product_add_info = ProductAddInfo(
            product_id = product.id,
            add_info_id = add_info.id,
            par_number = 1
        )
        product.add_infos.append(product_add_info)

    session.flush()