# health.py
# Stage11/routers/health.py
# Health check endpoints for load balancers and monitoring

from fastapi import APIRouter
from task_queue import queue_size
from config import settings

router = APIRouter()

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "app": settings.app_name,
        "env": settings.app_env
    }

@router.get("/ready")
async def ready():
    return {
        "status": "ready",
        "queue_size": queue_size()
    }

@router.get("/live")
async def live():
    return {"status": "alive"}