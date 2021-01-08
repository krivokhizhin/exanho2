import enum
from sqlalchemy import Column, Date, Enum, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class CntrParticipantKind(enum.Enum):
    RF = 1      # Юридическое лицо РФ (legalEntityRF), Физическое лицо РФ (individualPersonRF) и Физическое лицо РФ. Поставщик культурных ценностей (individualPersonRFisCulture)
    FS = 2      # Юридическое лицо иностранного государства (legalEntityForeignState), Физическое лицо иностранного государства (individualPersonForeignState) и Физическое лицо иностранного государства. Поставщик культурных ценностей (individualPersonForeignStateisCulture)

class CntrParticipant(Base):
    __tablename__ = 'cntr_participant'
    
    id = Column(Integer, primary_key=True)
    kind = Column(Enum(CntrParticipantKind), nullable=False)

    okopf_code = Column(String(5))
    okopf_name = Column(String(2000))

    full_name = Column(String(2000))
    short_name = Column(String(2000))
    firm_name = Column(String(2000))

    okpo = Column(String(10))
    inn = Column(String(12))
    kpp = Column(String(9))
    registration_date = Column(Date)
    oktmo_code = Column(String(11))
    oktmo_name = Column(String(1000))

    contracts = relationship('ZfcsContract2015Supplier', back_populates='participant', cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_identity':CntrParticipantKind.RF,
        'polymorphic_on':kind
    }

Index('ix_cntr_participant_inn_kpp', CntrParticipant.inn, CntrParticipant.kpp, unique=True)

class ForeignParticipant(CntrParticipant):
    __tablename__ = 'cntr_participant_foreign'
    
    id = Column(Integer, ForeignKey('cntr_participant.id'), primary_key=True)

    full_name_lat = Column(String(2000))
    tax_payer_code = Column(String(100), index=True)
    country_code = Column(String(3))
    country_full_name = Column(String(200))

    address = Column(String(1024))
    post_address = Column(String(1024))
    email = Column(String(256))
    phone = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity':CntrParticipantKind.FS
    }