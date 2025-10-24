from uuid import UUID

from fastapi import APIRouter, Depends

from app.common.models.response import BaseResponseModel
from app.features.movies.application.services.movie_service import MovieService
from app.module import get_instance

api_router = APIRouter()


def get_movie_service():
    return get_instance(MovieService)


@api_router.get("/fetch", response_model=BaseResponseModel)
def get_movies(service: MovieService = Depends(get_movie_service)):
    """Get all movies."""
    movies = service.get_movies()
    return BaseResponseModel(
        status="success", message="Movies fetched successfully", data=movies
    )


@api_router.get("/{movie_id}", response_model=BaseResponseModel)
def get_movie_details(
    movie_id: UUID, service: MovieService = Depends(get_movie_service)
):
    """Get movie details with all shows and available seats"""
    movie_details = service.get_movie_details(movie_id)
    if not movie_details:
        return BaseResponseModel(status="error", message="Movie not found", data=None)
    return BaseResponseModel(
        status="success",
        message="Movie details retrieved successfully",
        data=movie_details.model_dump(),
    )
