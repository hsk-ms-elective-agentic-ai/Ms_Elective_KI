# Generative & Agentic AI — Hands-On Exercises

*Companion repository for the exercise sessions of* **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**.

Lecture theory is delivered via slides in class. This repository is the hands-on practice companion: a small, working multi-agent AI system built with [CrewAI](https://crewai.com) that you'll read, run, and extend across the exercise sessions — plus a graded team assignment where you design your own agentic AI architecture for a use case of your choice.

## Communication

**All course communication goes through Discord — [join here](https://discord.gg/c89VTuMRQ).** Questions about setup, exercises, the team assignment, or anything else in this repo: ask there, not via GitHub Issues (Issues on *this* shared course repo are reserved for the team sign-up flow only — your own team's repo is different, see ["Working like an agile team"](team_assignment/en/assignment-overview.md#working-like-an-agile-team-sprints-user-stories--issues) for how you'll use Issues there) or any other channel.

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

Teams of **3–5 students** work through a sequence of versions of the same AI system on the same topic — this *is* the exercise series, not a separate thing alongside it: each step below both teaches a concept and produces output you compare directly to the previous step, done individually. As a team, you then design and build your own agent, sprint by sprint, culminating in an Interim and a Final Presentation; each student separately writes and submits their own Ethics Report. Start at [team_assignment/en/assignment-overview.md](team_assignment/en/assignment-overview.md) (English / [Deutsch](team_assignment/de/assignment-overview.md)) for the full grading rubric.

### Use cases to pick from

**1. Job Application Tailoring Assistant**

A student applying to internships or working-student roles needs each application tailored to the specific posting — recruiters and applicant-tracking systems filter out generic, copy-pasted applications fast. Writing one tailored application already takes real effort; writing a dozen, each genuinely specific to a different posting, company, and role, is what actually burns people out and pushes them back toward copy-paste. The hard part isn't writing well in general — it's reconciling two things that don't automatically line up: what a specific posting is actually asking for (often buried in vague corporate language, or split between the job ad and the company's own site), and what the applicant can honestly offer, using real experience rather than invented or exaggerated achievements. A good solution has to bridge that gap fresh for each posting, without the applicant manually rewriting their story from scratch every time.

- **Topic example:** `"Tailor an application for a [Working Student — Data Analytics] role at [Company] in [City]"`
- **Context you have available:** the job posting itself; the applicant's own CV/resume; public information about the company (news, culture, interview-process reports) reachable via web search.

---

**2. Exam Prep Coach**

A student preparing for an exam needs active recall practice — testing what they actually remember — not another pass of re-reading slides, which feels productive but barely improves retention. The problem has two parts that are easy to conflate: figuring out what's actually likely to matter for this exam (which takes judgment about relative importance, not just a list of topics), and then being genuinely tested on it — asked a question, forced to answer without peeking, and told honestly whether the answer was right or just close. Most students skip straight to re-reading because building good test questions from your own material is itself work — a lecture slide doesn't come with a quiz attached, and a generic online quiz for "the course" doesn't exist. A good solution needs to work from what was actually taught, not a generic textbook version of the subject, and needs to be honest when an answer is wrong rather than just moving on.

- **Topic example:** `"Prepare me for the [Course Name] midterm, covering [Topic A, B, C]"`
- **Context you have available:** the student's own lecture notes or slides; supplementary explanations and worked examples for tricky concepts, reachable via web search.

---

**3. Personalized Study & Semester Planner**

A student staring at a syllabus and an exam date needs a realistic day-by-day plan — not vague "study a bit every day" advice, but a schedule that actually accounts for how much time is left and how much material there is. This is a genuine scheduling and prioritization problem, not just a motivational one: a syllabus lists topics, not effort — some are a one-lecture aside, others are the backbone of half the exam, and a plan that treats them equally wastes the time it's supposed to be protecting. Building a good plan means correctly weighing what deserves more or less time, sequencing it sensibly (foundational topics before the ones that build on them), and fitting all of that into the hours a student actually has available around their other commitments — not an idealized full-time student's schedule.

- **Topic example:** `"4-week study plan for the [Course Name] final exam on [date], ~1.5h on weekdays"`
- **Context you have available:** the course syllabus or module handbook; effective study techniques for the specific subject, reachable via web search.

---

**4. Inbox Triage & Draft-Reply Assistant**

Anyone running a shared inbox — a student club, a TA mailbox, a part-time job — needs incoming emails read, understood, and answered consistently, without every reply being reinvented from scratch. Volume alone is rarely the hard part; the hard part is that "incoming email" isn't one task but several different ones wearing the same envelope — a meeting request, a complaint, a routine question with a known answer, something that genuinely needs a human's judgment call — and treating them all the same way either wastes effort on the simple ones or mishandles the ones that actually need care. A good solution has to tell these apart reliably, answer consistently with whatever the actual policy or past practice is instead of inventing a plausible-sounding but wrong answer, and know when to stop and hand something to a human rather than guess.

- **Topic example:** `"Triage and draft replies for incoming emails to [a student club / TA inbox]"`
- **Context you have available:** the incoming emails themselves, varying in intent and urgency; a personal FAQ, policy doc, or past reply examples; background an email might reference, reachable via web search.

---

**5. Student Budget & Savings Planner**

A student managing rent, part-time income, and irregular expenses needs an actual plan — not "spend less," but a concrete monthly budget that accounts for what's coming in and going out. Generic budgeting advice is nearly useless here, because the right answer depends entirely on someone's actual numbers, and those numbers are messy: income that varies month to month, expenses that aren't all monthly (a one-off semester fee, an irregular course cost), and goals that trade off against each other (save for X vs. afford Y this month). A good solution needs to work from someone's real income and spending rather than a hypothetical, and produce a plan that makes the actual trade-offs explicit, rather than hiding behind advice like "cut back on eating out."

- **Topic example:** `"Monthly budget for a student earning [income], saving for [goal]"`
- **Context you have available:** a budget spreadsheet or bank statement, exported as text (a synthetic one works fine — no need to use real financial data); current student discounts, grants, or cost-of-living figures, reachable via web search.

---

Start at [Step 02 — Zero-Shot Prompting](exercises/step_02_zero_shot_prompting.ipynb) once you have the repo running — or [Step 00](exercises/step_00_setup_and_python_basics.ipynb) first if Git, `uv`, or Jupyter are new to you.

## 3. Exercises & Tools

### Intro to CrewAI

[CrewAI](https://docs.crewai.com) is a Python framework for orchestrating multiple LLM-powered agents that collaborate on a shared set of tasks, instead of one model trying to do everything in a single call. Four abstractions do all the work:

- **Agent** — a `role`, `goal`, `backstory`, an LLM, and optionally `tools`
- **Task** — a `description`, an `expected_output`, and which agent is assigned to it
- **Crew** — the collection of agents + tasks + a `process` for running them
- **Process** — the orchestration strategy: `sequential` (fixed pipeline) or `hierarchical` (a manager agent delegates dynamically)

CrewAI's signature choice — demonstrated across the exercise steps — is that `role`/`goal`/`backstory`/task definitions live in **YAML config**, not Python, so you can usually change *what* a crew does without touching the orchestration code at all.

### The template code

The exercise notebooks (Steps 08–14) are standalone — each defines its own `Agent`(s) inline, with no dependency on a separate crew project. This repo also ships a full working crew (`researcher` → `analyst`, sequential) as a reference for the fuller CrewAI project layout (YAML-configured agents/tasks, a `Crew`, an entry point) once you're ready to go beyond the notebooks. It's wired up with tools, RAG, and MCP all at once, so it doubles as a worked example of combining all three:

| File | What it is |
| --- | --- |
| [src/research_crew/crew.py](src/research_crew/crew.py) | Defines the agents, tasks, and the `Crew` itself — short on purpose |
| [src/research_crew/config/agents.yaml](src/research_crew/config/agents.yaml) | Each agent's `role`/`goal`/`backstory` |
| [src/research_crew/config/tasks.yaml](src/research_crew/config/tasks.yaml) | Each task's `description`/`expected_output`/agent assignment |
| [src/research_crew/main.py](src/research_crew/main.py) | Entry point — sets the `topic` input and kicks off the crew |
| [src/research_crew/tools/custom_tool.py](src/research_crew/tools/custom_tool.py) | An unwired template for writing your own tool |
| [src/research_crew/knowledge_source_example.py](src/research_crew/knowledge_source_example.py) | `build_knowledge_sources()`, wired into `crew.py`'s `Crew(knowledge_sources=...)` — embeds `knowledge/user_preference.txt` and `knowledge/rag-data.pdf` |
| [exercises/](exercises/) | Jupyter notebooks for Steps 00–14 |

MCP needs no template file of its own: `crew.py`'s `researcher` agent connects directly to `mcp-server-fetch` (the official reference MCP server — an existing server, not one built for this repo) via `mcps=[MCPServerStdio(command="uvx", args=["mcp-server-fetch"])]`.

> **Note:** `knowledge/rag-data.pdf` is a local-only sample document (listed in `.git/info/exclude`, not tracked by git) — a real German-language T-Systems whitepaper on AI in healthcare, chosen to match the crew's default `topic`. If you clone this repo fresh, that file won't exist and the crew will fail with a missing-file error until you either add your own `knowledge/rag-data.pdf` or remove that entry from `build_knowledge_sources()`.

### Exercise steps

These steps (see [exercises/README.md](exercises/README.md)) walk through simple prompting → prompt template → single agent → multi-agent → tools/MCP/RAG, all on the same topic. Each step adds one layer and asks you to compare the output to the previous step — the progression is the exercise, and the comparison is the deliverable. Each step includes just enough background from the relevant research paper to place the concept, then goes straight into running and observing.

### Adding more tools, MCP servers, or RAG (for students)

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

This crew's `embedder` (see `crew.py`) is already configured the same way at the `Crew` level, so `build_knowledge_sources()` in `knowledge_source_example.py` (wired into `Crew(knowledge_sources=...)`) embeds a `TextFileKnowledgeSource` pointing at `knowledge/user_preference.txt` and a `PDFKnowledgeSource` pointing at `knowledge/rag-data.pdf` via Gemini automatically. Add or swap entries in that list for your own team's documents.

[Step 13](exercises/step_13_rag.ipynb) demonstrates the same `knowledge_sources`/`embedder` pattern standalone, with its own separate `exercises/knowledge/` folder. The two `knowledge/` directories are intentionally distinct, not a duplicate: this repo-root one belongs to the full demo project above; the one under `exercises/` belongs to that notebook, since `TextFileKnowledgeSource` resolves paths relative to wherever the code is actually running — the repo root for `crew.py`, but the notebook's own folder for a notebook (see Step 13 for details).

Connecting an agent to an MCP server works the same way, just with `Agent(mcps=[...])` instead of `Crew(knowledge_sources=[...])`: `crew.py`'s `researcher` gets `mcps=[MCPServerStdio(command="uvx", args=["mcp-server-fetch"])]` directly, no separate helper file — `mcp-server-fetch` is an existing, official reference server, not something built for this repo. See [Step 12](exercises/step_12_mcp.ipynb) for the underlying concept.

The table below covers the official [reference servers](https://github.com/modelcontextprotocol/servers) plus a few popular hosted ones — browse the [MCP Registry](https://registry.modelcontextprotocol.io/) for the full, ever-growing list. As with the tools table above, the setup that matters most is whether a server needs its own signup/API key, and — new for MCP — whether it runs locally via `uvx` (Python, no extra install, same as `mcp-server-fetch`) or `npx` (TypeScript/Node.js, **not** otherwise part of this repo's toolchain, so it needs installing separately).

| Category | Needs its own account/key? | Runs via | Servers |
| --- | --- | --- | --- |
| Web fetch | No | `uvx` | `mcp-server-fetch` — fetch and read one specific page (already wired into `researcher`) |
| Version control | No | `uvx` | `mcp-server-git` — read/search/diff a local git repo |
| Time & dates | No | `uvx` | `mcp-server-time` — current time / timezone conversions |
| Local files | No | `npx` | `@modelcontextprotocol/server-filesystem` — read/write files inside a directory you allow |
| Persistent memory | No | `npx` | `@modelcontextprotocol/server-memory` — knowledge-graph-based memory that persists across runs (an alternative to CrewAI's own `memory=True`) |
| Structured reasoning | No | `npx` | `@modelcontextprotocol/server-sequential-thinking` — decompose a problem into revisable thought steps |
| Web search | **Yes** | Hosted (URL) | [Exa](https://mcp.exa.ai), [Tavily](https://tavily.com), [Brave Search](https://github.com/brave/brave-search-mcp-server) |
| Docs, code & storage | **Yes** (OAuth/token) | Hosted or `npx` | GitHub, Google Drive, Slack — community-maintained, see the MCP Registry for current links |
| Job search | No (500 free calls/day) | `npx` | [JobDataLake](https://github.com/echojobsio/jdl-mcp-server) (`@jobdatalake/mcp-server`) — 1M+ job listings, filterable by skills/salary/location |

For a `uvx`/Python server, the wiring is exactly `mcp-server-fetch`'s pattern with a different package name:

```python
MCPServerStdio(command="uvx", args=["mcp-server-git"])
```

For an `npx`/Node.js server, swap the command (after installing Node.js — this repo doesn't require it otherwise):

```python
MCPServerStdio(command="npx", args=["-y", "@modelcontextprotocol/server-memory"])
```

For a hosted server reachable over HTTPS, `Agent.mcps` also accepts a plain URL string instead of an `MCPServerStdio` object — no local process at all, but you'll need that service's own API key:

```python
mcps=["https://mcp.exa.ai/mcp?api_key=your_key"]
```

## 4. Technical Setup

### IDE

Use [VS Code](https://code.visualstudio.com/) or [Cursor](https://cursor.com/) (Cursor is based on VS Code). Install these extensions:

- **Python** (`ms-python.python`)
- **Jupyter** (`ms-toolsai.jupyter`) — needed to open and run the `.ipynb` notebooks used throughout the exercises
- **GitHub Pull Requests and Issues** (`GitHub.vscode-pull-request-github`) — lets you create and review pull requests from within VS Code

### Git & GitHub setup

You'll need Git installed and the GitHub Pull Requests extension configured before you can push changes and open pull requests.

1. **Install Git** (skip if `git --version` in a terminal already works):
   - Mac: run `git --version` in Terminal — if it's missing, it'll prompt you to install the Xcode Command Line Tools, or install via [git-scm.com](https://git-scm.com/downloads).
   - Windows: download and install from [git-scm.com/downloads](https://git-scm.com/downloads) (default options are fine).
2. **Install the GitHub Pull Requests and Issues extension**: open the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`), search for **"GitHub Pull Requests and Issues"**, and click **Install**.
3. **Sign in**: click the new GitHub icon in the Activity Bar and sign in with your GitHub account when prompted.
4. **Verify**: open your cloned repo in VS Code, go to Source Control (`Cmd+Shift+G` / `Ctrl+Shift+G`) — you should see your branch and be able to commit/push. The GitHub Pull Requests view lets you create and view pull requests directly.

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
