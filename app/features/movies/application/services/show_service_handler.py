from uuid import UUID

from app.features.movies.application.services.show_service import ShowService
from app.features.movies.domain.repository.show_repository import ShowRepository


class ShowServiceHandler(ShowService):
    repository: ShowRepository

    def get_available_seats(self, show_id: UUID) -> list[int]:
        return self.repository.get_available_seats(show_id)
