import enum
from sqlalchemy import Column, Enum, Integer, String

from exanho.orm.sqlalchemy import Base

class ValueType(enum.Enum):
    int = 0
    str = 1

class KeyValue(Base):
    __tablename__ = 'key_value'

    key = Column(Integer, primary_key=True)
    type = Column(Enum(ValueType), nullable=False)
    value = Column(String(100))