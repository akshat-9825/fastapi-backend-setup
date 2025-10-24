from sqlalchemy import TIMESTAMP, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.database import Base


class ShowEntity(Base):
    __tablename__ = "shows"
    __table_args__ = {"schema": "movies"}

    show_id = Column(
        PG_UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    movie_id = Column(
        PG_UUID(as_uuid=True), ForeignKey("movies.movies.movie_id"), nullable=False
    )
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
