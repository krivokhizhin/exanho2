from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .. import NsiTemplateBase

class NsiOrderClauseTemplate(NsiTemplateBase):
    __tablename__ = 'nsi_template_order_clause'
    __mapper_args__ = {'polymorphic_identity': 'order_clause'}
    
    id = Column(Integer, ForeignKey('nsi_template_base.id'), primary_key=True)

    fields = relationship('NsiOrderClauseFieldTemplate', back_populates='order_clause_template', cascade='all, delete-orphan')
    
    order_clauses = relationship('NsiOrderClauseTemplateAs', back_populates='template', cascade='all, delete-orphan')