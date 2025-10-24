from abc import ABC, abstractmethod

from app.common.models.base_model import BaseModel
from app.features.movies.domain.entities.movie_entity import MovieEntity


class MovieRepository(ABC, BaseModel):
    @abstractmethod
    def get_all(self) -> list[MovieEntity]:
        pass
