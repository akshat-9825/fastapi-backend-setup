from uuid import UUID

from sqlalchemy import func

from app.common.modules.db_module import DB
from app.features.movies.domain.entities.booking_entity import BookingEntity
from app.features.movies.domain.repository.show_repository import ShowRepository


class ShowRepositoryHandler(ShowRepository):
    db: DB

    def get_booked_seats(self, show_id: UUID) -> set[int]:
        """Get all booked seats for a show"""
        with self.db.session() as session:
            booked_seats_result = (
                session.query(func.unnest(BookingEntity.seat).label("seat"))
                .filter(BookingEntity.show_id == show_id)
                .all()
            )
            return {row.seat for row in booked_seats_result}

    def get_available_seats(self, show_id: UUID) -> list[int]:
        """Get available seats for a show (1-30 minus booked seats)"""
        booked_seats = self.get_booked_seats(show_id)

        # All seats are 1-30
        all_seats = set(range(1, 31))
        available_seats = all_seats - booked_seats

        return sorted(available_seats)
