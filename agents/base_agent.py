# base_agent.py
# Stage11/agents/base_agent.py
# Base class all agents inherit from

import httpx
from config import settings
from logger import logger

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.ollama_url = settings.ollama_url
        self.model = settings.ollama_model

    async def call_ollama(self, prompt: str) -> str:
        logger.info(f"[{self.name}] calling Ollama...")
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]