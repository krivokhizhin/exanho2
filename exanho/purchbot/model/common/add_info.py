import enum

from sqlalchemy import BigInteger, Column, Enum, String

from exanho.orm.domain import Base

class AddInfoCode(enum.Enum):
    PARTICIPANT = 1
    CUSTOMER = 2
    NOTIFICATION = 3
    CONTRACT = 4

class AddInfoSettings(Base):
    __tablename__ = 'add_info_settings'

    id = Column(BigInteger, primary_key=True)

    code = Column(Enum(AddInfoCode), nullable=False, unique=True)
    name = Column(String(200), nullable=False)