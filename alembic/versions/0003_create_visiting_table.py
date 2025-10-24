"""create visiting table

Revision ID: 0003
Revises: 0002
Create Date: 2025-10-24 00:00:00.000000

"""

from collections.abc import Sequence
from typing import Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0003"
down_revision: Union[str, Sequence[str], None] = "0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create Visiting table for temporary seat locking
    op.execute("""
        CREATE TABLE movies.visiting (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            show_id UUID NOT NULL,
            seat SMALLINT[] NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL,
            CONSTRAINT fk_visiting_show
                FOREIGN KEY (show_id)
                REFERENCES movies.shows(show_id)
                ON DELETE CASCADE
        )
    """)

    # Create index on show_id for faster queries
    op.execute("""
        CREATE INDEX idx_visiting_show_id ON movies.visiting(show_id)
    """)

    # Create index on expires_at for efficient cleanup of expired locks
    op.execute("""
        CREATE INDEX idx_visiting_expires_at ON movies.visiting(expires_at)
    """)


def downgrade() -> None:
    """Downgrade schema."""
    # Drop indexes first
    op.execute("DROP INDEX IF EXISTS movies.idx_visiting_expires_at")
    op.execute("DROP INDEX IF EXISTS movies.idx_visiting_show_id")

    # Drop table
    op.execute("DROP TABLE IF EXISTS movies.visiting CASCADE")
