from sqlalchemy import Column, Index, Integer, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class CntrContact(Base):
    __tablename__ = 'cntr_contact'
    
    id = Column(Integer, primary_key=True)

    suppliers = relationship('ZfcsContract2015Supplier', back_populates='contact')

    last_name = Column(String(50))
    first_name = Column(String(50))
    middle_name = Column(String(50))

Index('ix_cntr_contact_fio', CntrContact.last_name, CntrContact.first_name, CntrContact.middle_name, unique=True)