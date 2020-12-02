from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .. import NsiTemplateBase

class NsiProtocolTemplate(NsiTemplateBase):
    __tablename__ = 'nsi_template_protocol'
    __mapper_args__ = {'polymorphic_identity': 'protocol'}
    
    id = Column(Integer, ForeignKey('nsi_template_base.id'), primary_key=True)

    hide_comm_decision = Column(Boolean, nullable=False)
    hide_comm_decision_access = Column(Boolean, nullable=False)
    hide_comm_decision_result = Column(Boolean, nullable=False)
    hide_procedure = Column(Boolean, nullable=False)
    hide_cancellation = Column(Boolean, nullable=False)

    fields = relationship('NsiProtocolFieldTemplate', back_populates='protocol_template', cascade='all, delete-orphan')
    
    protocols = relationship('NsiProtocolTemplateAs', back_populates='template', cascade='all, delete-orphan')