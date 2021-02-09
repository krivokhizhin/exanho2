from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class AccRecord(Base):
    __tablename__ = 'acc_record'  

    id = Column(BigInteger, primary_key=True)

    dt = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)
    cr = Column(BigInteger, ForeignKey('acc_account.id'), nullable=False)

    amount = Column(Numeric(18,4), nullable=False)

    desc = Column(String(500))
    date = Column(DateTime)