from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgSuccessor(Base):
    __tablename__ = 'nsi_org_successor'
    
    id = Column(Integer, primary_key=True)

    org_id = Column(Integer, ForeignKey('nsi_organization.id'), nullable=False)
    org = relationship('NsiOrganization', back_populates='successors')

    inn = Column(String(20), nullable=False)
    ogrn = Column(String(20), nullable=False)
    kpp = Column(String(20), nullable=False)

    full_name = Column(String(1000))
    short_name = Column(String(500))