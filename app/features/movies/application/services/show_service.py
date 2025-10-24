from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.application.models.show_response_model import ShowResponseModel


class ShowService(ABC, BaseModel):
    @abstractmethod
    def get_shows(self) -> list[ShowResponseModel]:
        pass

    @abstractmethod
    def get_show_by_id(self, show_id: UUID) -> ShowResponseModel | None:
        pass

    @abstractmethod
    def get_shows_by_movie(self, movie_id: UUID) -> list[ShowResponseModel]:
        pass

    @abstractmethod
    def get_available_seats(self, show_id: UUID) -> list[int]:
        pass
