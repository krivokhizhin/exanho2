from decimal import Decimal

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class AccRecord(ExaObjectMixin, Base):
    __tablename__ = 'acc_record'

    dt = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)
    cr = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)

    amount = Column(Numeric(18,4), nullable=False)

    desc = Column(String(500))
    date = Column(DateTime)

    def __init__(self, dt:int, cr:int, amount:Decimal) -> None:
        self.dt = dt
        self.cr = cr
        self.amount = amount