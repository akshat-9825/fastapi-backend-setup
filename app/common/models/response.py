"""Response Models for API endpoints"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class BaseResponseModel(BaseModel):
    """
    Standard response model for all API responses.
    Used for both success and error responses.
    """

    status: str = Field(..., description="Response status (success, error, etc.)")
    message: str = Field(..., description="Human-readable message")
    data: Optional[Any] = Field(None, description="Response payload or error details")

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "status": "success",
                    "message": "Operation completed successfully",
                    "data": {"user_id": 123, "email": "user@example.com"},
                },
                {
                    "status": "error",
                    "message": "Invalid request data",
                    "data": {
                        "error": "ValidationError",
                        "details": {"email": "field required"},
                    },
                },
            ]
        }
