from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchMethodProtocolAs(Base):
    __tablename__ = 'nsi_purch_method_protocol_association'
    method_id = Column(Integer, ForeignKey('nsi_purchase_method.id'), primary_key=True)
    protocol_id = Column(Integer, ForeignKey('nsi_purchase_protocol.id'), primary_key=True)

    method = relationship('NsiPurchaseMethod', back_populates='protocols')
    protocol = relationship('NsiPurchaseProtocol', back_populates='methods')