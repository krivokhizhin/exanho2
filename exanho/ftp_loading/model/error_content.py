from sqlalchemy import BigInteger, Column, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from exanho.orm.domain import Base

class FtpErrorContent(Base):
    __tablename__ = 'ftp_load_error_content'

    content_id = Column(BigInteger, ForeignKey('ftp_load_content.id'), primary_key=True)
    content = relationship('FtpContent', back_populates='error_content')

    origin_data = Column(LargeBinary)
    correct_data = Column(LargeBinary)

    def __str__(self):
        return 'FtpErrorContent, {0.content_id}: {0.data}'.format(self)