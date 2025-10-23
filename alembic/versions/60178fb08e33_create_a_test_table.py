"""create a test table

Revision ID: 60178fb08e33
Revises:
Create Date: 2025-10-23 20:07:23.298245

"""

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "60178fb08e33"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create schema 'test'
    op.execute("CREATE SCHEMA IF NOT EXISTS test")

    # Create table 'test' in schema 'test'
    op.create_table(
        "test",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="test",
    )
    op.create_index(
        op.f("ix_test_test_id"), "test", ["id"], unique=False, schema="test"
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Drop table 'test' from schema 'test'
    op.drop_index(op.f("ix_test_test_id"), table_name="test", schema="test")
    op.drop_table("test", schema="test")

    # Drop schema 'test'
    op.execute("DROP SCHEMA IF EXISTS test")
