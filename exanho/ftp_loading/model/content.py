import enum

from sqlalchemy import BigInteger, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from exanho.orm.sqlalchemy import Base

class FtpContentStatus(enum.Enum):
    NEW = 1
    INSPECTED = 2
    DOWNLOADING = 3
    PREPARED = 4
    PARSING = 5
    PROCESSED = 6
    FAULT = 7

class FtpContent(Base):
    __tablename__ = 'ftp_load_content'

    id = Column(BigInteger, primary_key=True)
    file_id = Column(BigInteger, ForeignKey('ftp_load_file.id'))
    status = Column(Enum(FtpContentStatus), nullable=False)
    name = Column(String(256), nullable=False, index=True)
    crc = Column(BigInteger)
    size = Column(Integer)
    last_modify = Column(DateTime)
    message = Column(String(100))

    ftp_file = relationship('FtpFile', back_populates='files')

    def __str__(self):
        return 'FtpContent, {0.id}: archive_id={0.archive_id}, status={0.status}, name={0.name}'.format(self)