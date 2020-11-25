from sqlalchemy import BigInteger, Column, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchasePhaseTransition(Base):
    __tablename__ = 'nsi_purchase_phase_transition'
    
    id = Column(Integer, primary_key=True)
    protocol_code = Column(BigInteger, nullable=False)
    phase_code = Column(BigInteger, nullable=False)

    phases = relationship('NsiPurchPhaseTransitionAs', back_populates='transition', cascade='all, delete-orphan')

Index('idx_purch_phase_transition', NsiPurchasePhaseTransition.protocol_code, NsiPurchasePhaseTransition.phase_code, unique=True)