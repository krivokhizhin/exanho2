from sqlalchemy import BigInteger, Boolean, Column, Date, ForeignKey, Index
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class EventSubscription(ExaObjectMixin, Base):

    last_date = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    
    order_id = Column(BigInteger, ForeignKey('order.id'), nullable=False, index=True)
    order = relationship('Order', back_populates='subscription')

    last_event_id = Column(BigInteger)

Index('idx_subscription_order_id_active', EventSubscription.order_id, postgresql_where=EventSubscription.active==True)