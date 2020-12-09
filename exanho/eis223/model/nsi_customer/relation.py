from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiAgencyRelation(Base):
    __tablename__ = 'nsi_agency_relation'
    
    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey('customer_main_info.id'), nullable=False, index=True)
    customer = relationship('CustomerMainInfo', foreign_keys=[customer_id], back_populates='relations')

    agency_id = Column(Integer, ForeignKey('customer_main_info.id'), nullable=False, index=True)
    agency = relationship('CustomerMainInfo', foreign_keys=[agency_id], back_populates='agency_relations')

    relation_type = Column(String(4), nullable=False)
    status = Column(String(40), nullable=False)
    create_dt = Column(DateTime(timezone=True), nullable=False)
    update_dt = Column(DateTime(timezone=True), nullable=False)
    comment = Column(String(2000))