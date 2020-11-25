from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchMethodTemplateAs(Base):
    __tablename__ = 'nsi_purch_method_template_association'
    method_id = Column(Integer, ForeignKey('nsi_purchase_method.id'), primary_key=True)
    template_id = Column(Integer, ForeignKey('nsi_template_notice.id'), primary_key=True)

    method = relationship('NsiPurchaseMethod', back_populates='templates')
    template = relationship('NsiNoticeTemplate', back_populates='methods')