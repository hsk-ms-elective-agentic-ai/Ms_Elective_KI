"""
Step 3 — Single Agent
---------------------
Wrap the prompt in a CrewAI Agent and Task. Under the hood, role/goal/backstory are still
assembled into a system prompt — CrewAI just does that for you and adds a think→act→observe
loop around the LLM call. One agent, one task, one crew.

Compare to step 2: what does the framework add beyond what two hand-written messages gave you?
Watch the verbose logs to see the internal reasoning.

Run:
    uv run python src/exercises/step_03_single_agent.py
"""
import os

from dotenv import load_dotenv

load_dotenv()
# These must be set before importing crewai (crew_base.py calls load_dotenv at import time).
os.environ.setdefault("MODEL", "groq/llama-3.3-70b-versatile")
os.environ.setdefault("EMBEDDINGS_GOOGLE_GENERATIVE_AI_MODEL_NAME", "gemini-embedding-001")
os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")

from crewai import Agent, Crew, Process, Task  # noqa: E402

TOPIC = "Artificial Intelligence in Healthcare"

researcher = Agent(
    role="Research Analyst",
    goal="Produce structured, evidence-based research summaries",
    backstory=(
        "You are a senior analyst with expertise in synthesizing complex information "
        "across technology and business domains. Known for clear structure, concrete "
        "examples, and surfacing non-obvious implications."
    ),
    verbose=True,
)

research_task = Task(
    description=(
        f"Research the following topic and write a comprehensive summary for a "
        f"professional audience.\n\nTopic: {TOPIC}\n\n"
        f"Include: overview, key developments, practical implications, open questions."
    ),
    expected_output="A structured research summary with clear sections and concrete examples",
    agent=researcher,
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print("\n\n=== RESULT ===\n")
print(result.raw)
