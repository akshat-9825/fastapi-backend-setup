"""FastAPI Application Entry Point"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI application instance
app = FastAPI(
    title="FastAPI Backend Setup",
    description="A standard FastAPI boilerplate for any project",
    version="1.0.0",
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Backend Setup"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "fastapi-backend-setup",
            "version": "1.0.0",
        },
    )
