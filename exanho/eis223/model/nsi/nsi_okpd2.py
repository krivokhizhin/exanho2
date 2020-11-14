from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOkpd2(Base):
    __tablename__ = 'nsi_okpd2'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    business_status = Column(String(10), nullable=False)
    code = Column(String(30))
    name = Column(String(500), nullable=False)
    parent_code = Column(String(30))

Index('idx_nsi_okpd2', NsiOkpd2.parent_code, NsiOkpd2.code, unique=True)