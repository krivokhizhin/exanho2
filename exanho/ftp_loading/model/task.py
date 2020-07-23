import enum

from sqlalchemy import BigInteger, Column, DateTime, Enum, String
from sqlalchemy.orm import relationship

from exanho.orm.sqlalchemy import Base

class FtpTaskStatus(enum.Enum):
    NEW = 1
    SCHEDULED = 2
    SCANNING = 3
    RUNNING = 4 
    PERFORMED = 5
    INACTIVE = 6
    ERROR = 7

class FtpTask(Base):
    __tablename__ = 'ftp_load_task'

    id = Column(BigInteger, primary_key=True)
    status = Column(Enum(FtpTaskStatus), nullable=False)
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