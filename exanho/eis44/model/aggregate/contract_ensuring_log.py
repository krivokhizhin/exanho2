from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, Index, String, UniqueConstraint
from exanho.orm.domain import Base

from ..aggregate import EisTableName

class EisContractEnsuringLog(Base):
    __tablename__ = 'eis_contract_ensuring_log'    

    id = Column(BigInteger, primary_key=True)

    reg_num = Column(String(30), nullable=False)
    publish_dt = Column(DateTime(timezone=True), nullable=False)

    source = Column(Enum(EisTableName), nullable=False)
    doc_id = Column(BigInteger, nullable=False)

    handled = Column(Boolean, default=False, nullable=False)

Index('idx_eis_contract_ensuring_log_reg_num_publish_dt', EisContractEnsuringLog.reg_num, EisContractEnsuringLog.publish_dt.asc())
Index('idx_eis_contract_ensuring_log_source_doc_id', EisContractEnsuringLog.source, EisContractEnsuringLog.doc_id, unique=True)
UniqueConstraint(EisContractEnsuringLog.source, EisContractEnsuringLog.doc_id, EisContractEnsuringLog.reg_num, name='uix_eis_contract_ensuring_log')