from sqlalchemy import BigInteger, Column, ForeignKey, String

from exanho.orm.domain import Base

class VkProductContent(Base):
    __tablename__ = 'vk_product_content'

    id = Column(BigInteger, primary_key=True)

    product_id = Column(BigInteger, ForeignKey('product.id'), nullable=False, unique=True, index=True)

    list_desc  = Column(String(200))
    list_button = Column(String(200))
