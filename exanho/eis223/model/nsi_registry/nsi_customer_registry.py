from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiCustomerRegistry(Base):
    __tablename__ = 'nsi_customer_registry'
    
    id = Column(Integer, primary_key=True)

    registration_number = Column(String(28), nullable=False, index=True, unique=True)
    version = Column(Integer, nullable=False)
    version_creation_dt = Column(DateTime(timezone=True), nullable=False)
    status = Column(String(30))

    added_dt = Column(DateTime(timezone=True))
    removed_dt = Column(DateTime(timezone=True))

    customer_id = Column(Integer, ForeignKey('customer_registry_info.id'), nullable=False, index=True, unique=True)
    customer = relationship('CustomerRegistryInfo', back_populates='customer_registry')

    ikuls = relationship('NsiRegIkul', back_populates='customer_registry', cascade='all, delete-orphan')

    okved_list = relationship('NsiRegOkvedActivity', back_populates='customer', cascade='all, delete-orphan')
    okved2_list = relationship('NsiRegOkved2Activity', back_populates='customer', cascade='all, delete-orphan')
    fz223types = relationship('NsiRegClassificationFz223type', back_populates='customer', cascade='all, delete-orphan')

    okpo = Column(String(20))
    okpo_name = Column(String(200))
    okato = Column(String(20))
    okato_name = Column(String(200))
    oktmo = Column(String(20))
    oktmo_name = Column(String(200))
    okfs = Column(String(10))
    okfs_name = Column(String(200))
    okopf = Column(String(10))
    okopf_name = Column(String(200))

    is_customer = Column(Boolean, default=False)
    is_customer_representative = Column(Boolean, default=False)
    is_supervisor = Column(Boolean, default=False)
    is_operator = Column(Boolean, default=False)
    is_ovk = Column(Boolean, default=False)
    is_purchase_audit = Column(Boolean, default=False)
    is_monitoring = Column(Boolean, default=False)
    is_assessment = Column(Boolean, default=False)
    is_typal_order_clause = Column(Boolean, default=False)
    is_operator_em = Column(Boolean, default=False)

    contact = relationship('NsiRegContact', uselist=False, cascade='all, delete-orphan', back_populates='customer_registry')
    granted_users = relationship('NsiRegGrantedUser', cascade='all, delete-orphan', back_populates='customer_registry')

    is_ppo = Column(Boolean, default=False, nullable=False)
    ppo_code = Column(String(20))
    ppo_name = Column(String(2000))

    capital_stock_agencies = relationship('NsiRegCapitalStockAgency', cascade='all, delete-orphan', back_populates='customer_registry')