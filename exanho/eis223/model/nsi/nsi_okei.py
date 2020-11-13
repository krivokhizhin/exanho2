from sqlalchemy import Column, Date, DateTime, Index, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOkei(Base):
    __tablename__ = 'nsi_okei'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(String(6), nullable=False)
    name = Column(String(1000), nullable=False)
    symbol = Column(String(30))

    section_id = Column(Integer, ForeignKey('nsi_okei_section.id'), nullable=False)
    section = relationship('NsiOkeiSection', back_populates='items')

    group_id = Column(Integer, ForeignKey('nsi_okei_group.id'), nullable=False)
    group = relationship('NsiOkeiGroup', back_populates='items')

Index('idx_nsi_okei', NsiOkei.code, unique=True)

class NsiOkeiSection(Base):
    __tablename__ = 'nsi_okei_section'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(1), nullable=False)
    name = Column(String(1000), nullable=False)

    items = relationship('NsiOkei', back_populates='section')

class NsiOkeiGroup(Base):
    __tablename__ = 'nsi_okei_group'
    
    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False)
    name = Column(String(1000), nullable=False)

    items = relationship('NsiOkei', back_populates='group')