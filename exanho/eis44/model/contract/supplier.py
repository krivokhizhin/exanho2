import enum
from sqlalchemy import BigInteger, Boolean, Column, Date, Enum, ForeignKey, Index, Integer, String
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

    contract_id = Column(BigInteger, ForeignKey('zfcs_contract2015.id'))
    contract = relationship('ZfcsContract2015', back_populates='suppliers')

    order = Column(Integer, default=1)
    
    okopf_code = Column(String(5))
    okopf_name = Column(String(2000))

    full_name = Column(String(2000))
    short_name = Column(String(2000))
    firm_name = Column(String(2000))

    okpo = Column(String(20))
    inn = Column(String(12))
    kpp = Column(String(9))
    registration_date = Column(Date)
    oktmo_code = Column(String(11))
    oktmo_name = Column(String(1000))

    full_name_lat = Column(String(2000))
    tax_payer_code = Column(String(100))
    country_code = Column(String(3))
    country_full_name = Column(String(200))

    fs_address = Column(String(1024))
    fs_post_address = Column(String(1024))
    fs_email = Column(String(256))
    fs_phone = Column(String(30))

    status = Column(String(2))
    ersmsp_inclusion_date = Column(Date)
    contract_price = Column(String(30))

    personal_account = Column(String(11))

    address = Column(String(1024))
    mailing_adress = Column(String(1024))
    mail_facility_name = Column(String(1024))
    post_box_number = Column(String(1024))
    post_address = Column(String(1024))
    
    contact_last_name = Column(String(250))
    contact_first_name = Column(String(250))
    contact_middle_name = Column(String(250))
    contact_email = Column(String(256))
    contact_phone = Column(String(30))

    is_ip = Column(Boolean)
    is_culture = Column(Boolean)

Index('ix_zfcs_contract2015_supplier_inn_kpp', ZfcsContract2015Supplier.inn, ZfcsContract2015Supplier.kpp)
Index('ix_zfcs_contract2015_supplier_tax_payer_code', ZfcsContract2015Supplier.tax_payer_code)