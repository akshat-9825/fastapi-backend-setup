from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.domain.entities.booking_entity import BookingEntity


class BookingRepository(ABC, BaseModel):
    @abstractmethod
    def get_by_id(self, booking_id: UUID) -> dict[str, Any] | None:
        """Get booking with movie details"""
        pass

    @abstractmethod
    def create(self, booking: BookingEntity) -> BookingEntity:
        pass
