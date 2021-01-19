import enum

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Enum, Integer, Numeric, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class EisContractState(enum.Enum):
    EXECUTION = 1
    DISCONTINUED = 2
    COMPLETED = 3
    CANCELED = 4

class EisContractKind(enum.Enum):
    FZ44 = 1
    FZ223 = 2

class EisContract(ExaObjectMixin, Base):

    kind = Column(Enum(EisContractKind), nullable=False)
    publish_dt = Column(DateTime(timezone=True))
    reg_num = Column(String(30), nullable=False, unique=True, index=True)
    subject = Column(String(2000))

    price = Column(Numeric(18,2))
    currency_code = Column(String(3))
    right_to_conclude = Column(Boolean, default=False)

    supplier_number = Column(Integer)
    suppliers = relationship('EisContractParticipant', back_populates='contract', cascade='all, delete-orphan')

    href = Column(String(1024))
    
    state = Column(Enum(EisContractState), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)