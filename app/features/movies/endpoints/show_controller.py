from uuid import UUID

from fastapi import APIRouter, Depends

from app.common.models.response import BaseResponseModel
from app.features.movies.application.services.show_service import ShowService
from app.module import get_instance

router = APIRouter()


def get_show_service() -> ShowService:
    return get_instance(ShowService)


@router.get("/{show_id}/available-seats", response_model=BaseResponseModel)
def get_available_seats(
    show_id: UUID, service: ShowService = Depends(get_show_service)
):
    """Get available seats for a show"""
    seats = service.get_available_seats(show_id)
    return BaseResponseModel(
        status="success",
        message="Available seats retrieved successfully",
        data={"available_seats": seats},
    )
