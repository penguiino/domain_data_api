from fastapi import APIRouter, Request
from app.dependencies import load_json
from app.auth import require_api_key
from app.rate_limiter import limiter


router = APIRouter()

@router.get("/types")
@limiter.limit("60/minute")
def property_types(request: Request):
    require_api_key(request)
    return load_json("app/data/properties/types.json")

@router.get("/amenities")
@limiter.limit("60/minute")
def property_amenities(request: Request):
    require_api_key(request)
    return load_json("app/data/properties/amenities.json")

@router.get("/furnishing")
@limiter.limit("60/minute")
def furnishing_levels(request: Request):
    require_api_key(request)
    return load_json("app/data/properties/furnishing.json")
