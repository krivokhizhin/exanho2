from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgFz223typeAs(Base):
    __tablename__ = 'nsi_org_fz223type_association'

    org_id = Column(Integer, ForeignKey('nsi_organization.id'), primary_key=True)
    fz223type_id = Column(Integer, ForeignKey('nsi_org_fz223type.id'), primary_key=True)

    org = relationship('NsiOrganization', back_populates='fz223types')
    fz223type = relationship('NsiOrgFz223type', back_populates='org_list')