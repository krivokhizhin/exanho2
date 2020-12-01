from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Index, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiTableTemplate(Base):
    __tablename__ = 'nsi_template_table'
    
    id = Column(Integer, primary_key=True)

    long_id = Column(BigInteger, nullable=False, index=True, unique=True)
    name = Column(String(100), nullable=False)

    fixed_columns_data = relationship('NsiTableTemplateFixedColumnData', back_populates='table', cascade='all, delete-orphan')

    columns = relationship('NsiTableColumnTemplate', back_populates='table', cascade='all, delete-orphan')