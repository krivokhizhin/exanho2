from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from ..orm.sqlalchemy import Base
from .i_serialize import ISerializeToDict

class LoadStatus(Base, ISerializeToDict):
    __tablename__ = 'LoadStatus'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(100))
    description = Column(String(500))

    def __init__(self, code, name, desc=None):
        self.code = code
        self.name = name
        self.description = desc

    def __str__(self):
        return 'LoadStatus, {0.id}: code={0.code}, name={0.name}'.format(self)

    def __repr__(self):
        return 'LoadStatus({0.code}, {0.name}, {0.description})'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({'id': self.id, 'code':self.code, 'name':self.name, 'description':self.description})

class FtpArchive(Base, ISerializeToDict):
    __tablename__ = 'ftpArchive'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    status_id = Column(Integer, ForeignKey('LoadStatus.id'), nullable=False) # ForeignKey(LoadStatus.id)
    location = Column(String(500), nullable=False)
    checksum = Column(String(50))
    update_date = Column(DateTime)

    def __str__(self):
        return 'FtpArchive, {0.id}: name={0.name}, status_id={0.status_id}, location={0.location}'.format(self)

    def __repr__(self):
        return 'FtpArchive(name={0.name}, status_id={0.status_id}, location={0.location})'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({
            'id': self.id,
            'name':self.name,
            'status_id':self.status_id,
            'location':self.location,
            'checksum':self.checksum,
            'update_date':self.update_date
            })

class FtpFile(Base, ISerializeToDict):
    __tablename__ = 'ftpFile'

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer, ForeignKey('ftpArchive.id')) # ForeignKey(FtpArchive.id)
    name = Column(String(256), nullable=False)
    status_id = Column(Integer, ForeignKey('LoadStatus.id'), nullable=False) # ForeignKey(LoadStatus.id)
    checksum = Column(String(50))
    update_date = Column(DateTime)

    def __str__(self):
        return 'FtpFile, {0.id}: archive_id={0.archive_id}, name={0.name}, status_id={0.status_id}'.format(self)

    def __repr__(self):
        return 'FtpFile(archive_id={0.archive_id}, name={0.name}, status_id={0.status_id}'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({
            'id': self.id,
            'archive_id':self.archive_id,
            'name':self.name,
            'status_id':self.status_id,
            'checksum':self.checksum,
            'update_date':self.update_date
            })