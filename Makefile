.PHONY: help install run dev test clean add remove shell env-info lint format check migrate-create migrate-up migrate-down migrate-history

# Default target
help:
	@echo "FastAPI Backend Setup - Available Commands"
	@echo "=========================================="
	@echo "make install       - Install all dependencies using Poetry"
	@echo "make run          - Run the application"
	@echo "make dev          - Run the application with auto-reload"
	@echo "make shell        - Activate Poetry virtual environment"
	@echo "make add PKG=name - Add a new package"
	@echo "make remove PKG=name - Remove a package"
	@echo "make env-info     - Show virtual environment information"
	@echo "make lint         - Run Ruff linter"
	@echo "make format       - Format code with Ruff"
	@echo "make check        - Run linter and check formatting"
	@echo "make migrate-create MSG=message - Create new migration"
	@echo "make migrate-up   - Run all pending migrations"
	@echo "make migrate-down - Downgrade by one migration"
	@echo "make migrate-history - Show migration history"
	@echo "make clean        - Remove cache and temporary files"
	@echo "make test         - Run tests (when test suite is added)"

# Install dependencies
install:
	@echo "Installing dependencies..."
	poetry install

# Run the application (production mode)
run:
	@echo "Starting FastAPI application..."
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

# Run the application with auto-reload (development mode)
dev:
	@echo "Starting FastAPI application in development mode..."
	poetry run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Activate Poetry shell
shell:
	@echo "Activating Poetry shell..."
	poetry shell

# Add a package
add:
ifndef PKG
	@echo "Error: Please specify a package name using PKG=package-name"
	@exit 1
endif
	@echo "Adding package: $(PKG)"
	poetry add $(PKG)

# Remove a package
remove:
ifndef PKG
	@echo "Error: Please specify a package name using PKG=package-name"
	@exit 1
endif
	@echo "Removing package: $(PKG)"
	poetry remove $(PKG)

# Show virtual environment info
env-info:
	@echo "Virtual Environment Information:"
	@echo "================================"
	poetry env info

# Run Ruff linter
lint:
	@echo "Running Ruff linter..."
	poetry run ruff check .

# Format code with Ruff
format:
	@echo "Formatting code with Ruff..."
	poetry run ruff check --fix .
	poetry run ruff format .

# Check linting and formatting without making changes
check:
	@echo "Checking code quality..."
	poetry run ruff check .
	poetry run ruff format --check .

# Create a new migration
migrate-create:
ifndef MSG
	@echo "Error: Please specify a message using MSG='your message'"
	@echo "Example: make migrate-create MSG='create users table'"
	@exit 1
endif
	@echo "Creating new migration: $(MSG)"
	poetry run alembic revision --autogenerate -m "$(MSG)"

# Run all pending migrations (upgrade to latest)
migrate-up:
	@echo "Running migrations..."
	poetry run alembic upgrade head

# Downgrade by one migration
migrate-down:
	@echo "Downgrading last migration..."
	poetry run alembic downgrade -1

# Show migration history
migrate-history:
	@echo "Migration History:"
	@echo "=================="
	poetry run alembic history --verbose

# Clean cache and temporary files
clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup complete!"

# Run tests (placeholder for when tests are added)
test:
	@echo "Running tests..."
	@echo "Note: Add pytest to the project first with 'make add PKG=pytest'"
	# poetry run pytest tests/ -v

