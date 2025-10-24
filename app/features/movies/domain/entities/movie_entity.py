from sqlalchemy import TIMESTAMP, UUID, Column, Integer, String

from app.database import Base


class MovieEntity(Base):
    __tablename__ = "movies"
    __table_args__ = {"schema": "movies"}

    movie_id = Column(UUID, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
