from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class AggContractParticipant(Base):
    __tablename__ = 'agg_contract_participant'    

    contract_id = Column(BigInteger, ForeignKey('agg_contract.id'), primary_key=True)
    participant_id = Column(BigInteger, ForeignKey('agg_participant.id'), primary_key=True)

    contract = relationship('AggContract', back_populates='suppliers')
    participant = relationship('AggParticipant', back_populates='contracts')