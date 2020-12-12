from sqlalchemy import Boolean, Column, Integer, Index, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiRegOkved2(Base):
    __tablename__ = 'nsi_reg_okved2'
    
    id = Column(Integer, primary_key=True)

    code = Column(String(10), nullable=False)
    is_main = Column(Boolean, default=False, nullable=False)
    name = Column(String(500), nullable=False)

    customers = relationship('NsiRegOkved2Activity', back_populates='okved2', cascade='all, delete-orphan')

Index('idx_reg_okved2_code_name_is_main', NsiRegOkved2.code, NsiRegOkved2.name, NsiRegOkved2.is_main, unique = True)