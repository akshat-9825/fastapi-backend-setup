from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel


class ShowRepository(ABC, BaseModel):
    @abstractmethod
    def get_available_seats(self, show_id: UUID) -> list[int]:
        pass
