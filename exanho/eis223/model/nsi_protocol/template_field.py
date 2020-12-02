from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .. import NsiFieldTemplateBase

class NsiProtocolFieldTemplate(NsiFieldTemplateBase):
    __tablename__ = 'nsi_template_field_protocol'
    __mapper_args__ = {'polymorphic_identity': 'protocol'}
    
    id = Column(Integer, ForeignKey('nsi_template_field_base.id'), primary_key=True)
    tab_level = Column(String(30), nullable=False)
    is_base_field = Column(Boolean, nullable=False)

    protocol_template_id = Column(Integer, ForeignKey('nsi_template_protocol.id'))
    protocol_template = relationship('NsiNoticeTemplate', back_populates='fields')