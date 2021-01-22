import enum

from sqlalchemy import Boolean, Column, Date, DateTime, Enum, Integer, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class AggContractState(enum.Enum):
    UNKNOWN = 0
    EXECUTION = 1
    DISCONTINUED = 2
    COMPLETED = 3
    CANCELED = 4

class AggContract(ExaObjectMixin, Base):

    publish_dt = Column(DateTime(timezone=True))
    reg_num = Column(String(30), nullable=False, unique=True, index=True)
    subject = Column(String(2000))

    price = Column(Numeric(18,2))
    currency_code = Column(String(3))
    right_to_conclude = Column(Boolean, default=False)

    supplier_number = Column(Integer)
    suppliers = relationship('AggContractParticipant', back_populates='contract', cascade='all, delete-orphan')

    href = Column(String(1024))
    
    state = Column(Enum(AggContractState), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)