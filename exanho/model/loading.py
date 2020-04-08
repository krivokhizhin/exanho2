from enum import Enum
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..orm.sqlalchemy import Base
from .i_serialize import ISerializeToDict

class LoadStatus(Enum):
    NEW = 'NEW'
    DIRTY = 'DIRTY'
    COMPLETE = 'COMPLETE'


class LoadTask(Base, ISerializeToDict):
    __tablename__ = 'load_task'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    status = Column(String(20), nullable=False)
    location = Column(String(500), nullable=False)
    scheduled_date = Column(DateTime, nullable=False)
    description = Column(String(500))

    def __init__(self, name, location, desc=None):
        self.code = code
        self.name = name
        self.status = LoadStatus.NEW.value
        self.description = desc

    def __str__(self):
        return 'LoadTask, {0.id}: name={0.name}, status={0.status}, location={0.location}, scheduled_date={0.scheduled_date}'.format(self)

    def __repr__(self):
        return 'LoadTask(name={0.name}, status={0.status}, location={0.location}, scheduled_date={0.scheduled_date}, description={0.description})'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({
            'id':self.id,
            'name':self.name,
            'location':self.location,
            'status':self.status,
            'scheduled_date':self.scheduled_date,
            'description':self.description
            })

class LoadArchive(Base, ISerializeToDict):
    __tablename__ = 'load_archive'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    status = Column(String(20), nullable=False)
    location = Column(String(500), nullable=False)
    checksum = Column(String(50))
    update_date = Column(DateTime)

    files = relationship('LoadFile', back_populates='archive')

    def __str__(self):
        return 'LoadArchive, {0.id}: name={0.name}, status={0.status}, location={0.location}'.format(self)

    def __repr__(self):
        return 'LoadArchive(name={0.name}, status={0.status}, location={0.location})'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({
            'id':self.id,
            'name':self.name,
            'status':self.status,
            'location':self.location,
            'checksum':self.checksum,
            'update_date':self.update_date
            })

class LoadFile(Base, ISerializeToDict):
    __tablename__ = 'load_file'

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer, ForeignKey(LoadArchive.id))
    name = Column(String(256), nullable=False)
    status = Column(String(20), nullable=False)
    checksum = Column(String(50))
    update_date = Column(DateTime)

    archive = relationship('LoadArchive', back_populates='files')

    def __str__(self):
        return 'LoadFile, {0.id}: archive_id={0.archive_id}, name={0.name}, status={0.status}'.format(self)

    def __repr__(self):
        return 'LoadFile(archive_id={0.archive_id}, name={0.name}, status={0.status}'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({
            'id':self.id,
            'archive_id':self.archive_id,
            'name':self.name,
            'status':self.status,
            'checksum':self.checksum,
            'update_date':self.update_date
            })