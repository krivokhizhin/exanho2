from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from .. import NsiTemplateBase

class NsiNoticeTemplate(NsiTemplateBase):
    __tablename__ = 'nsi_template_notice'
    __mapper_args__ = {'polymorphic_identity': 'notice'}
    
    id = Column(Integer, ForeignKey('nsi_template_base.id'), primary_key=True)
    copy_of_type = Column(String(4), nullable=False)
    hidden_fields = Column(String(20))

    fields = relationship('NsiNoticeFieldTemplate', back_populates='notice_template', cascade='all, delete-orphan')
    
    methods = relationship('NsiPurchMethodTemplateAs', back_populates='template', cascade='all, delete-orphan')