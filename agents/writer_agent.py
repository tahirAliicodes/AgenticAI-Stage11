# writer_agent.py
# Stage11/agents/writer_agent.py
# Writes the final response based on analysis

from agents.base_agent import BaseAgent
from logger import logger

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__("WriterAgent")

    async def run(self, task: str, analysis: str) -> str:
        logger.info(f"[WriterAgent] writing final response for: {task}")
        prompt = f"""You are a writer agent. Your job is to write a clear, helpful final answer.

Original Question: {task}
Analysis:
{analysis}

Write a clean, concise, helpful response for the user."""
        return await self.call_ollama(prompt)