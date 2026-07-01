from fastapi import FastAPI
from app.v1.router import router as v1_router
from app.rate_limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI(
    title="Domain Data API",
    version="1.0.0",
    description="API providing high-quality domain constants (properties, vehicles, countries, etc.)"
)

# Register rate limit handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include v1 endpoints
app.include_router(v1_router, prefix="/v1")
