from sqlalchemy import BigInteger, Column, Index, Integer, String
from exanho.orm.domain import Base

class NsiTemplateBase(Base):
    __tablename__ = 'nsi_template_base'
    
    id = Column(Integer, primary_key=True)
    discriminator = Column('type', String(50))

    long_id = Column(BigInteger, nullable=False)
    parent_long_id = Column(BigInteger, nullable=False)
    status = Column(String(1), nullable=False)
    version = Column(Integer, nullable=False)

    __mapper_args__ = {'polymorphic_on': discriminator}

Index('idx_purch_template_id', NsiTemplateBase.discriminator, NsiTemplateBase.long_id, unique=True)