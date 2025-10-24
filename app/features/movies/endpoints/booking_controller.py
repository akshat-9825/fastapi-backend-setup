from uuid import UUID

from fastapi import APIRouter, Depends

from app.common.models.response import BaseResponseModel
from app.features.movies.application.models.booking_response_model import (
    BookingCreateModel,
)
from app.features.movies.application.services.booking_service import BookingService
from app.module import get_instance

router = APIRouter()


def get_booking_service() -> BookingService:
    return get_instance(BookingService)


@router.get("/{booking_id}", response_model=BaseResponseModel)
def get_booking(
    booking_id: UUID, service: BookingService = Depends(get_booking_service)
):
    """Get a booking by ID with movie details"""
    booking = service.get_booking_by_id(booking_id)
    if not booking:
        return BaseResponseModel(status="error", message="Booking not found", data=None)
    return BaseResponseModel(
        status="success",
        message="Booking retrieved successfully",
        data=booking.model_dump(),
    )


@router.post("/create", response_model=BaseResponseModel)
def create_booking(
    booking: BookingCreateModel,
    service: BookingService = Depends(get_booking_service),
):
    """Create a new booking"""
    try:
        created_booking = service.create_booking(booking)
        return BaseResponseModel(
            status="success",
            message="Booking created successfully",
            data=created_booking.model_dump(),
        )
    except ValueError as e:
        return BaseResponseModel(status="error", message=str(e), data=None)
