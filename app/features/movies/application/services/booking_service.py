from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.application.models.booking_response_model import (
    BookingCreateModel,
    BookingResponseModel,
)


class BookingService(ABC, BaseModel):
    @abstractmethod
    def get_booking_by_id(self, booking_id: UUID) -> BookingResponseModel | None:
        pass

    @abstractmethod
    def create_booking(self, booking: BookingCreateModel) -> BookingResponseModel:
        pass
