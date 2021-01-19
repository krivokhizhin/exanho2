from sqlalchemy import BigInteger, Column, Index, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class EisParticipant(ExaObjectMixin, Base):

    name = Column(String(2000))
    inn = Column(String(12), nullable=False)
    kpp = Column(String(9))

    name_lat = Column(String(2000))
    tax_payer_code = Column(String(100))
    country_full_name = Column(String(200))

    contracts = relationship('EisContractParticipant', back_populates='participant', cascade='all, delete-orphan')

Index('ix_eis_participant_inn_kpp', EisParticipant.inn, EisParticipant.kpp, unique=True)