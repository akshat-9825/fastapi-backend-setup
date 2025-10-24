from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.application.models.movie_details_model import (
    MovieDetailsResponseModel,
)
from app.features.movies.application.models.movie_response_model import (
    MovieResponseModel,
)


class MovieService(ABC, BaseModel):
    @abstractmethod
    def get_movies(self) -> list[MovieResponseModel]:
        pass

    @abstractmethod
    def get_movie_details(self, movie_id: UUID) -> MovieDetailsResponseModel | None:
        pass
