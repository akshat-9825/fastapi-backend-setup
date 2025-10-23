"""
Root Dependency Injection Module.

This module automatically discovers and registers all feature modules.
Add new features in app/features/{feature}/modules/module.py
"""

from injector import Injector

from app.common.modules.db_module import DbModule

# Import feature modules here
# Each feature should export its module in app/features/{feature}/modules/module.py
# Example:
# from app.features.users.modules.module import UserModule
# from app.features.products.modules.module import ProductModule

# List all modules to register
FEATURE_MODULES = [
    DbModule(),
    # Add your feature modules here as you create them:
    # UserModule(),
    # ProductModule(),
]

# Create root injector with all modules
injector_instance = Injector(FEATURE_MODULES)


def get_instance(service_class: type):
    """
    Get an instance of a service from the injector.

    Usage in controllers:
        from app.module import get_instance
        from app.features.users.application.services.user_service import UserService

        def get_user_service() -> UserService:
            return get_instance(UserService)

        @router.get("/")
        def endpoint(service: UserService = Depends(get_user_service)):
            ...
    """
    return injector_instance.get(service_class)
