from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import BigInteger, Column, DateTime

class ExaObjectMixin:

    @declared_attr
    def __tablename__(cls):
        return ''.join(['_'+ch.lower() if ch.isupper() and index>0 else ch.lower() for index, ch in enumerate(cls.__name__)])

    id = Column(BigInteger, primary_key=True)

    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    created_by = Column(BigInteger, default=0, nullable=False)

    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now)
    updated_by = Column(BigInteger)

    def __str__(self):
        return f'ExaObject({self.__class__.__table__.key}, {self.id})'