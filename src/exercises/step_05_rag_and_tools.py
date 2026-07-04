"""
Step 5 — RAG + Tools
--------------------
Add two forms of external grounding:
  - SerperDevTool: live web search — the researcher can find current information
    the model was never trained on.
  - TextFileKnowledgeSource: a document the crew retrieves from at query time (RAG).

Both address the same root limitation in steps 1–4: answers are bounded by the LLM's
training data. This step makes the crew able to use real, external, current information.

Compare to step 4: is the output more accurate or more current? What's more complex or
fragile now? What would break if the search API went down?

Requires: SERPER_API_KEY and GEMINI_API_KEY in your .env
  (Gemini is used for embeddings — Groq handles chat, these are independent services).

Run:
    uv run python src/exercises/step_05_rag_and_tools.py
"""
import os

from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("MODEL", "groq/llama-3.3-70b-versatile")
os.environ.setdefault("EMBEDDINGS_GOOGLE_GENERATIVE_AI_MODEL_NAME", "gemini-embedding-001")
os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")

from crewai import Agent, Crew, Process, Task  # noqa: E402
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai_tools import SerperDevTool

TOPIC = "Artificial Intelligence in Healthcare"

web_search = SerperDevTool()

researcher = Agent(
    role="Research Analyst",
    goal="Gather comprehensive, current research using web search and provided documents",
    backstory=(
        "Senior analyst expert at combining live search results with document knowledge. "
        "Always checks whether claims from prior knowledge match current web sources, "
        "and notes any discrepancies explicitly."
    ),
    verbose=True,
    tools=[web_search],
)

analyst = Agent(
    role="Strategic Analyst",
    goal="Identify patterns, risks, and actionable implications from research",
    backstory="You transform raw research into strategic insight for decision-makers.",
    verbose=True,
)

research_task = Task(
    description=(
        f"Search the web for current information on: {TOPIC}\n\n"
        f"Also consult the provided knowledge documents for background context. "
        f"Combine and reconcile both sources — note any discrepancies between them."
    ),
    expected_output=(
        "A comprehensive research report combining live web findings and document knowledge, "
        "with any conflicts or gaps between sources noted explicitly"
    ),
    agent=researcher,
)

analysis_task = Task(
    description=(
        f"Using the research on '{TOPIC}', write a strategic analysis. "
        f"Identify: top 3 trends, key risks, biggest opportunities, and 3 specific recommendations."
    ),
    expected_output="Strategic analysis with specific, actionable recommendations",
    agent=analyst,
    context=[research_task],
)

knowledge_sources = [
    TextFileKnowledgeSource(file_paths=["user_preference.txt"]),
    # To add your own document (Step 5 stretch goal):
    # from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
    # PDFKnowledgeSource(file_paths=["your_document.pdf"]),
]

crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential,
    verbose=True,
    knowledge_sources=knowledge_sources,
    embedder={
        "provider": "google-generativeai",
        "config": {
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model_name": "gemini-embedding-001",
        },
    },
)

result = crew.kickoff(inputs={"topic": TOPIC})
print("\n\n=== FINAL ANALYSIS ===\n")
print(result.raw)
