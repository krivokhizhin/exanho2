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

UniqueConstraint(EisContractLog.source, EisContractLog.doc_id, name='uix_eis_contract_log_source_doc_id')

Index('idx_eis_contract_log_reg_num_publish_dt', EisContractLog.reg_num, EisContractLog.publish_dt.asc())