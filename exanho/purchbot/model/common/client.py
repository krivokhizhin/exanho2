from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class Client(ExaObjectMixin, Base):

    desc = Column(String(1000))

    vk_users = relationship('VkUser', back_populates='client')
    orders = relationship('Order', back_populates='client')