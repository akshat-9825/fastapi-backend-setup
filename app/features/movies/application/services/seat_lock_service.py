from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.application.models.seat_lock_model import (
    SeatLockRequestModel,
    SeatLockResponseModel,
)


class SeatLockService(ABC, BaseModel):
    @abstractmethod
    def lock_seats(self, request: SeatLockRequestModel) -> SeatLockResponseModel:
        pass

    @abstractmethod
    def get_locked_seats(self, show_id: UUID) -> list[int]:
        pass
