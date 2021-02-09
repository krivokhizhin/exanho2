from sqlalchemy import BigInteger, Column, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class AccRemain(ExaObjectMixin, Base):

    account_id = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)
    account = relationship('AccAccount', back_populates='remain')

    dt = Column(Numeric(18,4), nullable=False)
    cr = Column(Numeric(18,4), nullable=False)
    
    last_payment_id = Column(BigInteger, ForeignKey('acc_record.id'))