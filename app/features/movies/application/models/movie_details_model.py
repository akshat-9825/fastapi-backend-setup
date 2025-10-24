from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ShowWithSeatsModel(BaseModel):
    show_id: UUID
    available_seats: list[int]
    start_time: datetime
    end_time: datetime


class MovieDetailsResponseModel(BaseModel):
    movie_id: UUID
    title: str
    duration: int
    shows: list[ShowWithSeatsModel]
