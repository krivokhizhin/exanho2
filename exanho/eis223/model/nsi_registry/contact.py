from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiRegContact(Base):
    __tablename__ = 'nsi_reg_contact'
    
    id = Column(Integer, primary_key=True)

    customer_registry_id = Column(Integer, ForeignKey('nsi_customer_registry.id'), nullable=False, index=True)
    customer_registry = relationship('NsiCustomerRegistry', back_populates='contact')

    first_name = Column(String(300))
    middle_name = Column(String(300))
    last_name = Column(String(300))

    phone = Column(String(300))
    fax = Column(String(300))
    email = Column(String(300))

    additional = Column(String(2000))