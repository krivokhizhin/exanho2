import enum

from sqlalchemy import BigInteger, Column, Enum, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

LEN_ANALITIC = 10
class BalAccCode(enum.Enum):
    C901 = 901  # Общий счет оператора
    C902 = 902  # Счет оператора на вывод
    C907 = 907  # Промо счет оператора
    C951 = 951  # Счет оператора в ВК
    C101 = 101  # Свободный остаток
    C102 = 102  # Невыясненные поступления
    C107 = 107  # Промо-счет
    C301 = 301  # Оплата за QUE_PAR_ACT
    C701 = 701  # Промо-оплата за QUE_PAR_ACT
    C302 = 302  # Оплата за QUE_PAR_HIS
    C702 = 702  # Промо-оплата за QUE_PAR_HIS
    C331 = 331  # Оплата за SUB_PAR
    C731 = 731  # Промо-оплата за SUB_PAR
    C361 = 361  # Оплата за REP_PAR_ACT
    C761 = 761  # Промо-оплата за REP_PAR_ACT
    C362 = 362  # Оплата за REP_PAR_HIS
    C762 = 762  # Промо-оплата за REP_PAR_HIS
    C363 = 363  # Оплата за REP_PARS_CON
    C763 = 763  # Промо-оплата за REP_PARS_CON

class AccAccount(Base):
    __tablename__ = 'acc_account'

    id = Column(BigInteger, primary_key=True)

    account = Column(String(50), nullable=False, unique=True, index=True)

    balance_code = Column(Enum(BalAccCode), nullable=False, index=True)
    analitic1 = Column(BigInteger, index=True)
    analitic2 = Column(BigInteger, index=True)

    desc = Column(String(200))

    remain = relationship('AccRemain', uselist=False, back_populates='account')

    def __init__(self, balance_code:BalAccCode, analitic1=None, analitic2=None) -> None:

        self.balance_code = balance_code
        self.analitic1 = analitic1
        self.analitic2 = analitic2

        if self.analitic1 is None:
            assert self.analitic2 is None

        analitic1 = '' if analitic1 is None else str(analitic1).rjust(LEN_ANALITIC, '0')
        analitic2 = '' if analitic2 is None else str(analitic2).rjust(LEN_ANALITIC, '0')

        self.account = '{}{}{}'.format(balance_code.value, analitic1, analitic2)

    def __str__(self) -> str:
        return f'{self.account:>30} - {self.desc}'