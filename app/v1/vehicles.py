from fastapi import APIRouter, Request
from app.dependencies import load_json
from app.auth import require_api_key
from app.rate_limiter import limiter


router = APIRouter()

@router.get("/body-types")
@limiter.limit("60/minute")
def vehicle_body_types(request: Request):
    require_api_key(request)
    return load_json("app/data/vehicles/body_types.json")

@router.get("/fuel-types")
@limiter.limit("60/minute")
def vehicle_fuel_types(request: Request):
    require_api_key(request)
    return load_json("app/data/vehicles/fuel_types.json")

@router.get("/transmissions")
@limiter.limit("60/minute")
def vehicle_transmissions(request: Request):
    require_api_key(request)
    return load_json("app/data/vehicles/transmissions.json")
