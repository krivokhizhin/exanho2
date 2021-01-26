import enum

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, Index, String, UniqueConstraint
from exanho.orm.domain import Base

from ..aggregate import EisTableName

class EisParticipantLog(Base):
    __tablename__ = 'eis_participant_log'    

    id = Column(BigInteger, primary_key=True)

    inn = Column(String(12), nullable=False)
    kpp = Column(String(9))
    publish_dt = Column(DateTime(timezone=True), nullable=False)

    source = Column(Enum(EisTableName), nullable=False)
    doc_id = Column(BigInteger, nullable=False)

    handled = Column(Boolean, default=False, nullable=False)

Index('idx_eis_participant_log_inn_kpp', EisParticipantLog.inn, EisParticipantLog.kpp, EisParticipantLog.publish_dt.asc())
Index('idx_eis_participant_log_source_doc_id', EisParticipantLog.source, EisParticipantLog.doc_id)
UniqueConstraint(EisParticipantLog.source, EisParticipantLog.doc_id, EisParticipantLog.inn, EisParticipantLog.kpp, name='uix_eis_participant_log')