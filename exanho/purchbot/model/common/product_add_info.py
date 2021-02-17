from sqlalchemy import BigInteger, Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from exanho.orm.domain import Base

class ProductAddInfo(Base):
    __tablename__ = 'product_add_info'

    product_id = Column(BigInteger, ForeignKey('product.id'), primary_key=True)
    add_info_id = Column(BigInteger, ForeignKey('add_info_settings.id'), primary_key=True)

    par_number = Column(Integer, nullable=False)

    add_info = relationship('AddInfoSettings')
