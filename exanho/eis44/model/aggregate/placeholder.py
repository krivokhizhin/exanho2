import enum
from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, Enum

from exanho.orm.domain import Base

class EisTableName(enum.Enum):
    zfcs_contract2015 = 1
    zfcs_contract_procedure2015 = 2
    zfcs_contract_procedure_cancel2015 = 3

class LogPlaceholder(Base):
    __tablename__ = 'log_placeholder'  

    id = Column(BigInteger, primary_key=True)

    source_table = Column(Enum(EisTableName), nullable=False, unique=True)
    last_id = Column(BigInteger, default=-1, nullable=False)
    last_dt = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now, nullable=False)