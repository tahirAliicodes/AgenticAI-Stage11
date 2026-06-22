# tasks.py
# Stage11/routers/tasks.py
# Task submission and result retrieval endpoints

from fastapi import APIRouter
from models.task_model import TaskInput, TaskResponse
from task_queue import enqueue_task, queue_size
from logger import logger
import uuid

router = APIRouter()

task_results = {}

@router.get("/tasks/queue")
async def queue_status():
    return {"queue_size": queue_size()}

@router.post("/tasks", response_model=TaskResponse)
async def submit_task(task_input: TaskInput):
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "type": task_input.type,
        "payload": task_input.payload
    }
    await enqueue_task(task)
    logger.info(f"Task submitted: {task_id}")
    task_results[task_id] = {"status": "queued", "result": None}
    return TaskResponse(id=task_id, type=task_input.type, status="queued")

@router.get("/tasks/{task_id}")
async def get_task_result(task_id: str):
    if task_id not in task_results:
        return {"status": "not_found", "result": None}
    return task_results[task_id]