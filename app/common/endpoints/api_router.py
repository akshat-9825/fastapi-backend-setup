"""
API Router aggregator.
Import all feature routers here and register them with prefixes and tags.
"""

from fastapi import APIRouter

from app.features.movies.endpoints import movie_controller

# Import feature routers as you create them:
# from app.features.users.endpoints import user_controller
# from app.features.auth.endpoints import auth_controller
# from app.features.products.endpoints import product_controller

api_router = APIRouter()

api_router.include_router(
    movie_controller.api_router,
    prefix="/movies",
    tags=["movies"],
)
