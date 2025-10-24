from uuid import UUID

from app.features.movies.application.services.seat_lock_service import SeatLockService
from app.features.movies.application.services.show_service import ShowService
from app.features.movies.domain.repository.show_repository import ShowRepository


class ShowServiceHandler(ShowService):
    repository: ShowRepository
    seat_lock_service: SeatLockService

    def get_available_seats(self, show_id: UUID) -> list[int]:
        # Get available seats from repository (excludes booked seats)
        available_seats = self.repository.get_available_seats(show_id)

        # Get locked seats from seat lock service
        locked_seats = self.seat_lock_service.get_locked_seats(show_id)

        # Remove locked seats from available seats
        available_set = set(available_seats) - set(locked_seats)

        return sorted(available_set)
