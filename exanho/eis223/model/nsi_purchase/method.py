from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Index, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base

class NsiPurchaseMethod(Base):
    __tablename__ = 'nsi_purchase_method'
    
    id = Column(Integer, primary_key=True)
    guid = Column(String(36))
    create_dt = Column(DateTime(timezone=True), nullable=False)
    change_dt = Column(DateTime(timezone=True))
    start_date_active = Column(Date)
    end_date_active = Column(Date)
    business_status = Column(String(10), nullable=False)
    code = Column(BigInteger, nullable=False)
    name = Column(String(3000), nullable=False)
    parent_code = Column(BigInteger, nullable=False)
    order_number = Column(Integer, nullable=False)
    is_electronic = Column(Boolean, default=False)

    creator_id = Column(Integer, ForeignKey('nsi_org_customer.id'))
    creator = relationship('NsiOrgCustomer')

    extended = Column(Boolean)
    competitive = Column(Boolean)

    templates = relationship('NsiPurchMethodTemplateAs', back_populates='method', cascade='all, delete-orphan')

    protocol_controlled_order = Column(Boolean)
    protocols = relationship('NsiPurchMethodProtocolAs', back_populates='method', cascade='all, delete-orphan')
    phases = relationship('NsiPurchMethodPhaseAs', back_populates='method', cascade='all, delete-orphan')

    hasPhases = Column(Boolean, nullable=False)
    typal = Column(Boolean, nullable=False)
    typalKind = Column(String(10))
    lotOriented = Column(Boolean, nullable=False)