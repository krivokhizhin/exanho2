import enum
from sqlalchemy import BigInteger, Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CntrSupplierType(enum.Enum):
    LERF = 1    # Юридическое лицо РФ (legalEntityRF)
    IPRF = 2    # Физическое лицо РФ (individualPersonRF)
    IPRFC = 3   # Физическое лицо РФ. Поставщик культурных ценностей (individualPersonRFisCulture)
    LEFS = 4    # Юридическое лицо иностранного государства (legalEntityForeignState)
    IPFS = 5    # Физическое лицо иностранного государства (individualPersonForeignState)
    IPFSC = 6   # Физическое лицо иностранного государства. Поставщик культурных ценностей (individualPersonForeignStateisCulture)
    NPEIS = 7   # Информация не будет размещена на официальном сайте ЕИС в соответствии с ч. 5 ст. 103 Федерального закона № 44-ФЗ (notPublishedOnEIS)

class ZfcsContract2015Supplier(Base):
    __tablename__ = 'zfcs_contract2015_supplier'
    
    id = Column(BigInteger, primary_key=True)
    type = Column(Enum(CntrSupplierType), nullable=False)

    contract_id = Column(Integer, ForeignKey('zfcs_contract2015.id'), primary_key=True)
    participant_id = Column(Integer, ForeignKey('cntr_participant.id'), primary_key=True)

    contract = relationship('ZfcsContract2015', back_populates='suppliers')
    participant = relationship('CntrParticipant', back_populates='contracts')

    status = Column(String(2))
    ersmsp_inclusion_date = Column(Date)
    contract_price = Column(String(30))

    personal_account = Column(String(11))

    address = Column(String(1024))
    mailing_adress = Column(String(1024))
    mail_facility_name = Column(String(1024))
    post_box_number = Column(String(1024))
    post_address = Column(String(1024))
    
    contact_id = Column(Integer, ForeignKey('cntr_contact.id'))
    contact = relationship('CntrContact', back_populates='suppliers')

    contact_email = Column(String(256))
    contact_phone = Column(String(30))

    is_ip = Column(Boolean, default=False)
    is_culture = Column(Boolean, default=False)