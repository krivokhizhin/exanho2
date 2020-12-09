from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, String
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

    creator_id = Column(Integer, ForeignKey('customer_main_info.id'), index=True)
    creator = relationship('CustomerMainInfo', back_populates='order_clauses')

    templates = relationship('NsiOrderClauseTemplateAs', back_populates='order_clause', cascade='all, delete-orphan')