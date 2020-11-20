from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOkved(Base):
    __tablename__ = 'nsi_okved'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(10), nullable=False)
    name = Column(String(500), nullable=False)
    parent_code = Column(String(10))
    section = Column(String(1), nullable=False)
    subsection = Column(String(2))

Index('idx_nsi_okved_code', NsiOkved.code, NsiOkved.business_status, unique=True)
Index('idx_nsi_okved', NsiOkved.subsection, NsiOkved.section, NsiOkved.parent_code, NsiOkved.code, unique=True)