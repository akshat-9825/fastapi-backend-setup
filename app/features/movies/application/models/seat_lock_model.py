from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SeatLockRequestModel(BaseModel):
    show_id: UUID
    seat: list[int]
    expires_in_minutes: int = 10  # Default 10 minutes lock


class SeatLockResponseModel(BaseModel):
    id: UUID
    show_id: UUID
    seat: list[int]
    expires_at: datetime
