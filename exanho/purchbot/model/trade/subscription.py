from sqlalchemy import BigInteger, Boolean, Column, Date, ForeignKey, Index

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class Subscription(ExaObjectMixin, Base):

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    order_id = Column(BigInteger, ForeignKey('order.id'), nullable=False, index=True)

    # last_event_id = Column(BigInteger)

Index('idx_subscription_order_id_active', Subscription.order_id, postgresql_where=Subscription.active==True)