import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..orm.sqlalchemy import Base

class TaskStatus(enum.Enum):
    NEW = 1
    SCHEDULED = 2
    SCANNING = 3
    RUNNING = 4 
    DONE = 5
    INACTIVE = 6
    ERROR = 7

class LoadTask(Base):
    __tablename__ = 'load_task'

    id = Column(Integer, primary_key=True)
    status = Column(Enum(TaskStatus), nullable=False)
    location = Column(String(500), nullable=False, index=True)
    schedule = Column(String(50), nullable=False)
    scheduled_date = Column(DateTime)
    last_date = Column(DateTime)
    err_desc = Column(String(500))

    archives = relationship('LoadArchive', back_populates='task')

    def __str__(self):
        return 'LoadTask, {0.id}: status={0.status}, location={0.location}, schedule={0.schedule}, scheduled_date={0.scheduled_date}'.format(self)

class ArchiveStatus(enum.Enum):
    NEW = 1
    READY = 2
    LOADING = 3
    PERFORMED = 4
    FAILED = 5

class LoadArchive(Base):
    __tablename__ = 'load_archive'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey(LoadTask.id), nullable=False)
    status = Column(Enum(ArchiveStatus), nullable=False)
    name = Column(String(256), nullable=False, index=True)
    size = Column(Integer)
    date = Column(DateTime)
    err_desc = Column(String(500))

    task = relationship('LoadTask', back_populates='archives')
    files = relationship('LoadFile', back_populates='archive')

    def __str__(self):
        return 'LoadArchive, {0.id}: task_id={0.task_id}, status={0.status}, name={0.name}'.format(self)

class FileStatus(enum.Enum):
    NEW = 1
    CONSIDERED = 2
    DOWNLOADING = 3
    PREPARED = 4
    PARSING = 5
    COMPLETE = 6
    FAULT = 7

class LoadFile(Base):
    __tablename__ = 'load_file'

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer, ForeignKey(LoadArchive.id))
    status = Column(Enum(FileStatus), nullable=False)
    filename = Column(String(256), nullable=False, index=True)
    crc = Column(String(50))
    size = Column(Integer)
    last_modify = Column(DateTime)
    message = Column(String(100))

    archive = relationship('LoadArchive', back_populates='files')

    def __str__(self):
        return 'LoadFile, {0.id}: archive_id={0.archive_id}, status={0.status}, filename={0.filename}'.format(self)