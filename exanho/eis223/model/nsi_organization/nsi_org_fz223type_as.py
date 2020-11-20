from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import func, inspect
from sqlalchemy.engine import Connection
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship, Mapper
from sqlalchemy.sql import select

from exanho.orm.domain import Base
from . import NsiOrgFz223type

class NsiOrgFz223typeAs(Base):
    __tablename__ = 'nsi_org_fz223type_association'

    org_id = Column(Integer, ForeignKey('nsi_organization.id'), primary_key=True)
    fz223type_id = Column(Integer, ForeignKey('nsi_org_fz223type.id'), primary_key=True)

    org = relationship('NsiOrganization', back_populates='fz223types')
    fz223type = relationship('NsiOrgFz223type', back_populates='org_list')

@listens_for(NsiOrgFz223typeAs, 'after_delete')
def receive_after_delete(mapper:Mapper, connection:Connection, target:NsiOrgFz223typeAs):
    if connection.execute(select([func.count()]).select_from(mapper.local_table).where(mapper.local_table.c.fz223type_id==target.fz223type_id)) == 0:
        fz223type_mapper = inspect(NsiOrgFz223type)
        connection.execute(fz223type_mapper.local_table.delete().where(fz223type_mapper.local_table.c.id==target.fz223type_id))