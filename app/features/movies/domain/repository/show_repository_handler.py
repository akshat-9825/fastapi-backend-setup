from uuid import UUID

from sqlalchemy import func

from app.common.modules.db_module import DB
from app.features.movies.domain.entities.booking_entity import BookingEntity
from app.features.movies.domain.entities.show_entity import ShowEntity
from app.features.movies.domain.repository.show_repository import ShowRepository


class ShowRepositoryHandler(ShowRepository):
    db: DB

    def get_all(self) -> list[ShowEntity]:
        with self.db.session() as session:
            return session.query(ShowEntity).all()

    def get_by_id(self, show_id: UUID) -> ShowEntity | None:
        with self.db.session() as session:
            return (
                session.query(ShowEntity).filter(ShowEntity.show_id == show_id).first()
            )

    def get_by_movie_id(self, movie_id: UUID) -> list[ShowEntity]:
        with self.db.session() as session:
            return (
                session.query(ShowEntity).filter(ShowEntity.movie_id == movie_id).all()
            )

    def get_available_seats(self, show_id: UUID) -> list[int]:
        """Get available seats for a show (1-30 minus booked seats)"""
        with self.db.session() as session:
            # Get all booked seats for this show
            booked_seats_result = (
                session.query(func.unnest(BookingEntity.seat).label("seat"))
                .filter(BookingEntity.show_id == show_id)
                .all()
            )
            booked_seats = {row.seat for row in booked_seats_result}

            # All seats are 1-30
            all_seats = set(range(1, 31))
            available_seats = all_seats - booked_seats

            return sorted(available_seats)
