import enum

from sqlalchemy import BigInteger, Boolean, Column, Date
from sqlalchemy.sql.schema import ForeignKey

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class Subscription(ExaObjectMixin, Base):

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    order_id = Column(BigInteger, ForeignKey('order.id'), nullable=False)