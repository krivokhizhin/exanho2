import enum

from sqlalchemy import BigInteger, Boolean, Column, Enum, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CntrEnsuringKind(enum.Enum):
    CA = 1      # cashAccount - Внесение денежных средств на указанный заказчиком счет
    BG = 2      # bankGuarantee - Банковская гарантия, выданная банком в соответствии со статьей 45

class ZfcsContract2015Enforcement(Base):
    __tablename__ = 'zfcs_contract2015_enforcement'
    
    id = Column(BigInteger, primary_key=True)
    kind = Column(Enum(CntrEnsuringKind), nullable=False)

    contract_id = Column(BigInteger, ForeignKey('zfcs_contract2015.id'), index=True)
    contract = relationship('ZfcsContract2015', back_populates='enforcements')

    is_subsequent_maintenance = Column(Boolean, default=False)

    quality_guarantee_id = Column(BigInteger, ForeignKey('cntr_quality_guarantee_info.id'), index=True)
    quality_guarantee = relationship('CntrQualityGuaranteeInfo', back_populates='ensuring_way')

    currency_code = Column(String(3))
    amount = Column(String(30))
    currency_rate = Column(Numeric(10, 4))
    currency_raiting = Column(Integer)
    amount_rur = Column(String(30))

    reg_number = Column(String(20))
    reg_number_not_published = Column(Boolean, default=False)
    doc_number = Column(String(23))
    doc_number_not_published = Column(Boolean, default=False)