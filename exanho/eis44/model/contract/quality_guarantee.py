from sqlalchemy import BigInteger, Boolean, Column, Date,  ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CntrQualityGuaranteeInfo(Base):
    __tablename__ = 'cntr_quality_guarantee_info'
    
    id = Column(BigInteger, primary_key=True)

    contract_id = Column(BigInteger, ForeignKey('zfcs_contract2015.id'), index=True)
    contract = relationship('ZfcsContract2015', back_populates='quality_guarantee')

    from_date = Column(Date)
    to_date = Column(Date)
    other_period_text = Column(String(2000))
    period_not_published = Column(Boolean, default=False)

    warranty_reqs_text = Column(String(2000))
    manufacturer_warranty_reqs_text = Column(String(2000))
    isQAEnsuramceRequired = Column(Boolean)

    ensuring_way = relationship('ZfcsContract2015Enforcement', uselist=False, back_populates='quality_guarantee', cascade='all, delete-orphan')

    guarantee_returns = relationship('ZfcsContract2015BgReturn', back_populates='quality_guarantee', cascade='all, delete-orphan')