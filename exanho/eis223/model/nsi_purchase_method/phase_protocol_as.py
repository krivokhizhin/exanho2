from sqlalchemy import Column, Index, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchPhaseProtocolAs(Base):
    __tablename__ = 'nsi_purch_phase_protocol_association'

    id = Column(Integer, primary_key=True)
    phase_id = Column(Integer, ForeignKey('nsi_purchase_phase.id'), nullable=False)
    protocol_id = Column(Integer, ForeignKey('nsi_purchase_protocol.id'), nullable=False)

    phase = relationship('NsiPurchasePhase', back_populates='protocols')
    protocol = relationship('NsiPurchaseProtocol', back_populates='phases')

Index('idx_nsi_purch_phase_protocol_association', NsiPurchPhaseProtocolAs.phase_id, NsiPurchPhaseProtocolAs.protocol_id)