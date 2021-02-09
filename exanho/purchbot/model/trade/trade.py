import enum

from sqlalchemy import BigInteger, Boolean, Column, Enum, Index, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class TradeStatus(enum.Enum):
    NEW = 0
    FILLING = 1
    CONFIRMED = 2
    REJECTED = 3
    DURING = 4 
    COMPLETED = 5

class Trade(ExaObjectMixin, Base):

    status = Column(Enum(TradeStatus), nullable=False)

    product_id = Column(BigInteger, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='trades')

    client_id = Column(BigInteger, ForeignKey('client.id'), nullable=False)
    client = relationship('Client', back_populates='trades')

    amount = Column(Numeric(8,2), nullable=False)

    paid = Column(Boolean, nullable=False, default=False)

    parameter1 = Column(String(100))
    parameter2 = Column(String(100))
    parameter3 = Column(String(100))

Index('idx_product_status', Trade.product_id, Trade.status)