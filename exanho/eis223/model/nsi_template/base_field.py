from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiFieldTemplateBase(Base):
    __tablename__ = 'nsi_template_field_base'
    
    id = Column(Integer, primary_key=True)
    discriminator = Column('type', String(50))

    long_id = Column(BigInteger, nullable=False)
    name = Column(String(300), nullable=False)
    extend_type = Column(String(20), nullable=False)
    length = Column(String(21))
    mandatory = Column(Boolean, nullable=False)
    
    # position
    tab_ordinal = Column(BigInteger, nullable=False)
    tab_name = Column(String(130))
    section_ordinal = Column(BigInteger, nullable=False)
    section_name = Column(String(130))

    info = Column(String(100))
    integr_code = Column(String(50), nullable=False)
    index_number = Column(Integer, nullable=False)
    code = Column(String(50))

    table_type_id = Column(Integer, ForeignKey('nsi_template_table.id'))
    table_type = relationship('NsiTableTemplate')

    __mapper_args__ = {'polymorphic_on': discriminator}

Index('idx_nsi_template_field_tab_section', NsiFieldTemplateBase.tab_ordinal, NsiFieldTemplateBase.section_ordinal)