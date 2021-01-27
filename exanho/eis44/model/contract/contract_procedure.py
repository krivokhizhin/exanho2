from sqlalchemy import BigInteger, Boolean, Column, DateTime, Index, Integer, String, UniqueConstraint
from exanho.orm.domain import Base

class ZfcsContractProcedure2015(Base):
    __tablename__ = 'zfcs_contract_procedure2015'
    
    id = Column(BigInteger, primary_key=True)

    doc_id = Column(BigInteger)
    external_id = Column(String(40))
    reg_num = Column(String(19), nullable=False)
    defense_number = Column(String(25))
    direct_dt = Column(DateTime(timezone=True))
    publish_dt = Column(DateTime(timezone=True))
    version_number = Column(Integer)

    # executions
    # executionObligationGuarantee
    # termination
    # refundOverpaymentsInfo
    # contractInvalidation
    # bankGuaranteeTermination
    # penalties
    # delayWriteOffPenalties
    # bankGuaranteePayment
    # holdCashEnforcement
    # printForm
    # extPrintForm
    # terminationDocuments
    # paymentDocuments
    # receiptDocuments
    # productOriginDocuments
    # examinationResultsDocuments
    # budgetObligations

    modification_reason = Column(String(2000))
    current_stage = Column(String(5))
    okpd2okved2 = Column(Boolean)
    scheme_version = Column(String(20))
    content_id = Column(BigInteger)

Index('idx_zfcs_contract_procedure2015_reg_num', ZfcsContractProcedure2015.reg_num)
UniqueConstraint(ZfcsContractProcedure2015.doc_id, ZfcsContractProcedure2015.external_id, name='uix_zfcs_contract_procedure2015_doc_id')