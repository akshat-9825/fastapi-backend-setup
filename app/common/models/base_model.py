"""Base Model for services and repositories"""

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict


class BaseModel(PydanticBaseModel):
    """
    Base model for services and repositories.
    Allows creation from ORM models and arbitrary types (like DB connections).
    """

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        use_enum_values=True,
    )
