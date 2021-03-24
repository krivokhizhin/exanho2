from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Index, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CntrPlacer(Base):
    __tablename__ = 'cntr_placer'
    
    id = Column(BigInteger, primary_key=True)

    contract_id = Column(BigInteger, ForeignKey('zfcs_contract2015.id'))
    contract = relationship('ZfcsContract2015', back_populates='placer')

    reg_num = Column(String(11))
    cons_registry_num = Column(String(8))
    full_name = Column(String(2000))

    responsible_role = Column(String(5))
    placer_change = Column(Boolean)

Index('ix_cntr_placer_reg_num', CntrPlacer.reg_num)