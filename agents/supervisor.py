# supervisor_agent.py
# Stage11/agents/supervisor_agent.py
# Supervises the full pipeline: research → analysis → writer

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.writer_agent import WriterAgent
from models.messages import AgentMessage, AgentResult
from logger import logger

class Supervisor:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.writer_agent = WriterAgent()

    async def run(self, message: AgentMessage) -> AgentResult:
        task = message.task
        logger.info(f"[Supervisor] starting pipeline for: {task}")

        try:
            research = await self.research_agent.run(task)
            analysis = await self.analysis_agent.run(task, research)
            final = await self.writer_agent.run(task, analysis)

            logger.info(f"[Supervisor] pipeline complete for: {task}")
            return AgentResult(success=True, result=final)

        except Exception as e:
            logger.error(f"[Supervisor] pipeline failed: {e}")
            return AgentResult(success=False, error=str(e))