from abc import ABC, abstractmethod

from app.common.models.base_model import BaseModel
from app.features.movies.application.models.movie_response_model import (
    MovieResponseModel,
)


class MovieService(ABC, BaseModel):
    @abstractmethod
    def get_movies(self) -> list[MovieResponseModel]:
        pass
