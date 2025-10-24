from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class BookingResponseModel(BaseModel):
    booking_id: UUID
    show_id: UUID
    name: str
    email: EmailStr
    seat: list[int]
    movie_title: str
    movie_duration: int
    start_time: datetime
    end_time: datetime
    created_at: datetime | None = None
    updated_at: datetime | None = None


class BookingCreateModel(BaseModel):
    show_id: UUID
    name: str
    email: EmailStr
    seat: list[int]
