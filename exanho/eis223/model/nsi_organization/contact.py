from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgContact(Base):
    __tablename__ = 'nsi_org_contact'
    
    id = Column(Integer, primary_key=True)

    org_id = Column(Integer, ForeignKey('nsi_organization.id'), nullable=False, index=True)
    org = relationship('NsiOrganization', back_populates='contact')

    first_name = Column(String(300))
    middle_name = Column(String(300))
    last_name = Column(String(300))
    contact_email = Column(String(300))

    phone = Column(String(300))
    fax = Column(String(300))
    email = Column(String(300))
    website = Column(String(300))
    additional = Column(String(500))