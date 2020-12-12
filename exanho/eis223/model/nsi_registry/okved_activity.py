from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import func, inspect
from sqlalchemy.engine import Connection
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship, Mapper
from sqlalchemy.sql import select

from exanho.orm.domain import Base
from .okved import NsiRegOkved

class NsiRegOkvedActivity(Base):
    __tablename__ = 'nsi_reg_okved_activity'

    customer_id = Column(Integer, ForeignKey('nsi_customer_registry.id'),primary_key=True)
    okved_id = Column(Integer, ForeignKey('nsi_reg_okved.id'),primary_key=True)

    customer = relationship('NsiCustomerRegistry', back_populates='okved_list')
    okved = relationship('NsiRegOkved', back_populates='customers')

@listens_for(NsiRegOkvedActivity, 'after_delete')
def receive_after_delete(mapper:Mapper, connection:Connection, target:NsiRegOkvedActivity):
    if connection.execute(select([func.count()]).select_from(mapper.local_table).where(mapper.local_table.c.okved_id==target.okved_id)) == 0:
        okved_mapper = inspect(NsiRegOkved)
        connection.execute(okved_mapper.local_table.delete().where(okved_mapper.local_table.c.id==target.okved_id))