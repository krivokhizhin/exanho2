import enum

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, Index, String, UniqueConstraint
from exanho.orm.domain import Base

from ..aggregate import EisTableName

class EisContractLog(Base):
    __tablename__ = 'eis_contract_log'    

    id = Column(BigInteger, primary_key=True)

    reg_num = Column(String(30), nullable=False)
    publish_dt = Column(DateTime(timezone=True), nullable=False)

    source = Column(Enum(EisTableName), nullable=False)
    doc_id = Column(BigInteger, nullable=False)

    handled = Column(Boolean, default=False, nullable=False)

Index('idx_eis_contract_log_reg_num', EisContractLog.reg_num)
Index('idx_eis_contract_log_reg_num_not_handled', EisContractLog.reg_num, postgresql_where=EisContractLog.handled==False)
Index('idx_eis_contract_log_source_doc_id', EisContractLog.source, EisContractLog.doc_id, unique=True)
UniqueConstraint(EisContractLog.source, EisContractLog.doc_id, EisContractLog.reg_num, name='uix_eis_contract_log')