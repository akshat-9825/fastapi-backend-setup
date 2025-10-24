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
