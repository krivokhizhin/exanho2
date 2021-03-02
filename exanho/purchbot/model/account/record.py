from decimal import Decimal

from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class AccRecord(Base):
    __tablename__ = 'acc_record'

    id = Column(BigInteger, primary_key=True)
    
    dt = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)
    cr = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)

    amount = Column(Numeric(18,4), nullable=False)

    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    desc = Column(String(500))
    date = Column(DateTime)

    def __init__(self, dt:int, cr:int, amount:Decimal) -> None:
        self.dt = dt
        self.cr = cr
        self.amount = amount

    def __str__(self) -> str:
        return f'{self.id:>6} | dt {self.dt:>6} | cr {self.cr:>6} | {self.amount:18.2f} | {self.created_at}'