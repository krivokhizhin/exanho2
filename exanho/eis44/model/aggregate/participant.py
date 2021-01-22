from sqlalchemy import Column, Index, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class AggParticipant(ExaObjectMixin, Base):

    name = Column(String(2000))
    inn = Column(String(12), nullable=False)
    kpp = Column(String(9))

    name_lat = Column(String(2000))
    tax_payer_code = Column(String(100))
    country_full_name = Column(String(200))

    contracts = relationship('AggContractParticipant', back_populates='participant', cascade='all, delete-orphan')

Index('ix_agg_participant_inn_kpp', AggParticipant.inn, AggParticipant.kpp, unique=True)