from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiTableTemplateFixedColumnData(Base):
    __tablename__ = 'nsi_template_table_fixed_column_data'
    
    id = Column(Integer, primary_key=True)
    value = Column(String(100), nullable=False)

    table_id = Column(Integer, ForeignKey('nsi_template_table.id'))
    table = relationship('NsiTableTemplate', back_populates='fixed_columns_data')