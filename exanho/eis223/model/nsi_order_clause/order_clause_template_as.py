from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrderClauseTemplateAs(Base):
    __tablename__ = 'nsi_order_clause_template_association'
    order_clause_id = Column(Integer, ForeignKey('nsi_order_clause.id'), primary_key=True)
    template_id = Column(Integer, ForeignKey('nsi_template_order_clause.id'), primary_key=True)

    order_clause = relationship('NsiOrderClause', back_populates='templates')
    template = relationship('NsiOrderClauseTemplate', back_populates='order_clauses')