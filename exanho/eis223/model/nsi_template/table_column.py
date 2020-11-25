from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiTableColumnTemplate(Base):
    __tablename__ = 'nsi_template_table_column'
    
    id = Column(Integer, primary_key=True)

    index = Column(Integer, nullable=False)
    name = Column(String(40), nullable=False)
    extend_type = Column(String(20), nullable=False)
    length = Column(String(21))
    mandatory = Column(Boolean, nullable=False)
    integr_code = Column(String(50), nullable=False)
    info = Column(String(400), nullable=False)

    table_id = Column(Integer, ForeignKey('nsi_template_table.id'))
    table = relationship('NsiTableTemplate', back_populates='columns')