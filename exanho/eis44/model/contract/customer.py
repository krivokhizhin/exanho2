from sqlalchemy import BigInteger, Column, Date, ForeignKey, Index, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CntrCustomer(Base):
    __tablename__ = 'cntr_customer'
    
    id = Column(BigInteger, primary_key=True)

    contract_id = Column(BigInteger, ForeignKey('zfcs_contract2015.id'))
    contract = relationship('ZfcsContract2015', back_populates='customer')

    reg_num = Column(String(11))
    cons_registry_num = Column(String(8))
    full_name = Column(String(2000))

    short_name = Column(String(2000))
    registration_date = Column(Date)
    inn = Column(String(12))
    kpp = Column(String(9))
    
    okopf_code = Column(String(5))
    okopf_name = Column(String(2000))

    okpo = Column(String(20))
    customer_code = Column(String(20))

Index('ix_cntr_customer_inn_kpp', CntrCustomer.inn, CntrCustomer.kpp)
Index('ix_cntr_customer_reg_num', CntrCustomer.reg_num)