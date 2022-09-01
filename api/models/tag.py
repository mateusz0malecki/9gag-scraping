from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db.database import Base
from .meme import tag_meme_association_table


class Tag(Base):
    __tablename__ = 'tag'
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(128))
    memes = relationship(
        "Meme", secondary=tag_meme_association_table, back_populates="tags"
    )

    @staticmethod
    def get_tag_by_name(db, tag_name):
        db.query(Tag).filter(Tag.tag_name == tag_name).first()
