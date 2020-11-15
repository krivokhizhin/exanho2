from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgOkvedActivitiy(Base):
    __tablename__ = 'nsi_org_okved_activitiy'

    org_id = Column(Integer, ForeignKey('nsi_organization.id'), primary_key=True)
    okved_id = Column(Integer, ForeignKey('nsi_okved.id'), primary_key=True)

    is_main = Column(Boolean, default=False)
    
    org = relationship('NsiOrganization', back_populates='okved_list')
    okved = relationship('NsiOkved', back_populates='org_list')