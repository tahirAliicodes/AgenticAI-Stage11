# messages.py
# Stage11/models/messages.py
# Message format passed between worker and agents

from pydantic import BaseModel
from typing import Any, Dict, Optional

class AgentMessage(BaseModel):
    from_agent: str
    to_agent: str
    task: str
    payload: Dict[str, Any] = {}

class AgentResult(BaseModel):
    success: bool
    result: Optional[str] = None
    error: Optional[str] = None