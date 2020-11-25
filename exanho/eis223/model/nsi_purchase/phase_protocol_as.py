from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchPhaseProtocolAs(Base):
    __tablename__ = 'nsi_purch_phase_protocol_association'
    phase_id = Column(Integer, ForeignKey('nsi_purchase_phase.id'), primary_key=True)
    protocol_id = Column(Integer, ForeignKey('nsi_purchase_protocol.id'), primary_key=True)

    phase = relationship('NsiPurchasePhase', back_populates='protocols')
    protocol = relationship('NsiPurchaseProtocol', back_populates='phases')