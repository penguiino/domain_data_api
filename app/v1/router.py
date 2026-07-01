from fastapi import APIRouter
from .properties import router as properties_router
from .vehicles import router as vehicles_router
from .countries import router as countries_router

router = APIRouter()

router.include_router(properties_router, prefix="/properties", tags=["Properties"])
router.include_router(vehicles_router, prefix="/vehicles", tags=["Vehicles"])
router.include_router(countries_router, prefix="/countries", tags=["Countries"])
