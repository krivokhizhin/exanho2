from sqlalchemy import Column, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiRegCapitalStockAgency(Base):
    __tablename__ = 'nsi_reg_capital_stock_agency'
    
    id = Column(Integer, primary_key=True)

    customer_registry_id = Column(Integer, ForeignKey('nsi_customer_registry.id'), nullable=False, index=True)
    customer_registry = relationship('NsiCustomerRegistry', back_populates='capital_stock_agencies')

    ogrn = Column(String(20), nullable=False, index=True)
    inn = Column(String(20), nullable=False)
    kpp = Column(String(20), nullable=False)

    full_name = Column(String(1000))

Index('idx_nsi_reg_capital_stock_agency_inn_kpp_orgn', NsiRegCapitalStockAgency.inn, NsiRegCapitalStockAgency.kpp)