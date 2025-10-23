"""Alembic Environment Configuration"""

import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# Import our application's database configuration
from app.config import settings
from app.database import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config


def get_next_revision_id():
    """Generate sequential revision ID."""
    versions_dir = os.path.join(os.path.dirname(__file__), "versions")
    if not os.path.exists(versions_dir):
        return "0001"

    existing_files = [
        f for f in os.listdir(versions_dir) if f.endswith(".py") and f != "__pycache__"
    ]

    if not existing_files:
        return "0001"

    # Extract numbers from filenames
    numbers = []
    for filename in existing_files:
        try:
            # Try to extract number from start of filename
            num_str = filename.split("_")[0]
            if num_str.isdigit():
                numbers.append(int(num_str))
        except (ValueError, IndexError):
            pass

    if numbers:
        next_num = max(numbers) + 1
        return f"{next_num:04d}"
    else:
        return "0001"


# Set the revision ID generator
def process_revision_directives(_context, _revision, directives):
    """Use sequential numbers for revision IDs."""
    if directives:
        directives[0].rev_id = get_next_revision_id()


config = context.config

# Override sqlalchemy.url with our settings
config.set_main_option("sqlalchemy.url", settings.database_url)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target_metadata to our Base.metadata for autogenerate support
# Import all entities here to ensure they're registered with Base
# from app.entities import user, post  # Add your entities as you create them
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
