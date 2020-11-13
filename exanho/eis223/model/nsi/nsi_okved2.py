from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOkved2(Base):
    __tablename__ = 'nsi_okved2'
    
    id = Column(Integer, primary_key=True)
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(10), nullable=False)
    name = Column(String(500), nullable=False)
    parent_code = Column(String(10))
    section = Column(String(1), nullable=False)

Index('idx_nsi_okved2', NsiOkved2.section, NsiOkved2.parent_code, NsiOkved2.code, unique=True)