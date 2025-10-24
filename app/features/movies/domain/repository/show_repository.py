from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.domain.entities.show_entity import ShowEntity


class ShowRepository(ABC, BaseModel):
    @abstractmethod
    def get_by_movie_id(self, movie_id: UUID) -> list[ShowEntity]:
        pass

    @abstractmethod
    def get_available_seats(self, show_id: UUID) -> list[int]:
        pass

    @abstractmethod
    def get_available_seats_bulk(self, show_ids: list[UUID]) -> dict[UUID, list[int]]:
        """Get available seats for multiple shows in one query"""
        pass

    @abstractmethod
    def get_booked_seats(self, show_id: UUID) -> set[int]:
        """Get all booked seats for a show"""
        pass
