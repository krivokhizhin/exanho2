from sqlalchemy import Column, Index, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchPhaseTransitionAs(Base):
    __tablename__ = 'nsi_purch_phase_transition_association'

    id = Column(Integer, primary_key=True)
    phase_id = Column(Integer, ForeignKey('nsi_purchase_phase.id'), nullable=False)
    transition_id = Column(Integer, ForeignKey('nsi_purchase_phase_transition.id'), nullable=False)

    phase = relationship('NsiPurchasePhase', back_populates='transitions')
    transition = relationship('NsiPurchasePhaseTransition', back_populates='phases')

Index('idx_nsi_purch_phase_transition_association', NsiPurchPhaseTransitionAs.phase_id, NsiPurchPhaseTransitionAs.transition_id)