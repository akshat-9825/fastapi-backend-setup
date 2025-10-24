from sqlalchemy import TIMESTAMP, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY, SMALLINT
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.database import Base


class BookingEntity(Base):
    __tablename__ = "bookings"
    __table_args__ = {"schema": "movies"}

    booking_id = Column(
        PG_UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    show_id = Column(
        PG_UUID(as_uuid=True), ForeignKey("movies.shows.show_id"), nullable=False
    )
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    seat = Column(ARRAY(SMALLINT), nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
