from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ShowResponseModel(BaseModel):
    show_id: UUID
    movie_id: UUID
    start_time: datetime
    end_time: datetime
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
