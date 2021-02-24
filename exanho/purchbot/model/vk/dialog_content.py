from sqlalchemy import BigInteger, Column, Index, String

from exanho.orm.domain import Base

class VkDialogContent(Base):
    __tablename__ = 'vk_dialog_content'

    id = Column(BigInteger, primary_key=True)

    group = Column(String(30), nullable=False)
    topic = Column(String(30), nullable=False)
    content  = Column(String(200))

Index('idx_vk_dialog_content', VkDialogContent.group, VkDialogContent.topic, unique=True)