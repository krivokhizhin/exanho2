from sqlalchemy import BigInteger, Column, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class Tariff(ExaObjectMixin, Base):

    product_id = Column(BigInteger, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='trades')

    value = Column(Numeric(8,2), nullable=False)

    desc = Column(String(2000))