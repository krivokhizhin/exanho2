from sqlalchemy import BigInteger, Boolean, Column, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchasePhase(Base):
    __tablename__ = 'nsi_purchase_phase'
    
    id = Column(Integer, primary_key=True)
    order_number = Column(Integer, nullable=False)
    code = Column(BigInteger, nullable=False)
    name = Column(String(200), nullable=False)
    edit_enabled = Column(Boolean, nullable=False)

    protocols = relationship('NsiPurchPhaseProtocolAs', back_populates='phase', cascade='all, delete-orphan')
    transitions = relationship('NsiPurchPhaseTransitionAs', back_populates='phase', cascade='all, delete-orphan')

    methods = relationship('NsiPurchMethodPhaseAs', back_populates='phase', cascade='all, delete-orphan')

Index('idx_purch_phase', NsiPurchasePhase.code)