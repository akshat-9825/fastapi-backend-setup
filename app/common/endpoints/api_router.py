"""
API Router aggregator.
Import all feature routers here and register them with prefixes and tags.
"""

from fastapi import APIRouter

from app.features.movies.endpoints import (
    booking_controller,
    movie_controller,
    seat_lock_controller,
    show_controller,
)

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

api_router.include_router(
    show_controller.router,
    prefix="/show",
    tags=["shows"],
)

api_router.include_router(
    booking_controller.router,
    prefix="/booking",
    tags=["bookings"],
)

api_router.include_router(
    seat_lock_controller.router,
    prefix="/seats",
    tags=["seat-locking"],
)
