from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiOrganization(Base):
    __tablename__ = 'nsi_organization'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    code = Column(String(20))
    code_assign_dt = Column(DateTime(timezone=True))
    code_invalidate_dt = Column(DateTime(timezone=True))
    create_dt = Column(DateTime(timezone=True))
    change_dt = Column(DateTime(timezone=True))
    block_dt = Column(DateTime(timezone=True))
    change_esia_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)

    customer_id = Column(Integer, ForeignKey('customer_main_info.id'), nullable=False, index=True, unique=True)
    customer = relationship('CustomerMainInfo', back_populates='organization')

    status = Column(String(20))
    okfs = Column(String(10))
    okopf = Column(String(10))
    okato = Column(String(20))
    oktmo = Column(String(20))
    okpo = Column(String(20))

    spz_code = Column(String(255))
    pgmu_code = Column(String(255))
    rf_subject_code = Column(String(255))

    is_ppo = Column(Boolean, default=False)
    ppo_code = Column(String(20))
    ppo_name = Column(String(2000))

    okved_list = relationship('NsiOrgOkvedActivity', back_populates='org', cascade='all, delete-orphan')
    okved2_list = relationship('NsiOrgOkved2Activity', back_populates='org', cascade='all, delete-orphan')
    fz223types = relationship('NsiOrgFz223typeAs', back_populates='org', cascade='all, delete-orphan')

    time_zone_offset = Column(Integer)
    time_zone_name = Column(String(100))

    is_detached_department = Column(Boolean, default=False)

    is_customer = Column(Boolean, default=False)
    is_customer_agent = Column(Boolean, default=False)
    is_supervisor = Column(Boolean, default=False)
    is_operator = Column(Boolean, default=False)
    is_ovk = Column(Boolean, default=False)
    is_purchase_audit = Column(Boolean, default=False)
    is_monitoring = Column(Boolean, default=False)
    is_assessment = Column(Boolean, default=False)
    is_typal_order_clause = Column(Boolean, default=False)
    is_operator_em = Column(Boolean, default=False)

    contact = relationship('NsiOrgContact', uselist=False, cascade='all, delete-orphan', back_populates='org')

    comment = Column(String(500))

    successors = relationship('NsiOrgSuccessor', cascade='all, delete-orphan', back_populates='org')