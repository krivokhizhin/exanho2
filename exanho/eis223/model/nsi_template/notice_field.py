from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .base_field import NsiFieldTemplateBase

class NsiNoticeFieldTemplate(NsiFieldTemplateBase):
    __tablename__ = 'nsi_template_field_notice'
    __mapper_args__ = {'polymorphic_identity': 'notice'}
    
    id = Column(Integer, ForeignKey('nsi_template_field_base.id'), primary_key=True)
    tab_level = Column(String(30), nullable=False)
    is_base_field = Column(Boolean, nullable=False)

    notice_template_id = Column(Integer, ForeignKey('nsi_template_notice.id'))
    notice_template = relationship('NsiNoticeTemplate', back_populates='fields')