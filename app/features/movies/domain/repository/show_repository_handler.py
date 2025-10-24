from uuid import UUID

from sqlalchemy import func

from app.common.modules.db_module import DB
from app.features.movies.domain.entities.booking_entity import BookingEntity
from app.features.movies.domain.entities.show_entity import ShowEntity
from app.features.movies.domain.repository.show_repository import ShowRepository


class ShowRepositoryHandler(ShowRepository):
    db: DB

    def get_by_movie_id(self, movie_id: UUID) -> list[ShowEntity]:
        with self.db.session() as session:
            return (
                session.query(ShowEntity).filter(ShowEntity.movie_id == movie_id).all()
            )

    def get_booked_seats(self, show_id: UUID) -> set[int]:
        """Get all booked seats for a show"""
        with self.db.session() as session:
            booked_seats_result = (
                session.query(func.unnest(BookingEntity.seat).label("seat"))
                .filter(BookingEntity.show_id == show_id)
                .all()
            )
            return {row.seat for row in booked_seats_result}

    def get_available_seats_bulk(self, show_ids: list[UUID]) -> dict[UUID, list[int]]:
        """Get available seats for multiple shows in one optimized query"""
        if not show_ids:
            return {}

        with self.db.session() as session:
            # Get all booked seats for all shows in one query
            booked_seats_result = (
                session.query(
                    BookingEntity.show_id,
                    func.unnest(BookingEntity.seat).label("seat"),
                )
                .filter(BookingEntity.show_id.in_(show_ids))
                .all()
            )

            # Group booked seats by show_id
            booked_by_show: dict[UUID, set[int]] = {
                show_id: set() for show_id in show_ids
            }
            for row in booked_seats_result:
                booked_by_show[row.show_id].add(row.seat)

            # Calculate available seats for each show
            all_seats = set(range(1, 31))
            available_by_show = {}
            for show_id in show_ids:
                booked_seats = booked_by_show.get(show_id, set())
                available_seats = all_seats - booked_seats
                available_by_show[show_id] = sorted(available_seats)

            return available_by_show

    def get_available_seats(self, show_id: UUID) -> list[int]:
        """Get available seats for a single show"""
        result = self.get_available_seats_bulk([show_id])
        return result.get(show_id, list(range(1, 31)))
