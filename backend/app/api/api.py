from fastapi import APIRouter

from app.api.endpoints import testes

api_router = APIRouter()

api_router.include_router(testes.router, prefix="/testes", tags=["testes"])

