from typing import Any
from uuid import UUID

from app.common.modules.db_module import DB
from app.features.movies.domain.entities.booking_entity import BookingEntity
from app.features.movies.domain.entities.movie_entity import MovieEntity
from app.features.movies.domain.entities.show_entity import ShowEntity
from app.features.movies.domain.repository.booking_repository import BookingRepository


class BookingRepositoryHandler(BookingRepository):
    db: DB

    def get_by_id(self, booking_id: UUID) -> dict[str, Any] | None:
        """Get booking with movie details"""
        with self.db.session() as session:
            result = (
                session.query(
                    BookingEntity.booking_id,
                    BookingEntity.show_id,
                    BookingEntity.name,
                    BookingEntity.email,
                    BookingEntity.seat,
                    BookingEntity.created_at,
                    BookingEntity.updated_at,
                    MovieEntity.title.label("movie_title"),
                    MovieEntity.duration.label("movie_duration"),
                    ShowEntity.start_time,
                    ShowEntity.end_time,
                )
                .join(ShowEntity, BookingEntity.show_id == ShowEntity.show_id)
                .join(MovieEntity, ShowEntity.movie_id == MovieEntity.movie_id)
                .filter(BookingEntity.booking_id == booking_id)
                .first()
            )

            if not result:
                return None

            return {
                "booking_id": result.booking_id,
                "show_id": result.show_id,
                "name": result.name,
                "email": result.email,
                "seat": result.seat,
                "created_at": result.created_at,
                "updated_at": result.updated_at,
                "movie_title": result.movie_title,
                "movie_duration": result.movie_duration,
                "start_time": result.start_time,
                "end_time": result.end_time,
            }

    def create(self, booking: BookingEntity) -> BookingEntity:
        with self.db.session() as session:
            session.add(booking)
            session.commit()
            session.refresh(booking)
            return booking
