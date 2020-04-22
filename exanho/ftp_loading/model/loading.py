import enum

from sqlalchemy import BigInteger, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from exanho.orm.sqlalchemy import Base

class TaskStatus(enum.Enum):
    NEW = 1
    SCHEDULED = 2
    SCANNING = 3
    RUNNING = 4 
    PERFORMED = 5
    INACTIVE = 6
    ERROR = 7

class FtpTask(Base):
    __tablename__ = 'ftp_load_task'

    id = Column(Integer, primary_key=True)
    status = Column(Enum(TaskStatus), nullable=False)
    location = Column(String(500), nullable=False, index=True)
    schedule = Column(String(50), nullable=False)
    scheduled_date = Column(DateTime)
    min_date = Column(DateTime)
    max_date = Column(DateTime)
    excluded_folders = Column(String(4000))
    delimiter = Column(String(20))
    last_date = Column(DateTime)
    err_desc = Column(String(500))

    files = relationship('FtpFile', back_populates='task')

    def __str__(self):
        return 'FtpTask, {0.id}: status={0.status}, location={0.location}, schedule={0.schedule}, scheduled_date={0.scheduled_date}'.format(self)

class FileStatus(enum.Enum):
    NEW = 1
    READY = 2
    LOADING = 3
    DONE = 4
    FAILED = 5

class FtpFile(Base):
    __tablename__ = 'ftp_load_file'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey(FtpTask.id), nullable=False)
    status = Column(Enum(FileStatus), nullable=False)
    filename = Column(String(512), nullable=False, index=True)
    directory = Column(String(1024), nullable=False)
    size = Column(Integer)
    date = Column(DateTime)
    err_desc = Column(String(500))

    task = relationship('FtpTask', back_populates='files')
    files = relationship('FtpContent', back_populates='ftp_file')

    def __str__(self):
        return 'FtpFile, {0.id}: task_id={0.task_id}, status={0.status}, filename={0.filename}'.format(self)

class ContentStatus(enum.Enum):
    NEW = 1
    INSPECTED = 2
    DOWNLOADING = 3
    PREPARED = 4
    PARSING = 5
    PROCESSED = 6
    FAULT = 7

class FtpContent(Base):
    __tablename__ = 'ftp_load_content'

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey(FtpFile.id))
    status = Column(Enum(ContentStatus), nullable=False)
    name = Column(String(256), nullable=False, index=True)
    crc = Column(BigInteger)
    size = Column(Integer)
    last_modify = Column(DateTime)
    message = Column(String(100))

    ftp_file = relationship('FtpFile', back_populates='files')

    def __str__(self):
        return 'FtpContent, {0.id}: archive_id={0.archive_id}, status={0.status}, name={0.name}'.format(self)