from sqlalchemy import Boolean, Column, Integer, Index, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgOkved2(Base):
    __tablename__ = 'nsi_org_okved2'
    
    id = Column(Integer, primary_key=True)

    code = Column(String(10), nullable=False)
    is_main = Column(Boolean, default=False)
    name = Column(String(500), nullable=False)

    org_list = relationship('NsiOrgOkved2Activity', back_populates='okved2', cascade='all, delete-orphan')

Index('idx_okved2_code_name_is_main', NsiOrgOkved2.code, NsiOrgOkved2.name, NsiOrgOkved2.is_main, unique = True)