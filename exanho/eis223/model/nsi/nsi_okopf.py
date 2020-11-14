from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOkopf(Base):
    __tablename__ = 'nsi_okopf'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(10), nullable=False)
    name = Column(String(200), nullable=False)
    parent_code = Column(String(10))

Index('idx_nsi_okopf', NsiOkopf.parent_code, NsiOkopf.code, unique=True)