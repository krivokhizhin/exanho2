from sqlalchemy import BigInteger, Column, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchaseProtocol(Base):
    __tablename__ = 'nsi_purchase_protocol'
    
    id = Column(Integer, primary_key=True)
    code = Column(BigInteger, nullable=False, index=True, unique=True)
    name = Column(String(2000), nullable=False)

    methods = relationship('NsiPurchMethodProtocolAs', back_populates='protocol', cascade='all, delete-orphan')
    phases = relationship('NsiPurchPhaseProtocolAs', back_populates='protocol', cascade='all, delete-orphan')