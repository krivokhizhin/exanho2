from sqlalchemy import Column, ForeignKey, Integer, String, Table
from exanho.orm.domain import Base

nsi_org_fz223type_association_table = Table('nsi_org_fz223type_association', Base.metadata,
    Column('org_id', Integer, ForeignKey('nsi_organization.id')),
    Column('fz223type_id', Integer, ForeignKey('nsi_org_fz223type.id'))
)

class NsiOrgFz223type(Base):
    __tablename__ = 'nsi_org_fz223type'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(2000), nullable=False)