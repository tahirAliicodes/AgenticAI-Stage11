# task_queue.py
# Stage11/task_queue.py
# Async queue for passing tasks from API to worker

import asyncio
from logger import logger

task_queue: asyncio.Queue = asyncio.Queue()

async def enqueue_task(task: dict):
    await task_queue.put(task)
    logger.info(f"Task enqueued: {task['id']}")

async def get_next_task() -> dict:
    return await task_queue.get()

def task_done():
    task_queue.task_done()

def queue_size() -> int:
    return task_queue.qsize()