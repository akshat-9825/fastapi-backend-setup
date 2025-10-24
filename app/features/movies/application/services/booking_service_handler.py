from uuid import UUID

from app.features.movies.application.models.booking_response_model import (
    BookingCreateModel,
    BookingResponseModel,
)
from app.features.movies.application.services.booking_service import BookingService
from app.features.movies.domain.entities.booking_entity import BookingEntity
from app.features.movies.domain.repository.booking_repository import BookingRepository
from app.features.movies.domain.repository.show_repository import ShowRepository


class BookingServiceHandler(BookingService):
    repository: BookingRepository
    show_repository: ShowRepository

    def get_booking_by_id(self, booking_id: UUID) -> BookingResponseModel | None:
        booking_data = self.repository.get_by_id(booking_id)
        if not booking_data:
            return None
        return BookingResponseModel(**booking_data)

    def create_booking(self, booking: BookingCreateModel) -> BookingResponseModel:
        # Validate seat numbers (1-30)
        for seat_num in booking.seat:
            if seat_num < 1 or seat_num > 30:
                raise ValueError(
                    f"Seat number must be between 1 and 30, got {seat_num}"
                )

        # Check if any of the requested seats are already booked
        booked_seats = self.show_repository.get_booked_seats(booking.show_id)
        requested_seats = set(booking.seat)
        already_booked = requested_seats.intersection(booked_seats)

        if already_booked:
            raise ValueError(
                f"Seats {sorted(already_booked)} are already booked for this show"
            )

        entity = BookingEntity(
            show_id=booking.show_id,
            name=booking.name,
            email=booking.email,
            seat=booking.seat,
        )

        created_entity = self.repository.create(entity)

        # After creating, fetch the full booking with movie details
        booking_data = self.repository.get_by_id(created_entity.booking_id)  # type: ignore
        if not booking_data:
            raise ValueError("Failed to retrieve created booking")

        return BookingResponseModel(**booking_data)
