"""
Step 4 — Multi-Agent
--------------------
Add a second agent with a different, complementary role. The researcher gathers and
structures raw information; the analyst receives that output and turns it into critical,
decision-ready insight. Sequential pipeline: researcher → analyst.

Compare to step 3: does specialization actually improve the output? Does the analyst push
back on the researcher's findings, or just reformat them? Watch the verbose logs for both
agents' internal reasoning to see where the real difference is.

Run:
    uv run python src/exercises/step_04_multi_agent.py
"""
import os

from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("MODEL", "groq/llama-3.3-70b-versatile")
os.environ.setdefault("EMBEDDINGS_GOOGLE_GENERATIVE_AI_MODEL_NAME", "gemini-embedding-001")
os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")

from crewai import Agent, Crew, Process, Task  # noqa: E402

TOPIC = "Artificial Intelligence in Healthcare"

researcher = Agent(
    role="Research Analyst",
    goal="Gather and organize comprehensive, factual research on a topic",
    backstory=(
        "Senior analyst expert at finding and structuring information from diverse sources. "
        "Focuses on facts, concrete examples, and what's actually happening in the field — "
        "not what people wish were happening."
    ),
    verbose=True,
)

analyst = Agent(
    role="Strategic Analyst",
    goal="Identify patterns, risks, and actionable implications from research",
    backstory=(
        "You transform raw research into strategic insight. You are skeptical, look for what's "
        "missing or overstated, and always ask: what does this mean for decision-makers right now, "
        "not in the abstract? What's the strongest argument against the obvious conclusion?"
    ),
    verbose=True,
)

research_task = Task(
    description=f"Research the following topic comprehensively:\n\nTopic: {TOPIC}",
    expected_output="A thorough research report: facts, concrete examples, current developments",
    agent=researcher,
)

analysis_task = Task(
    description=(
        f"Using the research on '{TOPIC}', write a strategic analysis.\n\n"
        f"Identify: top 3 trends, key risks, biggest opportunities, "
        f"and 3 specific recommendations for decision-makers."
    ),
    expected_output=(
        "A strategic analysis with specific, actionable recommendations — "
        "not generic advice, but conclusions that follow from this particular research"
    ),
    agent=analyst,
    context=[research_task],
)

crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print("\n\n=== FINAL ANALYSIS ===\n")
print(result.raw)
