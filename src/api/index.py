from fastapi import APIRouter
from src.api.v1.index import v1_router

api_router = router = APIRouter()

api_router.include_router(v1_router, prefix='/v1')