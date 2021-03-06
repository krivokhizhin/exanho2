import enum

from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CntrBgReturnKind(enum.Enum):
    RETURN = 1          # bankGuaranteeReturn - Информация о возвращении заказчиком банковской гарантии гаранту
    WAIVER = 2          # waiverNotice - Информация об уведомлении, направленном заказчиком гаранту, об освобождении от обязательств по банковской гарантии
    NOT_PUBLISHED = 3   # notPublishedOnEIS - Информация не будет размещена на официальном сайте ЕИС в соответствии с ч. 8.1 ст. 45 Федерального закона № 44-ФЗ

class ZfcsContract2015BgReturn(Base):
    __tablename__ = 'zfcs_contract2015_bg_return'
    
    id = Column(BigInteger, primary_key=True)
    kind = Column(Enum(CntrBgReturnKind), nullable=False)

    contract_id = Column(BigInteger, ForeignKey('zfcs_contract2015.id'), index=True)
    contract = relationship('ZfcsContract2015', back_populates='guarantee_returns')

    quality_guarantee_id = Column(BigInteger, ForeignKey('cntr_quality_guarantee_info.id'), index=True)
    quality_guarantee = relationship('CntrQualityGuaranteeInfo', back_populates='guarantee_returns')

    reg_number = Column(String(20))
    doc_number = Column(String(23))
    date = Column(Date)
    reason = Column(String(2000))
    publish_dt = Column(DateTime(timezone=True))

    notice_number = Column(String(100))