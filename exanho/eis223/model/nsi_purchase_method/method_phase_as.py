from sqlalchemy import Column, Index, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchMethodPhaseAs(Base):
    __tablename__ = 'nsi_purch_method_phase_association'

    id = Column(Integer, primary_key=True)
    method_id = Column(Integer, ForeignKey('nsi_purchase_method.id'), nullable=False)
    phase_id = Column(Integer, ForeignKey('nsi_purchase_phase.id'), nullable=False)

    method = relationship('NsiPurchaseMethod', back_populates='phases')
    phase = relationship('NsiPurchasePhase', back_populates='methods')

Index('idx_nsi_purch_method_phase_association', NsiPurchMethodPhaseAs.method_id, NsiPurchMethodPhaseAs.phase_id)