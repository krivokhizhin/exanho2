from sqlalchemy import BigInteger, Column, Date, DateTime, Index, String
from exanho.orm.domain import Base

class ZfcsContractProcedureCancel2015(Base):
    __tablename__ = 'zfcs_contract_procedure_cancel2015'
    
    id = Column(BigInteger, primary_key=True)

    cancelled_id = Column(BigInteger, nullable=False)
    reg_num = Column(String(19), nullable=False)

    # placer

    cancel_dt = Column(DateTime(timezone=True))
    reason = Column(String(2000))

    court_name = Column(String(2000))
    court_doc_name = Column(String(1000))
    court_doc_date = Column(Date)
    court_doc_number = Column(String(1000))
    # receiptDocuments

    # extPrintForm

    current_stage = Column(String(5))
    scheme_version = Column(String(20))
    content_id = Column(BigInteger)

Index('idx_zfcs_contract_procedure_cancel2015_cancelled_id', ZfcsContractProcedureCancel2015.cancelled_id, ZfcsContractProcedureCancel2015.current_stage, ZfcsContractProcedureCancel2015.cancel_dt, ZfcsContractProcedureCancel2015.court_doc_date, unique=True)
Index('idx_zfcs_contract_procedure_cancel2015_reg_num', ZfcsContractProcedureCancel2015.reg_num)