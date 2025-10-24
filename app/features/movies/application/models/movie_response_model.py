from uuid import UUID

from pydantic import BaseModel, Field


class MovieResponseModel(BaseModel):
    movie_id: UUID = Field(..., description="The unique identifier for the movie")
    title: str = Field(..., description="The title of the movie")
    duration: int = Field(..., description="The duration of the movie in minutes")
