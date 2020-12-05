from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .. import NsiFieldTemplateBase

class NsiOrderClauseFieldTemplate(NsiFieldTemplateBase):
    __tablename__ = 'nsi_template_field_order_clause'
    __mapper_args__ = {'polymorphic_identity': 'order_clause'}
    
    id = Column(Integer, ForeignKey('nsi_template_field_base.id'), primary_key=True)

    order_clause_template_id = Column(Integer, ForeignKey('nsi_template_order_clause.id'))
    order_clause_template = relationship('NsiOrderClauseTemplate', back_populates='fields')