from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class EisContractParticipant(Base):
    __tablename__ = 'eis_contract_participant'    

    contract_id = Column(BigInteger, ForeignKey('eis_contract.id'), primary_key=True)
    participant_id = Column(BigInteger, ForeignKey('eis_participant.id'), primary_key=True)

    contract = relationship('EisContract', back_populates='suppliers')
    participant = relationship('EisParticipant', back_populates='contracts')