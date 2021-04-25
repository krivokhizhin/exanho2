import enum

from sqlalchemy import BigInteger, Boolean, Column, Enum, Index, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class OrderStatus(enum.Enum):
    NEW = 0
    FILLING = 1
    CONFIRMED = 2
    REJECTED = 3
    DURING = 4 
    COMPLETED = 5

class Order(ExaObjectMixin, Base):

    status = Column(Enum(OrderStatus), nullable=False)

    client_id = Column(BigInteger, ForeignKey('client.id'), nullable=False)
    client = relationship('Client', back_populates='orders')

    product_id = Column(BigInteger, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='orders')

    amount = Column(Numeric(8,2), nullable=False)

    paid = Column(Boolean, nullable=False, default=False)

    parameter1 = Column(String(100))
    parameter2 = Column(String(100))
    parameter3 = Column(String(100))

    subscription = relationship('EventSubscription', uselist=False, back_populates='order', cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.id:>6}: client {self.client_id:>6} | status {self.status.name:<10} | {self.amount:18.2f} | paid={self.paid} | {self.product}'

Index('idx_order_product_status', Order.client_id, Order.product_id, Order.status)