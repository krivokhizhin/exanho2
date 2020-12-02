from sqlalchemy import BigInteger, Column, Index, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiProtocolPurchMethod(Base):
    __tablename__ = 'nsi_protocol_purch_method'
    
    id = Column(Integer, primary_key=True)
    purch_method_code = Column(BigInteger, nullable=False)
    
    protocol_id = Column(Integer, ForeignKey('nsi_protocol.id'))
    protocol = relationship('NsiProtocol', back_populates='purchase_methods')

Index('idx_nsi_protocol_purch_method', NsiProtocolPurchMethod.protocol_id, NsiProtocolPurchMethod.purch_method_code, unique=True)