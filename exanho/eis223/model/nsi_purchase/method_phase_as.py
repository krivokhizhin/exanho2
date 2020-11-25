from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchMethodPhaseAs(Base):
    __tablename__ = 'nsi_purch_method_phase_association'
    method_id = Column(Integer, ForeignKey('nsi_purchase_method.id'), primary_key=True)
    phase_id = Column(Integer, ForeignKey('nsi_purchase_phase.id'), primary_key=True)

    method = relationship('NsiPurchaseMethod', back_populates='phases')
    phase = relationship('NsiPurchasePhase', back_populates='methods')