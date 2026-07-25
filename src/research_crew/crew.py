# src/research_crew/crew.py
import os

from dotenv import load_dotenv

# Load .env before the setdefault calls below — otherwise MODEL's fallback would
# already be set by the time crewai's own internal load_dotenv() (override=False)
# runs on import, and .env's MODEL would silently never take effect.
load_dotenv()

# The Gemini embedder's model_name field shares a "model" validation alias with the
# MODEL var above, so it silently inherits MODEL's value unless pinned via this more
# specific env var — set both defensively, before crewai is imported.
os.environ.setdefault('MODEL', 'gpt-4o-mini')
os.environ.setdefault('EMBEDDINGS_GOOGLE_GENERATIVE_AI_MODEL_NAME', 'gemini-embedding-001')

# CrewAI's telemetry tries to reach its backend over the network on import; on a
# restricted/firewalled connection this can hang for a long time with no error.
# Disable it before crewai is imported.
os.environ.setdefault('CREWAI_DISABLE_TELEMETRY', 'true')

from crewai import Agent, Crew, Process, Task
from crewai.mcp import MCPServerStdio
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from research_crew.knowledge_source_example import build_knowledge_sources

# embedder dict shape used throughout this repo (e.g. Step 12's RAG
# notebook), just centralized here since crew.py only needs it once.
GEMINI_EMBEDDER = {
    "provider": "google-generativeai",
    "config": {
        "api_key": os.getenv("GEMINI_API_KEY"),
        "model_name": "gemini-embedding-001",
    },
}


# @CrewBase turns this plain class into a "project": on init, it reads
# config/agents.yaml and config/tasks.yaml and exposes them as
# self.agents_config / self.tasks_config (dicts keyed by the YAML's top-level
# names, e.g. agents_config['researcher'] below is that whole "researcher:"
# block). This is the notebooks-vs-project split from the README's "The
# template code" section: Steps 09-13 build an Agent/Task inline in Python;
# this class instead pulls role/goal/backstory and description/expected_output
# from YAML, so changing what the crew does rarely means touching this file.
@CrewBase
class ResearchCrew():
    """Research crew for comprehensive topic analysis and reporting

    See agents.yaml/tasks.yaml for how each field maps back to the prompting
    building blocks from step 2 (system/user roles, chain prompting via `context:`).
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    # @agent registers this method's return value into self.agents below —
    # you never append to that list by hand, decorating the method does it.
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()],
            # mcp-server-fetch: the official reference MCP server (fetches
            # and reads web pages), run as a local subprocess via `uvx` — an
            # existing server, nothing custom-built. Lets the researcher pull
            # and quote a specific page directly, complementing SerperDevTool's
            # broad search-and-summarize. See Step 11 for the concept.
            mcps=[MCPServerStdio(command="uvx", args=["mcp-server-fetch"])],
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )

    # @task does the same for self.tasks — one decorated method per Task,
    # in the order you want them to run under Process.sequential below.
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

    # @crew marks the method CrewAI actually calls (via ResearchCrew().crew()
    # in main.py) to assemble everything above into one runnable Crew.
    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # Prints a free, no-signup shareable trace URL (agent reasoning, task
            # timing, tool calls) to app.crewai.com after each run.
            tracing=True,
            embedder=GEMINI_EMBEDDER,
            # RAG (see knowledge_source_example.py / Step 12) grounds the crew
            # in knowledge/user_preference.txt and knowledge/rag-data.pdf.
            knowledge_sources=build_knowledge_sources(),
        )