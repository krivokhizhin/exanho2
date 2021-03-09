import enum

from sqlalchemy import BigInteger, Boolean, Column, Enum, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import relationship
from exanho.orm.domain import Base
from exanho.orm.mixin import ExaObjectMixin

class CntrEnsuringWay(enum.Enum):
    CA = 1      # cashAccount - Внесение денежных средств на указанный заказчиком счет
    BG = 2      # bankGuarantee - Банковская гарантия, выданная банком в соответствии со статьей 45

class CntrEnsuringType(enum.Enum):
    ENFORCEMENT = 1  # ОИК - Обеспечение исполнения контракта
    QUALITY = 2      # ОГО - обеспечение гарантийных обязательств по контракту
    MAINTENANCE = 3  # Обеспечение исполнения контракта по последующему обслуживанию, эксплуатации (при наличии) в течение срока службы, ремонту и (или) утилизации поставленного товара или созданного в результате выполнения работы объекта капитального строительства или товара

class CntrEnsuringStatus(enum.Enum):
    ACCEPT = 1       # Обязательство принято
    EXECUTION = 2    # Обязательство исполнено (взыскано)
    RETURN = 3       # Обязательство возвращено заказчиком
    WAIVER = 4       # Гарант освобожден от обязательства
    TERMINATION = 5  # Обязательство прекращено

class AggContractEnsuring(ExaObjectMixin, Base):
    
    way = Column(Enum(CntrEnsuringWay), nullable=False)
    kind = Column(Enum(CntrEnsuringType), nullable=False)
    status = Column(Enum(CntrEnsuringStatus), nullable=False)

    contract_id = Column(BigInteger, ForeignKey('agg_contract.id'), nullable=False, index=True)
    contract = relationship('AggContract', back_populates='ensuring')

    currency_code = Column(String(3))
    amount = Column(Numeric(18,2), nullable=False, default=0)

UniqueConstraint(AggContractEnsuring.contract_id, AggContractEnsuring.kind, AggContractEnsuring.status, name='uix_agg_contract_ensuring')