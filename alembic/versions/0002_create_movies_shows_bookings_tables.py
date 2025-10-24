"""create movies shows bookings tables

Revision ID: 0002
Revises: 0001
Create Date: 2025-10-24 00:00:00.000000

"""

from collections.abc import Sequence
from typing import Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0002"
down_revision: Union[str, Sequence[str], None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Enable UUID extension
    op.execute("""
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
    """)

    # Create movies schema
    op.execute("""
        CREATE SCHEMA IF NOT EXISTS movies
    """)

    # Create Movies table
    op.execute("""
        CREATE TABLE movies.movies (
            movie_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            title VARCHAR(255) NOT NULL,
            duration INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create Shows table
    op.execute("""
        CREATE TABLE movies.shows (
            show_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            movie_id UUID NOT NULL,
            start_time TIMESTAMP NOT NULL,
            end_time TIMESTAMP NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_shows_movie
                FOREIGN KEY (movie_id)
                REFERENCES movies.movies(movie_id)
                ON DELETE CASCADE
        )
    """)

    # Create Bookings table
    op.execute("""
        CREATE TABLE movies.bookings (
            booking_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            show_id UUID NOT NULL,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            seat SMALLINT[] NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_bookings_show
                FOREIGN KEY (show_id)
                REFERENCES movies.shows(show_id)
                ON DELETE CASCADE
        )
    """)

    # Create indexes for foreign keys
    op.execute("""
        CREATE INDEX idx_shows_movie_id ON movies.shows(movie_id)
    """)

    op.execute("""
        CREATE INDEX idx_bookings_show_id ON movies.bookings(show_id)
    """)

    # Create index for email lookups
    op.execute("""
        CREATE INDEX idx_bookings_email ON movies.bookings(email)
    """)


def downgrade() -> None:
    """Downgrade schema."""
    # Drop schema with all tables (CASCADE will drop all objects in the schema)
    op.execute("DROP SCHEMA IF EXISTS movies CASCADE")
