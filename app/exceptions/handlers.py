"""Exception handler implementations."""

from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

from app.common.models.response import BaseResponseModel


def exception_handler(request: Request, exception: Exception) -> JSONResponse:
    """
    Universal exception handler for all exceptions.
    Handles RequestValidationError, custom exceptions, and unexpected errors.
    """
    request_id = getattr(request.state, "request_id", "")

    # Handle validation errors
    if isinstance(exception, RequestValidationError):
        status_code = status.HTTP_400_BAD_REQUEST
        error_name = "ValidationError"
        message = "Invalid request data"
        errors = exception.errors()

        # Format validation errors nicely
        error_details = {
            ".".join(
                map(str, err["loc"][1:] if err["loc"][0] == "body" else err["loc"])
            ): err["msg"]
            for err in errors
        }

        logger.warning(
            f"Validation error on {request.method} {request.url.path}",
            request_id=request_id,
            errors=error_details,
        )

        return JSONResponse(
            status_code=status_code,
            content=BaseResponseModel(
                status="error",
                message=message,
                data={"error": error_name, "details": error_details},
            ).model_dump(),
        )

    # Handle ValueError (bad input)
    elif isinstance(exception, ValueError):
        status_code = status.HTTP_400_BAD_REQUEST
        error_name = exception.__class__.__name__
        message = str(exception)

        logger.warning(
            f"ValueError on {request.method} {request.url.path}: {message}",
            request_id=request_id,
        )

        return JSONResponse(
            status_code=status_code,
            content=BaseResponseModel(
                status="error",
                message=message,
                data={"error": error_name},
            ).model_dump(),
        )

    # Handle all other unexpected errors
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        error_name = exception.__class__.__name__
        message = "An unexpected error occurred"

        # Log full traceback for internal server errors
        logger.error(
            f"Unhandled exception on {request.method} {request.url.path}",
            request_id=request_id,
            exc_info=True,
        )

        return JSONResponse(
            status_code=status_code,
            content=BaseResponseModel(
                status="error",
                message=message,
                data={"error": error_name},
            ).model_dump(),
        )
