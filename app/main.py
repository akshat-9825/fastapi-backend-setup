"""FastAPI Application Entry Point"""

from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app.database import get_db

app = FastAPI(
    title="FastAPI Backend Setup",
    description="A standard FastAPI boilerplate for any project",
    version="1.0.0",
)


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Backend Setup"}


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "fastapi-backend-setup",
            "version": "1.0.0",
        },
    )


@app.get("/db/check")
def check_database(db: Session = Depends(get_db)):
    """
    Check database connection.
    Simple endpoint to verify database is accessible.
    """
    try:
        # Test database connection
        result = db.execute(text("SELECT 1")).scalar()
        return {
            "status": "connected",
            "message": "Database connection successful",
            "test_query_result": result,
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)},
        )
