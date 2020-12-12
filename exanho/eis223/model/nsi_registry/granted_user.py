from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiRegGrantedUser(Base):
    __tablename__ = 'nsi_reg_granted_user'
    
    id = Column(Integer, primary_key=True)

    customer_registry_id = Column(Integer, ForeignKey('nsi_customer_registry.id'), nullable=False, index=True)
    customer_registry = relationship('NsiCustomerRegistry', back_populates='contact')

    first_name = Column(String(300), nullable=False)
    middle_name = Column(String(300), nullable=False)
    last_name = Column(String(300), nullable=False)

    inn = Column(String(20), nullable=False)
    position = Column(String(2000), nullable=False)