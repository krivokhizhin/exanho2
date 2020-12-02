from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiProtocolTemplateAs(Base):
    __tablename__ = 'nsi_protocol_template_association'
    protocol_id = Column(Integer, ForeignKey('nsi_protocol.id'), primary_key=True)
    template_id = Column(Integer, ForeignKey('nsi_template_protocol.id'), primary_key=True)

    protocol = relationship('NsiProtocol', back_populates='templates')
    template = relationship('NsiProtocolTemplate', back_populates='protocols')