from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


tag_meme_association_table = Table(
    "tag_meme_association",
    Base.metadata,
    Column("tag_id", ForeignKey("tag.tag_id"), primary_key=True),
    Column("meme_id", ForeignKey("meme.meme_id"), primary_key=True),
)


class Meme(Base):
    __tablename__ = 'meme'
    meme_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024))
    link = Column(String(1024))
    tags = relationship("Tag", secondary=tag_meme_association_table, back_populates="memes")
