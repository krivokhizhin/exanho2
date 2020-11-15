from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgOkved2Activitiy(Base):
    __tablename__ = 'nsi_org_okved2_activitiy'

    org_id = Column(Integer, ForeignKey('nsi_organization.id'), primary_key=True)
    okved2_id = Column(Integer, ForeignKey('nsi_okved2.id'), primary_key=True)

    is_main = Column(Boolean, default=False)
    
    org = relationship('NsiOrganization', back_populates='okved2_list')
    okved2 = relationship('NsiOkved2', back_populates='org_list')