from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Index, Integer, Numeric, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class ZfcsContract2015(Base):
    __tablename__ = 'zfcs_contract2015'
    
    id = Column(BigInteger, primary_key=True)

    doc_id = Column(BigInteger)
    external_id = Column(String(40))
    direct_dt = Column(DateTime(timezone=True))
    publish_dt = Column(DateTime(timezone=True))
    version_number = Column(Integer)

    # foundation

    conclusion_st95_ch17_1 = Column(Boolean)

    # customer
    # placer
    # finances

    protocol_date = Column(Date)
    doc_base = Column(String(2000))
    doc_code = Column(String(10))
    sign_date = Column(Date)
    reg_num = Column(String(19))
    number = Column(String(50))
    subject = Column(String(2000))

    group_build_code = Column(String(5))

    # bankSupportContractRequiredInfo

    defense_number = Column(String(25))
    is_goz = Column(Boolean)
    igk = Column(String(20))
    life_cycle = Column(Boolean)

    price = Column(String(30))
    price_type = Column(String(50))
    price_formula = Column(String(2000))
    price_formula_specified = Column(Boolean)
    currency_code = Column(String(3))
    currency_rate = Column(Numeric(10, 4))
    currency_raiting = Column(Integer)
    price_rur = Column(String(30))
    price_vat = Column(String(30))
    price_vat_rur = Column(String(30))
    reduced_by_taxes = Column(Boolean)
    right_to_conclude = Column(Boolean, default=False)

    advance_payment_percents = Column(Numeric(10, 7))
    advance_payment_value = Column(String(30))
    advance_payment_value_rur = Column(String(30))

    is_smpo_or_sono_tender = Column(Boolean)
    is_smpo_or_sono_engage = Column(Boolean)

    sub_contractors_percents = Column(Numeric(10, 7))
    sub_contractors_value_rur = Column(String(30))
    # subContractor

    quantity_stages = Column(Integer)
    execution_start_date = Column(Date)
    execution_end_date = Column(Date)
    # stages

    # enforcement
    # subsequentMaintenanceEnforcement
    # st14Info
    # qualityGuaranteeInfo
    # guaranteeReturns

    energy_service_info = Column(String(200))

    # products
    suppliers = relationship('ZfcsContract2015Supplier', back_populates='contract', cascade='all, delete-orphan')

    href = Column(String(1024))
    # print_form
    # extPrintForm
    # scanDocuments
    # medicalDocuments
    # singleSupplierP25Part1St93Documents
    # budgetObligations
    # attachments
    # modification
    
    current_stage = Column(String(5))
    okpd2okved2 = Column(Boolean)
    is_invalid = Column(Boolean)
    scheme_version = Column(String(20))
    content_id = Column(BigInteger)

Index('idx_zfcs_contract2015_reg_num', ZfcsContract2015.reg_num, ZfcsContract2015.number, ZfcsContract2015.version_number,unique=True)
Index('idx_zfcs_contract2015_doc_id', ZfcsContract2015.doc_id, ZfcsContract2015.external_id, unique=True)