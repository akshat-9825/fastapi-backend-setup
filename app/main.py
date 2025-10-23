"""FastAPI Application Entry Point"""

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.common.endpoints.api_router import api_router
from app.common.models.response import BaseResponseModel
from app.config import settings
from app.database import get_db
from app.exceptions.handlers import exception_handler

app = FastAPI(
    title="FastAPI Backend Setup",
    description="A standard FastAPI boilerplate for any project",
    version="1.0.0",
)

# CORS Middleware - Configure via settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)


# Register exception handlers using decorators
@app.exception_handler(Exception)
@app.exception_handler(RequestValidationError)
async def global_exception_handler(request: Request, exception: Exception):
    """Wrapper to handle all exceptions using the universal exception_handler."""
    return exception_handler(request, exception)


app.include_router(api_router, prefix="/api")


@app.get("/", response_model=BaseResponseModel)
def root():
    """Root endpoint"""
    logger.info("Root endpoint accessed")
    return BaseResponseModel(
        status="success",
        message="Welcome to FastAPI Backend Setup",
        data={"version": "1.0.0"},
    )


@app.get("/health", response_model=BaseResponseModel)
def health_check():
    """Health check endpoint"""
    return BaseResponseModel(
        status="healthy",
        message="Service is running",
        data={
            "service": "fastapi-backend-setup",
            "version": "1.0.0",
        },
    )


@app.get("/db/check", response_model=BaseResponseModel)
def check_database(db: Session = Depends(get_db)):
    """
    Check database connection.
    Simple endpoint to verify database is accessible.
    """
    try:
        result = db.execute(text("SELECT 1")).scalar()
        logger.info("Database connection successful")
        return BaseResponseModel(
            status="connected",
            message="Database connection successful",
            data={"test_query_result": result},
        )
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise e
