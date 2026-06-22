# main.py
# Stage11/main.py
# FastAPI entry point — starts worker, registers routers, manages lifecycle

import asyncio
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from logger import logger
from worker import run_worker
from routers.health import router as health_router
from routers.tasks import router as tasks_router
from routers.canary import router as canary_router

worker_task = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global worker_task
    logger.info(f"Starting {settings.app_name} in {settings.app_env} mode")
    worker_task = asyncio.create_task(run_worker())

    yield

    logger.info("Shutting down...")
    worker_task.cancel()
    try:
        await worker_task
    except asyncio.CancelledError:
        pass
    logger.info("Shutdown complete")


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
    redoc_url=None,
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(tasks_router)
app.include_router(canary_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)
