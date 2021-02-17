import enum

from sqlalchemy import BigInteger, Column, Enum, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

LEN_ANALITIC = 10
class BalAccCode(enum.Enum):
    C901 = 901  # Общий счет оператора
    C907 = 907  # Промо счет оператора
    C951 = 951  # Счет оператора в ВК
    C101 = 101  # Свободный остаток
    C102 = 102  # Невыясненные поступления
    C107 = 107  # Промо-счет
    C131 = 131  # Оплата за запросы
    C132 = 132  # Оплата за подписки
    C133 = 133  # Оплата за отчеты

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