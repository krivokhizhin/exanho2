from sqlalchemy import Column, Integer, String

from ..orm.sqlalchemy import Base

class NsiOrganizationType(Base):
    __tablename__ = 'nsiOrganizationType'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(2), index=True, nullable=False, unique=True)
    name = Column(String(20))
    description = Column(String(500))

    def __init__(self, code, name, desc=None):
        self.name = name
        self.code = code
        self.description = desc