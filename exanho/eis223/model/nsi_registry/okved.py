from sqlalchemy import Boolean, Column, Integer, Index, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiRegOkved(Base):
    __tablename__ = 'nsi_reg_okved'
    
    id = Column(Integer, primary_key=True)

    code = Column(String(10), nullable=False)
    is_main = Column(Boolean, default=False, nullable=False)
    name = Column(String(500), nullable=False)

    customers = relationship('NsiRegOkvedActivity', back_populates='okved', cascade='all, delete-orphan')

Index('idx_reg_okved_code_name_is_main', NsiRegOkved.code, NsiRegOkved.name, NsiRegOkved.is_main, unique = True)