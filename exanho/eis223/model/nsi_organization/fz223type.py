from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgFz223type(Base):
    __tablename__ = 'nsi_org_fz223type'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(2000), nullable=False)

    org_list = relationship('NsiOrgFz223typeAs', back_populates='fz223type', cascade='all, delete-orphan')