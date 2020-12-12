from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiRegIkul(Base):
    __tablename__ = 'nsi_reg_ikul'
    
    id = Column(Integer, primary_key=True)

    customer_registry_id = Column(ForeignKey('nsi_customer_registry.id'), nullable=False, index=True)
    customer_registry = relationship('NsiCustomerRegistry', back_populates='ikuls')

    code = Column(String(100), nullable=False)
    name = Column(String(255), nullable=False)
    assignment_dt = Column(DateTime(timezone=True))

    org_list = relationship('NsiOrgOkvedActivity', back_populates='okved', cascade='all, delete-orphan')