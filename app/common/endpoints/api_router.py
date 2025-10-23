"""
API Router aggregator.
Import all feature routers here and register them with prefixes and tags.
"""

from fastapi import APIRouter

# Import feature routers as you create them:
# from app.features.users.endpoints import user_controller
# from app.features.auth.endpoints import auth_controller
# from app.features.products.endpoints import product_controller

api_router = APIRouter()

# Register feature routers with their prefixes and tags
# Example:
# api_router.include_router(
#     user_controller.router,
#     prefix="/v1/users",
#     tags=["users"]
# )
#
# api_router.include_router(
#     auth_controller.router,
#     prefix="/v1/auth",
#     tags=["authentication"]
# )
