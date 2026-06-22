# task_model.py
# Stage11/models/task_model.py
# Pydantic models for task input and response

from pydantic import BaseModel
from typing import Optional

class TaskInput(BaseModel):
    type: str
    payload: Optional[str] = None

class TaskResponse(BaseModel):
    id: str
    type: str
    status: str