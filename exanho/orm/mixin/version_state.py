import datetime
import enum

from sqlalchemy import Column, Enum, DateTime, Integer, String

class VersionState(enum.Enum):
    NEW = 0
    VALID = 1
    INVALID = 2
    PENDING = 3
    CHANCHING = 4
    OBSOLETE = 5

def default_active_to(context):
    return datetime.datetime.now() + datetime.timedelta(days=365)

class VersionMixin:
    state = Column(Enum(VersionState), default=VersionState.NEW, nullable=False)
    version_code = Column(String(50), nullable=False)
    version_description = Column(String(2000))
    priority = Column(Integer, default=0, nullable=False)
    active_from = Column(DateTime(timezone=True), default=datetime.datetime.now, nullable=False)
    active_to = Column(DateTime(timezone=True), default=default_active_to, nullable=False)