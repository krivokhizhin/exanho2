from sqlalchemy import BigInteger, Boolean, Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

from exanho.purchbot.model.common.add_info import AddInfoCode

class LastTradeDetailing(ExaObjectMixin, Base):

    client_id = Column(BigInteger, ForeignKey('client.id'), nullable=False, index=True, unique=True)
    client = relationship('Client')

    trade_id = Column(BigInteger, ForeignKey('trade.id'), nullable=False)
    trade = relationship('Trade')

    add_info = Column(Enum(AddInfoCode), nullable=False)
    par_number = Column(Integer, nullable=False)

    handled = Column(Boolean, nullable=False, default=False)