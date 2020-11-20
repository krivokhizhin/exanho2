from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import func, inspect
from sqlalchemy.engine import Connection
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship, Mapper
from sqlalchemy.sql import select

from exanho.orm.domain import Base
from .okved import NsiOrgOkved

class NsiOrgOkvedActivity(Base):
    __tablename__ = 'nsi_org_okved_activity'

    org_id = Column(Integer, ForeignKey('nsi_organization.id'),primary_key=True)
    okved_id = Column(Integer, ForeignKey('nsi_org_okved.id'),primary_key=True)

    org = relationship('NsiOrganization', back_populates='okved_list')
    okved = relationship('NsiOrgOkved', back_populates='org_list')

@listens_for(NsiOrgOkvedActivity, 'after_delete')
def receive_after_delete(mapper:Mapper, connection:Connection, target:NsiOrgOkvedActivity):
    if connection.execute(select([func.count()]).select_from(mapper.local_table).where(mapper.local_table.c.okved_id==target.okved_id)) == 0:
        okved_mapper = inspect(NsiOrgOkved)
        connection.execute(okved_mapper.local_table.delete().where(okved_mapper.local_table.c.id==target.okved_id))