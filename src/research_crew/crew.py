# src/research_crew/crew.py
import os

from dotenv import load_dotenv

# Load .env before the setdefault calls below — otherwise MODEL's fallback would
# already be set by the time crewai's own internal load_dotenv() (override=False)
# runs on import, and .env's MODEL would silently never take effect.
load_dotenv()

# CrewAI's telemetry tries to register OS signal handlers, which only works in the
# main thread — fails (harmlessly) when run from Streamlit's worker thread otherwise.
os.environ.setdefault('CREWAI_DISABLE_TELEMETRY', 'true')

# Codespaces secrets bypass .env entirely, so .env.example's defaults never apply there —
# set them here instead. Also: the Gemini embedder's model_name field shares a "model"
# validation alias with the MODEL var above, so it silently inherits MODEL's value unless
# pinned via this more specific env var — set both defensively, before crewai is imported.
os.environ.setdefault('MODEL', 'gpt-4o-mini')
os.environ.setdefault('EMBEDDINGS_GOOGLE_GENERATIVE_AI_MODEL_NAME', 'gemini-embedding-001')

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class ResearchCrew():
    """Research crew for comprehensive topic analysis and reporting"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'] # type: ignore[index]
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], # type: ignore[index]
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            embedder={
                "provider": "google-generativeai",
                "config": {
                    "api_key": os.getenv("GEMINI_API_KEY"),
                    "model_name": "gemini-embedding-001",
                },
            },
        )