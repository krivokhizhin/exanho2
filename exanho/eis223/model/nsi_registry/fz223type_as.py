from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class NsiRegClassificationFz223type(Base):
    __tablename__ = 'nsi_reg_classification_fz223type'

    customer_id = Column(Integer, ForeignKey('nsi_customer_registry.id'), primary_key=True)
    fz223type_id = Column(Integer, ForeignKey('nsi_fz223type.id'), primary_key=True)

    customer = relationship('NsiCustomerRegistry', back_populates='fz223types')
    fz223type = relationship('NsiFz223type', back_populates='customers')