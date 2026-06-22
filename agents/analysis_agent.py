# analysis_agent.py
# Stage11/agents/analysis_agent.py
# Analyses the research findings and extracts insights

from agents.base_agent import BaseAgent
from logger import logger

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("AnalysisAgent")

    async def run(self, task: str, research: str) -> str:
        logger.info(f"[AnalysisAgent] analysing findings for: {task}")
        prompt = f"""You are an analysis agent. Your job is to analyse research and extract key insights.

Topic: {task}
Research Findings:
{research}

Provide a clear analysis with the most important insights. Be concise."""
        return await self.call_ollama(prompt)