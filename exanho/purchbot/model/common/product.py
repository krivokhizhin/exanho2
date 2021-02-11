import enum

from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class ProductKind(enum.Enum):
    QUERY = 0
    SUBSCRIPTION = 1
    REPORT = 2

class Product(ExaObjectMixin, Base):

    kind = Column(Enum(ProductKind), nullable=False)
    code = Column(String(30), nullable=False, unique=True, index=True)
    name = Column(String(200), nullable=False)
    desc = Column(String(2000))

    trades = relationship('Trade', back_populates='product')
    tariff = relationship('Tariff', back_populates='product', uselist=False)