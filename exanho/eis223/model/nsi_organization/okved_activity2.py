from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import func, inspect
from sqlalchemy.engine import Connection
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship, Mapper
from sqlalchemy.sql import select

from exanho.orm.domain import Base
from .okved2 import NsiOrgOkved2

class NsiOrgOkved2Activity(Base):
    __tablename__ = 'nsi_org_okved2_activity'

    org_id = Column(Integer, ForeignKey('nsi_organization.id'),primary_key=True)
    okved2_id = Column(Integer, ForeignKey('nsi_org_okved2.id'),primary_key=True)

    org = relationship('NsiOrganization', back_populates='okved2_list')
    okved2 = relationship('NsiOrgOkved2', back_populates='org_list')

@listens_for(NsiOrgOkved2Activity, 'after_delete')
def receive_after_delete(mapper:Mapper, connection:Connection, target:NsiOrgOkved2Activity):
    if connection.execute(select([func.count()]).select_from(mapper.local_table).where(mapper.local_table.c.okved2_id==target.okved2_id)) == 0:
        okved2_mapper = inspect(NsiOrgOkved2)
        connection.execute(okved2_mapper.local_table.delete().where(okved2_mapper.local_table.c.id==target.okved2_id))