from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiProtocol(Base):
    __tablename__ = 'nsi_protocol'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    create_dt = Column(DateTime(timezone=True), nullable=False)
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(BigInteger, nullable=False, index=True, unique=True)
    name = Column(String(2000), nullable=False)
    order_number = Column(Integer, nullable=False)

    purchase_methods = relationship('NsiProtocolPurchMethod', back_populates='protocol', cascade='all, delete-orphan')

    extended = Column(Boolean)

    templates = relationship('NsiProtocolTemplateAs', back_populates='protocol', cascade='all, delete-orphan')

    protocol_kind = Column(String(20))
    lot_oriented = Column(Boolean, nullable=False)