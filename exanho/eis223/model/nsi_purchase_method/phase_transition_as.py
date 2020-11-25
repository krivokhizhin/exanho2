from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchPhaseTransitionAs(Base):
    __tablename__ = 'nsi_purch_phase_transition_association'
    phase_id = Column(Integer, ForeignKey('nsi_purchase_phase.id'), primary_key=True)
    transition_id = Column(Integer, ForeignKey('nsi_purchase_phase_transition.id'), primary_key=True)

    phase = relationship('NsiPurchasePhase', back_populates='transitions')
    transition = relationship('NsiPurchasePhaseTransition', back_populates='phases')