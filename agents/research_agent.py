# research_agent.py
# Stage11/agents/research_agent.py
# Researches the topic and returns raw findings

from agents.base_agent import BaseAgent
from logger import logger


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent")

    async def run(self, task: str) -> str:
        logger.info(f"[ResearchAgent] researching: {task}")
        prompt = f"""You are a research agent. Your job is to gather key facts and information.

Topic: {task}

Provide clear, factual research findings in bullet points. Be concise."""
        return await self.call_ollama(prompt)