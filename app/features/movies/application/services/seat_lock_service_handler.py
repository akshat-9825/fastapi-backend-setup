from datetime import datetime, timedelta, timezone
from uuid import UUID

from app.features.movies.application.models.seat_lock_model import (
    SeatLockRequestModel,
    SeatLockResponseModel,
)
from app.features.movies.application.services.seat_lock_service import SeatLockService
from app.features.movies.domain.entities.visiting_entity import VisitingEntity
from app.features.movies.domain.repository.show_repository import ShowRepository
from app.features.movies.domain.repository.visiting_repository import VisitingRepository


class SeatLockServiceHandler(SeatLockService):
    repository: VisitingRepository
    show_repository: ShowRepository

    def _validate_seat_numbers(self, seats: list[int]) -> None:
        """Validate that all seat numbers are in valid range (1-30)"""
        for seat_num in seats:
            if seat_num < 1 or seat_num > 30:
                raise ValueError(
                    f"Seat number must be between 1 and 30, got {seat_num}"
                )

    def _check_already_booked_seats(
        self, show_id: UUID, requested_seats: set[int]
    ) -> None:
        """Check if any requested seats are already booked"""
        booked_seats = self.show_repository.get_booked_seats(show_id)
        already_booked = requested_seats.intersection(booked_seats)

        if already_booked:
            raise ValueError(
                f"Seats {sorted(already_booked)} are already booked and cannot be locked"
            )

    def _check_already_locked_seats(
        self, show_id: UUID, requested_seats: set[int]
    ) -> None:
        """Check if any requested seats are already locked by someone else"""
        locked_seats = set(self.repository.get_locked_seats(show_id))
        already_locked = requested_seats.intersection(locked_seats)

        if already_locked:
            raise ValueError(
                f"Seats {sorted(already_locked)} are already locked by another user"
            )

    def _calculate_expiration_time(self, expires_in_minutes: int) -> datetime:
        """Calculate expiration time from current time"""
        return datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)

    def _create_lock_entity(
        self, show_id: UUID, seats: list[int], expires_at: datetime
    ) -> VisitingEntity:
        """Create and persist a lock entity"""
        entity = VisitingEntity(show_id=show_id, seat=seats, expires_at=expires_at)
        return self.repository.create(entity)

    def lock_seats(self, request: SeatLockRequestModel) -> SeatLockResponseModel:
        """Lock seats for a show with validation"""
        # Validate seat numbers
        self._validate_seat_numbers(request.seat)

        # Cleanup expired locks for this show
        self.repository.cleanup_expired(request.show_id)

        # Check availability
        requested_seats = set(request.seat)
        self._check_already_booked_seats(request.show_id, requested_seats)
        self._check_already_locked_seats(request.show_id, requested_seats)

        # Create lock
        expires_at = self._calculate_expiration_time(request.expires_in_minutes)
        created_entity = self._create_lock_entity(
            request.show_id, request.seat, expires_at
        )

        return SeatLockResponseModel(
            id=created_entity.id,  # type: ignore
            show_id=created_entity.show_id,  # type: ignore
            seat=created_entity.seat,  # type: ignore
            expires_at=created_entity.expires_at,  # type: ignore
        )

    def get_locked_seats(self, show_id: UUID) -> list[int]:
        # Cleanup expired locks before fetching
        self.repository.cleanup_expired(show_id)
        locked_seats = self.repository.get_locked_seats(show_id)
        return sorted(locked_seats)
