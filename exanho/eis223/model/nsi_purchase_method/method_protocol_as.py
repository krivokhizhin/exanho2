from sqlalchemy import Column, Index, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchMethodProtocolAs(Base):
    __tablename__ = 'nsi_purch_method_protocol_association'

    id = Column(Integer, primary_key=True)
    method_id = Column(Integer, ForeignKey('nsi_purchase_method.id'), nullable=False)
    protocol_id = Column(Integer, ForeignKey('nsi_purchase_protocol.id'), nullable=False)

    method = relationship('NsiPurchaseMethod', back_populates='protocols')
    protocol = relationship('NsiPurchaseProtocol', back_populates='methods')

Index('idx_nsi_purch_method_protocol_association', NsiPurchMethodProtocolAs.method_id, NsiPurchMethodProtocolAs.protocol_id)