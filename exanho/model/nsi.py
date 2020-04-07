from sqlalchemy import Column, Integer, String

from ..orm.sqlalchemy import Base
from .i_serialize import ISerializeToDict

class NsiOrganizationType(Base, ISerializeToDict):
    __tablename__ = 'nsiOrganizationType'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(2), index=True, nullable=False, unique=True)
    name = Column(String(20))
    description = Column(String(500))

    def __init__(self, code, name, desc=None):
        self.code = code
        self.name = name
        self.description = desc

    def __str__(self):
        return 'NsiOrganizationType, {0.id}: code={0.code}, name={0.name}'.format(self)

    def __repr__(self):
        return 'NsiOrganizationType({0.code}, {0.name}, {0.description})'.format(self)

    def serialize(self):
        dto = super().serialize()
        return dto.update({'id': self.id, 'code':self.code, 'name':self.name, 'description':self.description})
