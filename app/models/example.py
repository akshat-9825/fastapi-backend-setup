"""Example Model

This is an example model to demonstrate SQLAlchemy usage.
Delete or modify this file as needed for your project.
"""

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Example(Base):
    """
    Example model for demonstration purposes.

    To use this model:
    1. Uncomment the import in app/models/__init__.py
    2. Uncomment the import in alembic/env.py
    3. Create a migration: make migrate-create MSG="create example table"
    4. Run migration: make migrate-up
    """

    __tablename__ = "examples"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<Example(id={self.id}, name='{self.name}')>"
