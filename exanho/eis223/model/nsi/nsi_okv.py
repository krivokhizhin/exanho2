from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOkv(Base):
    __tablename__ = 'nsi_okv'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(3), nullable=False)
    digital_code = Column(String(3), nullable=False)
    name = Column(String(500), nullable=False)
    short_name = Column(String(500))

Index('idx_nsi_okv', NsiOkv.code, NsiOkv.digital_code, unique=True)