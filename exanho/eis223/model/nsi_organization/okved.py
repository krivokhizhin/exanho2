from sqlalchemy import Boolean, Column, Integer, Index, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgOkved(Base):
    __tablename__ = 'nsi_org_okved'
    
    id = Column(Integer, primary_key=True)

    code = Column(String(10), nullable=False)
    is_main = Column(Boolean, default=False)
    name = Column(String(500), nullable=False)

    org_list = relationship('NsiOrgOkvedActivity', back_populates='okved', cascade='all, delete-orphan')

Index('idx_okved_code_name_is_main', NsiOrgOkved.code, NsiOrgOkved.name, NsiOrgOkved.is_main, unique = True)