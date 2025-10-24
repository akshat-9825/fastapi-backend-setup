from abc import ABC, abstractmethod
from uuid import UUID

from app.common.models.base_model import BaseModel
from app.features.movies.domain.entities.visiting_entity import VisitingEntity


class VisitingRepository(ABC, BaseModel):
    @abstractmethod
    def create(self, visiting: VisitingEntity) -> VisitingEntity:
        pass

    @abstractmethod
    def get_locked_seats(self, show_id: UUID) -> set[int]:
        """Get all currently locked seats for a show (not expired)"""
        pass

    @abstractmethod
    def cleanup_expired(self, show_id: UUID) -> None:
        """Remove expired visiting records for a show"""
        pass
