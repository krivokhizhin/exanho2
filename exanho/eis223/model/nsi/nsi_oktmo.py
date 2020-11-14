from sqlalchemy import Column, Date, DateTime, Index, Integer, String
from exanho.orm.domain import Base

class NsiOktmo(Base):
    __tablename__ = 'nsi_oktmo'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(20), nullable=False)
    name = Column(String(500), nullable=False)
    parent_code = Column(String(20))
    okato = Column(String(4000))

Index('idx_nsi_oktmo', NsiOktmo.parent_code, NsiOktmo.code, unique=True)