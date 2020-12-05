from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrderClause(Base):
    __tablename__ = 'nsi_order_clause'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    business_status = Column(String(10), nullable=False)
    name = Column(String(2000), nullable=False)
    order_number = Column(Integer, nullable=False)
    
    creator_inn = Column(String(20))
    creator_kpp = Column(String(20))
    creator_ogrn = Column(String(20))

    templates = relationship('NsiOrderClauseTemplateAs', back_populates='order_clause', cascade='all, delete-orphan')

Index('idx_nsi_order_clause_inn_kpp_order', NsiOrderClause.creator_inn, NsiOrderClause.creator_kpp, NsiOrderClause.order_number, unique=True)
Index('idx_nsi_order_clause_ogrn_inn_kpp_order', NsiOrderClause.creator_ogrn, NsiOrderClause.creator_inn, NsiOrderClause.creator_kpp, NsiOrderClause.order_number, unique=True)