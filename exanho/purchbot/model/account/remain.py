from sqlalchemy import BigInteger, Column, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class AccRemain(ExaObjectMixin, Base):

    account_id = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False, unique=True, index=True)
    account = relationship('AccAccount', back_populates='remain')

    dt = Column(Numeric(18,4), nullable=False)
    cr = Column(Numeric(18,4), nullable=False)

    def __init__(self, account) -> None:
        self.account = account
        self.dt = 0
        self.cr = 0
        self.last_payment_id = None

    def __str__(self):
        balance = self.dt-self.cr
        return f'{self.account_id:>10} | dt {self.dt:18.2f} | cr {self.cr:18.2f} | dt-cr {balance:18.2f}'