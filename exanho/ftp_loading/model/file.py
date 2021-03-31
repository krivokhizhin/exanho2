import enum

from sqlalchemy import BigInteger, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class FtpFileStatus(enum.Enum):
    NEW = 1
    READY = 2
    LOADING = 3
    DONE = 4
    FAILED = 5

class FtpFile(Base):
    __tablename__ = 'ftp_load_file'

    id = Column(BigInteger, primary_key=True)
    task_id = Column(BigInteger, ForeignKey('ftp_load_task.id'), nullable=False)
    status = Column(Enum(FtpFileStatus), nullable=False)
    filename = Column(String(512), nullable=False, index=True)
    directory = Column(String(1024), nullable=False)
    size = Column(Integer)
    date = Column(DateTime)
    err_desc = Column(String(500))

    task = relationship('FtpTask', back_populates='files')
    files = relationship('FtpContent', back_populates='ftp_file', cascade='all, delete-orphan')

    def __str__(self):
        return 'FtpFile, {0.id}: task_id={0.task_id}, status={0.status}, filename={0.filename}'.format(self)