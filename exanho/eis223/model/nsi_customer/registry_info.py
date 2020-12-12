from sqlalchemy import Boolean, Column, DateTime, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class CustomerRegistryInfo(Base):
    __tablename__ = 'customer_registry_info'
    
    id = Column(Integer, primary_key=True)

    full_name = Column(String(1000))

    ogrn = Column(String(20), nullable=False, default='')
    inn = Column(String(20), nullable=False, default='')
    kpp = Column(String(20), nullable=False, default='')

    reg_date = Column(DateTime(timezone=True))
    legal_address = Column(String(2000))
    website = Column(String(300))
    iko = Column(String(30))
    create_iko_dt = Column(DateTime(timezone=True))
    time_zone_offset = Column(Integer)
    time_zone_name = Column(String(100))

    postal_address = Column(String(2000))
    email_system = Column(String(300))
    email = Column(String(300))
    phone = Column(String(300))
    fax = Column(String(300))

    customer_registry = relationship('NsiCustomerRegistry', uselist=False, back_populates='customer', cascade='all, delete-orphan')

Index('idx_nsi_reg_customer_ogrn_inn_kpp', CustomerRegistryInfo.ogrn, CustomerRegistryInfo.inn, CustomerRegistryInfo.kpp, unique=True)
Index('idx_nsi_reg_customer_inn_kpp_orgn', CustomerRegistryInfo.inn, CustomerRegistryInfo.kpp, CustomerRegistryInfo.ogrn, unique=True)