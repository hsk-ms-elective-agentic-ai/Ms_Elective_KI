# Generative & Agentic AI — Hands-On Exercises

*Companion repository for the exercise sessions of* **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**.

Lecture theory is delivered via slides in class. This repository is the hands-on practice companion: a small, working multi-agent AI system built with [CrewAI](https://crewai.com) that you'll read, run, and extend across the exercise sessions — plus a graded team assignment where you design your own agentic AI architecture for a use case of your choice.

## Communication

**All course communication goes through Discord — [join here](https://discord.gg/c89VTuMRQ).** Questions about setup, exercises, the team assignment, or anything else in this repo: ask there, not via GitHub Issues (Issues on *this* shared course repo are reserved for the team sign-up flow only — your own team's repo is different, see ["Working like an agile team"](team_assignment/en/assignment-overview.md#working-like-an-agile-team-sprints-epics-user-stories--issues) for how you'll use Issues there) or any other channel.

Each team can spin up its **own thread** off the relevant channel for internal team coordination — any member can start one, no special permission needed.

Inquiries via email, WhatsApp, or any other channel will not be answered.

## Goal

The goal of these exercises is to turn the architectural concepts from the lecture — agents, tasks, tools, RAG, multi-agent orchestration, trust, production, security — from slides into things you've actually read, run, and modified in working code. By the end, you'll be able to **design**, and optionally **implement**, your own agentic AI architecture for a real use case, using CrewAI as the concrete framework.

## 1. Prerequisites

### Getting access (students)

This course runs in a GitHub Organization, not on this repo directly. Everything below happens once, before your first exercise:

1. **Get a GitHub account** if you don't already have one — free, just an email signup.
2. **Submit your details**: open a [team sign-up issue](https://github.com/hsk-ms-elective-agentic-ai/Ms_Elective_KI/issues/new?template=team-signup.yml) with your email and your GitHub username. You don't pick your team yourself — your instructor reviews the issue and assigns your team manually (not instant), which triggers a GitHub Action that adds you automatically.
3. **Accept the invite** — check your GitHub notifications/email and accept the team invitation. You have no access until you do this step.
4. Once you're on your team, your instructor gives your team access to **your own copy of this repo** (created from this template, one per team) — that's the repo you'll actually work in for every exercise and the team assignment, not this one.

Everything from section 4 onward in this README applies to **your team's repo**, once you have access to it.

## 2. Team Allocation & Steps

### Team assignment

Teams of **3–5 students** work through a sequence of versions of the same AI system on the same topic — this *is* the exercise series, not a separate thing alongside it: each step below both teaches a concept and produces output you compare directly to the previous step. The primary deliverable is `EVALUATION.md`: a full project report on the agent your team designs and builds, informed by what changed at each step. Start at [team_assignment/en/assignment-overview.md](team_assignment/en/assignment-overview.md) (English / [Deutsch](team_assignment/de/assignment-overview.md)) for the full grading rubric.

### Use cases to pick from

Pick one of the five use cases below. Each is designed so that the steps produce **noticeably different output**: a simple prompt gives a broad starting point, structured prompting adds focus and format, a single agent adds a consistent perspective, web search + RAG grounds the output in current, specific evidence, and a second agent transforms the grounded research into a recommendation. The quality of your evaluation depends on how well your team knows the subject — pick a topic you can actually judge.

---

**1. Competitive Landscape Analysis**

A product manager or founder entering a new market needs to know who the dominant players are, how they differentiate, and where the genuine gaps are — not a Wikipedia summary, but analysis sharp enough to inform a market-entry decision. *Step 03* gives you a list of names with surface-level descriptions. *Steps 04–08* add a SWOT frame, an analyst persona, and investor-friendly language — immediately more structured. *Step 09* gives you a researcher agent whose role keeps it consistently focused on competitive signals rather than generic industry background. *Steps 10–12* close the information gap: web search adds current funding rounds and product launches; a market brief or investor memo as a RAG source ties the analysis to a specific entry thesis rather than the general market. *Step 13* adds a positioning strategist who takes the now-grounded competitive data and converts it into a differentiation recommendation — the two agents together produce something neither produces alone.

- **Topic example:** `"Competitive landscape for [product category] targeting [customer segment] in [region]"`
- **Agents (Step 09, Step 13):** Market Intelligence Researcher → Positioning Strategist
- **Tool (step 10):** `SerperDevTool` — current news, funding announcements, product launches
- **RAG source (step 12):** Market positioning brief or investor memo (PDF)

---

**2. Regulatory Impact Briefing**

A compliance officer or product team needs to understand what a specific regulation — EU AI Act, GDPR, Digital Markets Act — actually requires of their product, and what concrete actions to take before the compliance deadline. *Step 03* produces a generic regulation summary that could have come from a news article. *Steps 04–08* add a compliance-officer persona and an action-checklist output format — the same information becomes immediately actionable. *Step 09* gives you a policy-tracker agent that stays focused on the obligations relevant to a specific company type, not the regulation in general. *Steps 10–12* are where it gets specific: web search surfaces recent enforcement decisions and implementation guidance; the actual regulation text as a RAG source lets agents quote specific articles rather than paraphrase from training data. *Step 13* adds a compliance strategist who converts those now-grounded obligations into a prioritized remediation plan — the tracker surfaces what's required; the strategist says what to do about it and in what order.

- **Topic example:** `"EU AI Act compliance requirements for a B2B SaaS company that uses LLMs in its product"`
- **Agents (Step 09, Step 13):** Policy Tracker → Compliance Strategist
- **Tool (step 10):** `SerperDevTool` — enforcement decisions, recent regulatory guidance
- **RAG source (step 12):** The regulation text (PDF — available from EUR-Lex)

---

**3. Talent and Skills Gap Analysis**

An HR director or team lead at a tech company needs to know which AI/ML skills are genuinely in demand right now, how the current team stacks up, and whether to hire, retrain, or partner. *Step 03* produces a generic "top skills in AI" list — exactly what any search engine returns. *Steps 04–08* add an HR-manager persona and a skills-gap-table format, making the output directly usable in a team meeting. *Step 09* gives you a labor-market researcher agent focused on demand signals from real job postings rather than general trends. *Steps 10–12* make it current: web search pulls live job postings and salary benchmarks; a team skills inventory or competency framework as a RAG source makes the gap analysis specific to the actual team rather than a hypothetical one. *Step 13* adds a workforce strategist who takes the now-grounded research and proposes a concrete hiring or upskilling plan — researcher provides the market picture; strategist provides the response.

- **Topic example:** `"In-demand AI engineering and MLOps skills for product teams at European fintechs (2025)"`
- **Agents (Step 09, Step 13):** Labor Market Researcher → Workforce Strategist
- **Tool (step 10):** `SerperDevTool` — job boards, hiring trends, salary benchmarks
- **RAG source (step 12):** Team skills inventory or competency framework (text file)

---

**4. Startup Due-Diligence Memo**

An angel investor or early-stage VC evaluating a pre-seed startup needs a structured view of the market opportunity, competitive threats, team credibility, and key risks — produced quickly from public information. *Step 03* gives you a generic "how to evaluate a startup" framework, not an evaluation of any specific startup. *Steps 04–08* add a VC analyst persona and a standard memo structure (market / competition / team / risks / verdict) — suddenly it reads like an actual first draft. *Step 09* gives you a diligence researcher who stays focused on gathering factual signals for a specific startup type rather than explaining due diligence in general. *Steps 10–12* make it grounded: web search surfaces recent press, competitor funding, and market context; the startup's pitch deck as a RAG source lets the analysis engage directly with what the founders claim rather than what the model assumes. *Step 13* adds an investment analyst who takes the now-grounded research and writes the memo with an explicit recommendation — the researcher gathers evidence; the analyst makes the call.

- **Topic example:** `"Due diligence on an early-stage startup building AI-powered legal document review for SMEs"`
- **Agents (Step 09, Step 13):** Diligence Researcher → Investment Analyst
- **Tool (step 10):** `SerperDevTool` — recent news, competitor signals, market sizing
- **RAG source (step 12):** Startup pitch deck or product one-pager (PDF)

---

**5. ESG and Sustainability Risk Briefing**

A fund manager, analyst, or corporate strategy team needs to assess the environmental, social, and governance risks of a company or sector — for investment screening, stakeholder reporting, or strategic planning. *Step 03* produces a surface-level summary of ESG topics that applies to almost any company — not useful for any specific one. *Steps 04–08* add an ESG analyst persona and a risk-rating output format, making the output look and read like a proper briefing section. *Step 09* gives you an ESG researcher agent focused on material risks for a specific sector, not ESG in general. *Steps 10–12* are where generic output becomes specific: web search surfaces recent controversies, regulatory fines, and third-party ESG ratings; the company's own sustainability report as a RAG source lets the agents compare what the company claims against what is publicly documented. *Step 13* adds a risk strategist who converts the now-grounded research into a risk rating with concrete mitigation recommendations — the researcher surfaces the exposure; the strategist says what to do about it.

- **Topic example:** `"ESG risk profile for fast-fashion retailers: labor practices, Tier-2 supply chain, and end-of-life circularity"`
- **Agents (Step 09, Step 13):** ESG Researcher → Risk & Strategy Analyst
- **Tool (step 10):** `SerperDevTool` — controversies, regulatory actions, ESG ratings
- **RAG source (step 12):** Company sustainability report (PDF)

---

Start at [Step 03 — Zero-Shot Prompting](exercises/en/step_03_zero_shot_prompting.ipynb) once you have the repo running — or [Step 00](exercises/en/step_00_setup_and_python_basics.ipynb) first if Git, `uv`, Jupyter, or Python itself are new to you.

## 3. Exercises & Tools

### Intro to CrewAI

[CrewAI](https://docs.crewai.com) is a Python framework for orchestrating multiple LLM-powered agents that collaborate on a shared set of tasks, instead of one model trying to do everything in a single call. Four abstractions do all the work:

- **Agent** — a `role`, `goal`, `backstory`, an LLM, and optionally `tools`
- **Task** — a `description`, an `expected_output`, and which agent is assigned to it
- **Crew** — the collection of agents + tasks + a `process` for running them
- **Process** — the orchestration strategy: `sequential` (fixed pipeline) or `hierarchical` (a manager agent delegates dynamically)

CrewAI's signature choice — demonstrated across the exercise steps — is that `role`/`goal`/`backstory`/task definitions live in **YAML config**, not Python, so you can usually change *what* a crew does without touching the orchestration code at all.

### The template code

The exercise notebooks (Steps 09–13) are standalone — each defines its own `Agent`(s) inline, with no dependency on a separate crew project. This repo also ships a full working crew (`researcher` → `analyst`, sequential) as a reference for the fuller CrewAI project layout (YAML-configured agents/tasks, a `Crew`, an entry point) once you're ready to go beyond the notebooks:

| File | What it is |
| --- | --- |
| [src/research_crew/crew.py](src/research_crew/crew.py) | Defines the agents, tasks, and the `Crew` itself — short on purpose |
| [src/research_crew/config/agents.yaml](src/research_crew/config/agents.yaml) | Each agent's `role`/`goal`/`backstory` |
| [src/research_crew/config/tasks.yaml](src/research_crew/config/tasks.yaml) | Each task's `description`/`expected_output`/agent assignment |
| [src/research_crew/main.py](src/research_crew/main.py) | Entry point — sets the `topic` input and kicks off the crew |
| [src/research_crew/tools/custom_tool.py](src/research_crew/tools/custom_tool.py) | An unwired template for writing your own tool |
| [src/research_crew/knowledge_source_example.py](src/research_crew/knowledge_source_example.py) | A working, unwired `build_knowledge_sources()` helper for RAG |
| [exercises/en/](exercises/en/) | Jupyter notebooks for Steps 00–13 |

### Exercise steps

These steps ([English](exercises/README.md) / [Deutsch](exercises/de/README.md)) walk through simple prompting → prompt template → single agent → multi-agent → tools/MCP/RAG, all on the same topic. Each step adds one layer and asks you to compare the output to the previous step — the progression is the exercise, and the comparison is the deliverable. Each step includes just enough background from the relevant research paper to place the concept, then goes straight into running and observing.

### Adding more tools or RAG (for students)

`crewai_tools` ships ~90 built-in tools beyond `SerperDevTool`. The setup that matters most is whether a tool calls an external API directly (just needs a key) or does **local embedding-based search** (needs an embedder pointed at Gemini, same as below) — that split is called out per category.

| Category | Needs embedder config? | Tools |
| --- | --- | --- |
| Web search | No — just an API key | `SerperDevTool`, `TavilySearchTool`, `BraveSearchTool`, `EXASearchTool`, `SerpApiGoogleSearchTool`, `SerpApiGoogleShoppingTool`, `SerplyWebSearchTool`, `SerplyNewsSearchTool`, `SerplyJobSearchTool`, `SerplyScholarSearchTool`, `LinkupSearchTool`, `ParallelSearchTool`, `ArxivPaperTool`, `FirecrawlSearchTool` |
| Web scraping & browser automation | No — just an API key | `ScrapeWebsiteTool`, `ScrapeElementFromWebsiteTool`, `SerperScrapeWebsiteTool`, `SerplyWebpageToMarkdownTool`, `FirecrawlScrapeWebsiteTool`, `FirecrawlCrawlWebsiteTool`, `JinaScrapeWebsiteTool`, `ScrapflyScrapeWebsiteTool`, `ScrapegraphScrapeTool`, `SeleniumScrapingTool`, `SpiderTool`, `BrowserbaseLoadTool`, `HyperbrowserLoadTool`, `StagehandTool`, `MultiOnTool`, `TavilyExtractorTool`, `BrightDataSearchTool`, `BrightDataWebUnlockerTool`, `BrightDataDatasetTool`, `OxylabsAmazonProductScraperTool`, `OxylabsAmazonSearchScraperTool`, `OxylabsGoogleSearchScraperTool`, `OxylabsUniversalScraperTool` |
| Local RAG / semantic content search | **Yes** — defaults to OpenAI embeddings | `RagTool` (base class), `WebsiteSearchTool`, `PDFSearchTool`, `CSVSearchTool`, `DOCXSearchTool`, `JSONSearchTool`, `MDXSearchTool`, `TXTSearchTool`, `XMLSearchTool`, `CodeDocsSearchTool`, `GithubSearchTool`, `YoutubeVideoSearchTool`, `YoutubeChannelSearchTool`, `DirectorySearchTool` |
| Vector database connectors | Bring your own embeddings/index | `QdrantVectorSearchTool`, `WeaviateVectorSearchTool`, `MongoDBVectorSearchTool`, `CouchbaseFTSVectorSearchTool` |
| Databases & structured data | No | `MySQLSearchTool`, `SnowflakeSearchTool`, `SingleStoreSearchTool`, `DatabricksQueryTool`, `NL2SQLTool` |
| File & storage I/O | No | `FileReadTool`, `FileWriterTool`, `FileCompressorTool`, `DirectoryReadTool`, `S3ReaderTool`, `S3WriterTool` |
| Code execution | No | `CodeInterpreterTool` |
| Vision, image & OCR | No | `DallETool`, `VisionTool`, `OCRTool` |
| Evaluation & quality | No | `PatronusEvalTool`, `PatronusLocalEvaluatorTool`, `PatronusPredefinedCriteriaEvalTool` |
| Platform & automation integrations | Varies by platform | `ZapierActionTool`, `ComposioTool`, `ApifyActorsTool`, `EnterpriseActionTool`, `MergeAgentHandlerTool`, `GenerateCrewaiAutomationTool`, `InvokeCrewAIAutomationTool`, `BedrockInvokeAgentTool`, `BedrockKBRetrieverTool`, `AIMindTool`, `LlamaIndexTool`, `ContextualAICreateAgentTool`, `ContextualAIParseTool`, `ContextualAIQueryTool`, `ContextualAIRerankTool` |

For any tool marked "Needs embedder config", point it at Gemini the same way (otherwise it fails with a missing `OPENAI_API_KEY` error):

```python
WebsiteSearchTool(config={
    "embedding_model": {
        "provider": "google-generativeai",
        "config": {"api_key": os.getenv("GEMINI_API_KEY"), "model_name": "gemini-embedding-001"},
    },
})
```

This crew's `embedder` (see `crew.py`) is already configured the same way at the `Crew` level, so adding a `knowledge_sources=[...]` list there (e.g. a `TextFileKnowledgeSource` pointing at `knowledge/user_preference.txt` — see `knowledge_source_example.py` for an unwired template) will embed via Gemini automatically.

[Step 12](exercises/en/step_12_rag.ipynb) demonstrates the same `knowledge_sources`/`embedder` pattern standalone, with its own separate `exercises/en/knowledge/` folder. The two `knowledge/` directories are intentionally distinct, not a duplicate: this repo-root one belongs to the full demo project above; the one under `exercises/en/` belongs to that notebook, since `TextFileKnowledgeSource` resolves paths relative to wherever the code is actually running — the repo root for `crew.py`, but the notebook's own folder for a notebook (see Step 12 for details).

## 4. Technical Setup

### IDE

Use [VS Code](https://code.visualstudio.com/) or [Cursor](https://cursor.com/) (Cursor is based on VS Code). Install two extensions:

- **Python** (`ms-python.python`)
- **Jupyter** (`ms-toolsai.jupyter`) — needed to open and run the `.ipynb` notebooks used throughout the exercises

### Getting started

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Clone your team's repo, then from its root install the dependencies:

```bash
uv sync
```

Copy `.env.example` to `.env` and fill in your API keys (`OPENAI_API_KEY` or `GEMINI_API_KEY`, plus `SERPER_API_KEY` and `GEMINI_API_KEY`) — ask your team if someone already has keys to share rather than signing up again, unless you specifically want your own.

#### Register the Jupyter kernel

All steps are Jupyter notebooks. To make this project's virtual environment (and its dependencies) available inside them, register it as a kernel once:

```bash
uv run python -m ipykernel install --user --name research_crew --display-name "research_crew"
```

Now, when you open a notebook in VS Code/Cursor, pick **"research_crew"** from the kernel picker in the top-right corner (or **Kernel → Change kernel**).

Once that's done, continue with [Run the crew](#run-the-crew) below.

#### Customizing

**Make sure your `.env` has the right API keys for whichever LLM/tools you use**

- Modify `src/research_crew/config/agents.yaml` to define your agents
- Modify `src/research_crew/config/tasks.yaml` to define your tasks
- Modify `src/research_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/research_crew/main.py` to add custom inputs for your agents and tasks

**Using Gemini free tier instead of OpenAI (optional)**: switch to Google's free-tier model by setting `MODEL=gemini/gemini-3.1-flash-lite` in your `.env`. You only need one key (`GEMINI_API_KEY`) because the same key covers both the chat model and embeddings — no credit card required. Get a key at [ai.google.dev](https://ai.google.dev). The `MODEL` env var works with any provider `litellm` supports, so you can also swap in other models (e.g. `deepseek/deepseek-chat` with `DEEPSEEK_API_KEY`, or `cohere/command-r-plus` with `COHERE_API_KEY` — Cohere's free trial key is capped at 1,000 calls/month and chat only, embeddings still need `GEMINI_API_KEY`) without touching the code.

**Hit a Gemini "RESOURCE_EXHAUSTED" / quota error?** The free tier's daily request quota is tracked **per model**, not per key — switching `MODEL` to a different free Gemini model (e.g. `gemini/gemini-2.5-flash`, `gemini/gemini-3.5-flash`, `gemini/gemini-3-flash-preview`) gets you a fresh quota immediately, no new key needed. Avoid these — confirmed broken or unavailable as of 2026-07: `gemini-2.0-flash`/`gemini-2.0-flash-lite` (deprecated, no longer free), `gemini-2.5-flash-lite` (returns a 404, "no longer available to new users"), and `gemini-2.5-pro` (no free tier at all, paid only).

### Run the crew

From the project root:

```bash
uv run research_crew
```

This initializes the research_crew Crew, assembling the agents and assigning them tasks as defined in your configuration, and saves the report to `output/report.md`.

## Support

For support, questions, or feedback regarding CrewAI itself (not the exercises):
- Visit the [CrewAI documentation](https://docs.crewai.com)
- Reach out via the [CrewAI GitHub repository](https://github.com/crewAIInc/crewAI)

To learn CrewAI beyond what these steps cover, on your own time:
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) (DeepLearning.AI) — a short video course taught by CrewAI's founder; free during DeepLearning.AI's platform beta, may not stay free indefinitely
- [Join the CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)
