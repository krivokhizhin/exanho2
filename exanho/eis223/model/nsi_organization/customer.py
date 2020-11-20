from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrgCustomer(Base):
    __tablename__ = 'nsi_org_customer'
    
    id = Column(Integer, primary_key=True)

    org = relationship('NsiOrganization', uselist=False, back_populates='customer', cascade='all, delete-orphan')

    full_name = Column(String(1000))
    short_name = Column(String(500))
    iko = Column(String(30))

    inn = Column(String(20), nullable=False, default='')
    kpp = Column(String(20), nullable=False, default='')
    ogrn = Column(String(20), nullable=False, default='')

    legal_address = Column(String(2000))
    postal_address = Column(String(2000))
    phone = Column(String(300))
    fax = Column(String(300))
    email = Column(String(300))

    okato = Column(String(20))
    okopf = Column(String(10))
    okopf_name = Column(String(200))
    okpo = Column(String(10))

    reg_date = Column(DateTime(timezone=True))
    time_zone_offset = Column(Integer)
    time_zone_name = Column(String(100))
    region = Column(String(200))
    assessed_compliance = Column(Boolean)
    monitored_compliance = Column(Boolean)

Index('idx_nsi_org_customer_ogrn_inn_kpp', NsiOrgCustomer.ogrn, NsiOrgCustomer.inn, NsiOrgCustomer.kpp, unique=True)
Index('idx_nsi_org_customer_inn_kpp_orgn', NsiOrgCustomer.inn, NsiOrgCustomer.kpp, NsiOrgCustomer.ogrn, unique=True)