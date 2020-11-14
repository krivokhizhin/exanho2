from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOkfs(Base):
    __tablename__ = 'nsi_okfs'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(4), nullable=False)
    name = Column(String(500), nullable=False)
    parent_code = Column(String(4))

Index('idx_nsi_okfs', NsiOkfs.parent_code, NsiOkfs.code, unique=True)