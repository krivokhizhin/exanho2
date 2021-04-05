import enum

from sqlalchemy import BigInteger, Column, Enum, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class ProductKind(enum.Enum):
    QUERY = 0
    SUBSCRIPTION = 1
    REPORT = 2

class Product(Base):
    __tablename__ = 'product'  

    id = Column(BigInteger, primary_key=True)

    kind = Column(Enum(ProductKind), nullable=False)
    code = Column(String(30), nullable=False, unique=True, index=True)
    name = Column(String(200), nullable=False)
    desc = Column(String(2000))

    add_infos = relationship('ProductAddInfo')
    tariff = relationship('Tariff', back_populates='product', uselist=False)
    
    orders = relationship('Order', back_populates='product')

    def __str__(self) -> str:
        return f'{self.kind.name:>12} | {self.code:>10}'