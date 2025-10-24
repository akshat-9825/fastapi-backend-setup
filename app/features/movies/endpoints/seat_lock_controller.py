from fastapi import APIRouter, Depends

from app.common.models.response import BaseResponseModel
from app.features.movies.application.models.seat_lock_model import SeatLockRequestModel
from app.features.movies.application.services.seat_lock_service import SeatLockService
from app.module import get_instance

router = APIRouter()


def get_seat_lock_service() -> SeatLockService:
    return get_instance(SeatLockService)


@router.post("/lock-seats", response_model=BaseResponseModel)
def lock_seats(
    request: SeatLockRequestModel,
    service: SeatLockService = Depends(get_seat_lock_service),
):
    """Lock seats temporarily for a user"""
    try:
        locked_seats = service.lock_seats(request)
        return BaseResponseModel(
            status="success",
            message="Seats locked successfully",
            data=locked_seats.model_dump(),
        )
    except ValueError as e:
        return BaseResponseModel(status="error", message=str(e), data=None)
