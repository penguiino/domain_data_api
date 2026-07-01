from fastapi import APIRouter, Request
from app.dependencies import load_json
from app.auth import require_api_key
from app.rate_limiter import limiter


router = APIRouter()

@router.get("/")
@limiter.limit("60/minute")
def countries(request: Request):
    require_api_key(request)
    return load_json("app/data/countries/list.json")

@router.get("/languages")
@limiter.limit("60/minute")
def country_languages(request: Request):
    require_api_key(request)
    return load_json("app/data/countries/languages.json")
