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

Teams of **3–5 students** work through a sequence of versions of the same AI system on the same topic — this *is* the exercise series, not a separate thing alongside it: each step below both teaches a concept and produces output you compare directly to the previous step. The primary deliverable is `REPORT.md`: a full project report on the agent your team designs and builds, informed by what changed at each step. Start at [team_assignment/en/assignment-overview.md](team_assignment/en/assignment-overview.md) (English / [Deutsch](team_assignment/de/assignment-overview.md)) for the full grading rubric.

### Use cases to pick from

Pick one of the five use cases below. Each is designed so that the steps produce **noticeably different output**: a simple prompt gives a broad starting point, structured prompting adds focus and format, a single agent adds a consistent perspective, web search + RAG grounds the output in current, specific evidence, and a second agent transforms the grounded research into a recommendation. The quality of your evaluation depends on how well your team knows the subject — pick a topic you can actually judge.

---

**1. Job Application Tailoring Assistant**

A student applying to internships or working-student roles needs each application tailored to the specific posting — recruiters and applicant-tracking systems filter out generic, copy-pasted applications fast. *Step 03* gives you generic "how to write a cover letter" advice that could apply to any job anywhere. *Steps 04–08* add a career-coach persona and a structured bullet-point format — immediately more usable, but still generic to the role type, not the actual posting. *Step 09* gives you a job-posting analyst agent whose role keeps it focused on extracting the specific requirements and keywords from one real posting, not general career advice. *Steps 10–12* close the information gap: web search adds current company news, culture signals, and interview-process reports; the applicant's own CV as a RAG source grounds every suggestion in experience they actually have, not invented achievements. *Step 13* adds an application strategist who takes the now-grounded requirements and CV and writes a tailored pitch, mapping specific experience to specific requirements — the two agents together produce something neither produces alone.

- **Topic example:** `"Tailor an application for a [Working Student — Data Analytics] role at [Company] in [City]"`
- **Agents (Step 09, Step 13):** Job-Posting Analyst → Application Strategist
- **Tool (step 10):** `SerperDevTool` — company news, culture, interview-process reports
- **RAG source (step 12):** The applicant's own CV/resume (PDF)

---

**2. Exam Prep Coach**

A student preparing for an exam needs active recall practice — testing what they actually remember — not another pass of re-reading slides, which feels productive but barely improves retention. *Step 03* gives you a generic "how to study effectively" list, useful for no exam in particular. *Steps 04–08* add a tutor persona and a structured quiz-question format — closer to something usable, but still built from the model's general knowledge of the subject, not the actual course. *Step 09* gives you a content-reviewer agent whose role keeps it focused on identifying the key concepts likely to matter for this exam, not explaining the subject from scratch. *Steps 10–12* close the information gap: web search adds a clearer explanation or worked example for a concept the notes only mention briefly; the student's own lecture notes as a RAG source ground every question in what was actually taught, not a generic textbook version. *Step 13* adds a quiz master who takes the now-grounded key concepts and runs an actual practice round — asking questions, checking the answer, and flagging what's still shaky — the two agents together produce something neither produces alone.

- **Topic example:** `"Prepare me for the [Course Name] midterm, covering [Topic A, B, C]"`
- **Agents (Step 09, Step 13):** Content Reviewer → Quiz Master
- **Tool (step 10):** `SerperDevTool` — supplementary explanations, worked examples for tricky concepts
- **RAG source (step 12):** The student's own lecture notes or slides (PDF/text)

---

**3. Personalized Study & Semester Planner**

A student staring at a syllabus and an exam date needs a realistic day-by-day plan — not vague "study a bit every day" advice, but a schedule that actually accounts for how much time is left and how much material there is. *Step 03* gives you generic study-planning advice, the same for a two-week sprint or a full semester. *Steps 04–08* add a planner persona and a day-by-day table format — immediately more concrete, but still guessing at what the course actually covers. *Step 09* gives you a curriculum-analyst agent whose role keeps it focused on prioritizing the topics in one specific course by weight and difficulty, not studying in general. *Steps 10–12* close the information gap: web search adds effective study techniques for the specific subject (spaced repetition for vocabulary vs. worked problems for math); the course syllabus as a RAG source grounds the prioritization in what the course actually covers and how it's graded, not a generic curriculum. *Step 13* adds a study scheduler who takes the now-grounded priorities and turns them into an actual day-by-day plan that fits the available time — the two agents together produce something neither produces alone.

- **Topic example:** `"4-week study plan for the [Course Name] final exam on [date], ~1.5h on weekdays"`
- **Agents (Step 09, Step 13):** Curriculum Analyst → Study Scheduler
- **Tool (step 10):** `SerperDevTool` — effective study techniques for the specific subject
- **RAG source (step 12):** The course syllabus or module handbook (PDF)

---

**4. Inbox Triage & Draft-Reply Assistant**

Anyone running a shared inbox — a student club, a TA mailbox, a part-time job — needs incoming emails read, understood, and answered consistently, without every reply being reinvented from scratch. *Step 03* gives you a generic reply to a generic email, ignoring who's actually asking or what they actually need. *Steps 04–08* add an assistant persona and a structured reply format — sounds more consistent, but still can't tell a meeting request from a complaint. *Step 09* gives you an email-triager agent whose role keeps it focused on classifying intent and extracting the actual ask, not producing a reply yet. *Steps 10–12* close the information gap: web search looks up something the email references — a company, an event, a policy change; a personal FAQ or past-reply document as a RAG source keeps every answer consistent with actual policy and tone, not invented on the spot. *Step 13* adds a reply drafter who takes the now-grounded classification and context and writes an actual reply, flagging anything that needs a human rather than guessing — the two agents together produce something neither produces alone.

- **Topic example:** `"Triage and draft replies for incoming emails to [a student club / TA inbox]"`
- **Agents (Step 09, Step 13):** Email Triager → Reply Drafter
- **Tool (step 10):** `SerperDevTool` — look up something the email references
- **RAG source (step 12):** A personal FAQ, policy doc, or past reply examples (text file)

---

**5. Student Budget & Savings Planner**

A student managing rent, part-time income, and irregular expenses needs an actual plan — not "spend less," but a concrete monthly budget that accounts for what's coming in and going out. *Step 03* gives you generic budgeting advice that ignores anyone's actual numbers. *Steps 04–08* add a financial-coach persona and a structured budget-table format — looks like a real budget, but the numbers are invented. *Step 09* gives you a spending-analyst agent whose role keeps it focused on reviewing actual income and spending patterns, not general financial advice. *Steps 10–12* close the information gap: web search adds current student discounts, grants, or cost-of-living figures for a specific city; a budget spreadsheet or bank statement as a RAG source grounds every recommendation in actual spending, not a hypothetical student's. *Step 13* adds a budget advisor who takes the now-grounded spending picture and proposes a concrete monthly plan with explicit trade-offs — the two agents together produce something neither produces alone.

- **Topic example:** `"Monthly budget for a student earning [income], saving for [goal]"`
- **Agents (Step 09, Step 13):** Spending Analyst → Budget Advisor
- **Tool (step 10):** `SerperDevTool` — current student discounts, grants, cost-of-living data
- **RAG source (step 12):** A sample budget spreadsheet or bank statement, exported as text (a synthetic one works fine — no need to use real financial data)

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
