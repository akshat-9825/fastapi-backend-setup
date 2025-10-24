from sqlalchemy import TIMESTAMP, Column, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, SMALLINT
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.database import Base


class VisitingEntity(Base):
    __tablename__ = "visiting"
    __table_args__ = {"schema": "movies"}

    id = Column(
        PG_UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    show_id = Column(
        PG_UUID(as_uuid=True), ForeignKey("movies.shows.show_id"), nullable=False
    )
    seat = Column(ARRAY(SMALLINT), nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    expires_at = Column(TIMESTAMP, nullable=False)
