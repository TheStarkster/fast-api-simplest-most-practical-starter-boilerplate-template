from fastapi import APIRouter
from backend.routes.auth import router as auth_router

router = APIRouter()

router.include_router(auth_router)
