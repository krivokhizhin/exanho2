from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiFz223type(Base):
    __tablename__ = 'nsi_fz223type'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(30), nullable=False, index=True, unique=True)
    name = Column(String(2000), nullable=False)

    customers = relationship('NsiRegClassificationFz223type', back_populates='fz223type', cascade='all, delete-orphan')