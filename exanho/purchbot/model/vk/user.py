import enum

from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class VkUser(ExaObjectMixin, Base):

    user_id = Column(BigInteger, nullable=False, unique=True, index=True)

    client_id = Column(BigInteger, ForeignKey('client.id'), nullable=False)
    client = relationship('Client', back_populates='vk_users')