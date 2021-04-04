from sqlalchemy import BigInteger, Column, Date, DateTime, Index, String
from exanho.orm.domain import Base

class ZfcsContractCancel2015(Base):
    __tablename__ = 'zfcs_contract_cancel2015'
    
    id = Column(BigInteger, primary_key=True)

    reg_num = Column(String(19), nullable=False)
    cancel_dt = Column(DateTime(timezone=True), nullable=False)

    publish_dt = Column(DateTime(timezone=True))
    doc_base = Column(String(2000), nullable=False)
    current_stage = Column(String(5))

    contract_number = Column(String(100))
    sign_date = Column(Date)
    # contractPrintFormInfo->customer
    sign_name = Column(String(2000))

    scheme_version = Column(String(20))
    content_id = Column(BigInteger)

Index('idx_zfcs_contract_cancel2015_reg_num', ZfcsContractCancel2015.reg_num)