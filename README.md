# FastAPI Backend Setup

A production-ready FastAPI boilerplate with Poetry for dependency management.

## Features

- ✨ **FastAPI** - Modern, fast web framework for building APIs
- 📦 **Poetry** - Dependency management and packaging
- ⚙️ **Pydantic** - Data validation using Python type annotations
- 🚀 **Uvicorn** - Lightning-fast ASGI server
- 🔧 **Configuration Management** - Environment-based configuration with pydantic-settings
- 🎨 **Ruff** - Extremely fast Python linter and formatter (replaces Black, isort, flake8)
- 🗄️ **SQLAlchemy + PostgreSQL** - Powerful ORM with PostgreSQL support
- 🔄 **Alembic** - Database migration management
- 📝 **Loguru** - Beautiful, easy-to-use logging (no more print statements!)
- 🛡️ **Exception Handling** - Global error handlers with consistent API responses
- 🌐 **CORS Middleware** - Pre-configured CORS support

## Prerequisites

- Python 3.9 or higher
- Poetry (install from [python-poetry.org](https://python-poetry.org/docs/#installation))

## Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd fastapi-backend-setup
   ```

2. **Install dependencies using Poetry**

   ```bash
   poetry install
   ```

   Poetry will automatically:

   - Create a virtual environment
   - Install all dependencies
   - Set up the project

3. **Create environment file** (optional)
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to configure your application settings.

## Running the Application

### Using Makefile (Recommended)

```bash
# Development mode with auto-reload
make dev

# Production mode
make run

# See all available commands
make help
```

### Using Poetry

```bash
poetry run uvicorn app.main:app --reload
```

### Using Poetry Shell

```bash
poetry shell
uvicorn app.main:app --reload
```

The application will be available at:

- API: http://localhost:8000
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## API Endpoints

### Health Check

```
GET /health
```

Returns the health status of the application.

**Response:**

```json
{
  "status": "healthy",
  "service": "fastapi-backend-setup",
  "version": "1.0.0"
}
```

### Root

```
GET /
```

Returns a welcome message.

## Project Structure

```
fastapi-backend-setup/
├── app/
│   ├── __init__.py      # Makes app a Python package
│   ├── main.py          # Application entry point
│   └── config.py        # Configuration management
├── .vscode/
│   ├── launch.json      # VS Code debug configurations
│   └── settings.json    # VS Code workspace settings
├── pyproject.toml       # Poetry configuration
├── poetry.lock          # Locked dependencies
├── Makefile            # Common development commands
├── .env                # Environment variables (git-ignored)
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

### Why `__init__.py`?

The `app/__init__.py` file is essential as it makes the `app` directory a Python package. This allows you to:

- Import modules using `from app.main import app`
- Organize your code into a proper package structure
- Enable relative imports between modules within the `app` package

## Development

### Makefile Commands

The project includes a Makefile with common development tasks:

```bash
make help          # Show all available commands
make install       # Install all dependencies
make dev           # Run with auto-reload (development)
make run           # Run in production mode
make shell         # Activate Poetry virtual environment
make add PKG=name  # Add a new package (e.g., make add PKG=pytest)
make remove PKG=name  # Remove a package
make env-info      # Show virtual environment information
make lint          # Run Ruff linter
make format        # Format code with Ruff
make check         # Check linting and formatting (no changes)
make migrate-create MSG="message" # Create new database migration
make migrate-up    # Run all pending migrations
make migrate-down  # Rollback last migration
make migrate-history # Show migration history
make clean         # Remove cache and temporary files
make test          # Run tests (when added)
```

### Poetry Commands

```bash
# Adding Dependencies
poetry add <package-name>

# Adding Development Dependencies
poetry add --group dev <package-name>

# View Virtual Environment Info
poetry env info

# Activate Virtual Environment
poetry shell
```

### Code Quality with Ruff

Ruff is configured as both linter and formatter. It's extremely fast and replaces multiple tools (Black, isort, flake8, etc.):

```bash
# Run linter to check for issues
make lint

# Auto-fix issues and format code
make format

# Check without making changes (useful for CI/CD)
make check
```

**VS Code Integration:**

- Install the [Ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- Code will auto-format on save
- Linting errors will appear inline

Configuration is in `ruff.toml`.

### VS Code Debugging

The project includes VS Code debug configurations in `.vscode/launch.json`:

1. **FastAPI: Debug** - Run with auto-reload and debugging
2. **FastAPI: Debug (No Reload)** - Run without auto-reload (better for breakpoints)
3. **Python: Current File** - Debug the currently open Python file

To debug:

1. Open VS Code
2. Go to Run and Debug (Cmd+Shift+D / Ctrl+Shift+D)
3. Select a configuration from the dropdown
4. Press F5 or click the green play button
5. Set breakpoints by clicking in the gutter next to line numbers

**Virtual Environment Setup:**

- The `.venv` folder is created in your project directory
- VS Code should auto-detect it when you open the project
- If not, press `Cmd/Ctrl+Shift+P` → "Python: Select Interpreter" → Choose `.venv/bin/python`

## Configuration

Configuration is managed through environment variables and the `app/config.py` file. Available settings:

- `APP_NAME`: Application name (default: "FastAPI Backend Setup")
- `APP_VERSION`: Application version (default: "1.0.0")
- `DEBUG`: Debug mode (default: True)
- `HOST`: Server host (default: "0.0.0.0")
- `PORT`: Server port (default: 8000)
- `DATABASE_URL`: PostgreSQL connection string (required, no default)
- `DATABASE_ECHO`: Echo SQL queries to console (default: False)
- `CORS_ORIGINS`: Allowed CORS origins (default: ["*"] - all origins)
- `CORS_CREDENTIALS`: Allow credentials in CORS (default: True)
- `CORS_METHODS`: Allowed HTTP methods (default: ["*"] - all methods)
- `CORS_HEADERS`: Allowed headers (default: ["*"] - all headers)

## Database Migrations

This project uses **Alembic** for database migrations.

**Quick Start:**

```bash
# Create a new migration
make migrate-create MSG="create users table"

# Run migrations
make migrate-up

# Rollback
make migrate-down

# View history
make migrate-history
```

See `.cursor/rules.mdc` for complete migration workflow and best practices.

## Expanding the Boilerplate

This boilerplate is designed to be easily extended. Consider adding:

- **Database entities** - Create your tables in `app/entities/`
- **Authentication** (JWT, OAuth2)
- **API routers** for organizing endpoints
- **Middleware** (CORS, logging, error handling)
- **Testing** (pytest)
- **Docker** support
- **CI/CD** pipelines

## License

[Add your license here]
