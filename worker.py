# worker.py
# Stage11/worker.py
# Pulls tasks from queue and runs them through the supervisor pipeline

import asyncio
from logger import logger
from task_queue import get_next_task, task_done
from agents.supervisor import Supervisor
from models.messages import AgentMessage
from routers.tasks import task_results

supervisor = Supervisor()

BLOCKED_WORDS = {"fuck", "shit", "bitch", "asshole", "fucker", "motherfucker", "bastard"}

async def process_task(task: dict):
    task_id = task["id"]
    logger.info(f"Processing task: {task_id} | type: {task['type']}")

    query = task.get("payload") or task.get("type")

    # Strip spaces before checking so "mother fucker" is caught too
    query_lower = query.lower().replace(" ", "")
    if any(word in query_lower for word in BLOCKED_WORDS):
        logger.warning(f"Task rejected (bad words): {task_id}")
        task_results[task_id] = {"status": "rejected", "result": "Task rejected: inappropriate language."}
        return

    message = AgentMessage(
        from_agent="worker",
        to_agent="supervisor",
        task=query,
        payload={}
    )

    result = await supervisor.run(message)

    if result.success:
        logger.info(f"Task complete: {task_id} | result: {result.result[:200]}")
        task_results[task_id] = {"status": "completed", "result": result.result}
    else:
        logger.error(f"Task failed: {task_id} | error: {result.error}")
        task_results[task_id] = {"status": "failed", "result": result.error}


async def run_worker():
    logger.info("Worker started — waiting for tasks...")
    while True:
        try:
            task = await get_next_task()
            await process_task(task)
            task_done()
        except asyncio.CancelledError:
            logger.info("Worker shutting down cleanly")
            break
        except Exception as e:
            logger.error(f"Worker error: {e}")
            task_done()