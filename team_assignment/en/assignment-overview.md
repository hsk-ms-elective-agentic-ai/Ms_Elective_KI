# Team Assignment — Evaluate the Progression

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-overview.md)

This is the graded assignment, and it builds directly on the exercise series, but the two halves are split differently than you might expect. Individually, each of you works through the exercise notebooks on your own — in class or at home; they're not part of the team repo. As a team, you then design and build your own agent on your own topic, organized into four sprints (preceded by a Sprint 0 setup phase), folding one new layer into the design each sprint. The graded deliverables are your team's Project Report (`REPORT.md`, 40%), Final Presentation (30%), and a working Code implementation (10%, either `src/` or reworked exercise notebooks — pick one), plus an Ethics Report each of you writes and submits **individually** (20%). Your team also gives an Interim Presentation after sprint 2 — a required live checkpoint, but not separately graded.

**Team size:** 3–5 students.

See [Assignment Templates](assignment-templates.md) for the documents you'll fill in (`REPORT.md`, `TEAM.md`, Ethics Report).

## How this works: one sprint, one layer, one comparison

Each sprint pairs an individual exercise-notebook range (do these yourselves — they aren't part of the team repo) with a team design task: fold that sprint's concept into your own agent, capture the decision in `REPORT.md`, and open a `sprint-<N>` → `main` PR before the next sprint starts. Building it out — either in `src/`, or as your own topic worked into copies of the exercise notebooks — counts toward your grade (Code, 10% — see [Grading](#grading), pick one path); it doesn't have to be complete at every sprint PR, only the final state of `main` is graded.

| Sprint | Dates | Individual exercises (Steps) | Team design task |
| --- | --- | --- | --- |
| 0 | 08.10.–22.10. | [Steps 00–01 — Setup & Python Basics](../../exercises/step_00_setup_and_python_basics.ipynb) | Technical setup — get your environment and team backlog ready, no PR required *(see checklist below)* |
| 1 | 22.10.–05.11. | [Steps 02–07 — Zero-Shot & Prompting Techniques](../../exercises/step_02_zero_shot_prompting.ipynb) | The bare API call through several prompting techniques — design your own agent's baseline prompt, before CrewAI enters the picture |
| 2 | 05.11.–19.11. | [Steps 08–09 — Introduction to CrewAI & Single Agent](../../exercises/step_08_intro_to_crewai.ipynb) | CrewAI's `Agent`/`Task`/`Crew`, then design your own single agent *(Interim Presentation)* |
| 3 | 19.11.–03.12. | [Steps 10–13 — Memory, Tools, MCP & RAG](../../exercises/step_10_memory.ipynb) | Recall across calls, plus external grounding: web search, an MCP server, document retrieval — decide which of these your own agent actually needs |
| 4 | 03.12.–17.12. | [Step 14 — Multi-Agent](../../exercises/step_14_multi_agent_seq.ipynb) | Role specialization + output chaining — design the second agent your own case study needs *(Final Presentation)* |

You don't redesign anything between sprints — you add one design layer each time, on the same topic throughout. Two live milestones: the **Interim Presentation** after sprint 2 (a required checkpoint, not separately graded), and the **Final Presentation** after sprint 4 (30% of your grade). Your individual Ethics Report is due separately, alongside the final deadline — see [Grading](#grading) for exactly where to submit it.

**Sprint 0 checklist** — before Sprint 1 starts, as a team:

- [ ] Every member has a GitHub account and access to your team repo ([Getting access](../../README.md#getting-access-students))
- [ ] Clone your team repo and get [Run the crew](../../README.md#run-the-crew) working locally: install dependencies with `uv sync`, get your API keys and fill in `.env`, register the Jupyter kernel ([Getting started](../../README.md#getting-started)) — if Git, `uv`, or Jupyter are new to you, work through [Steps 00–01](../../exercises/step_00_setup_and_python_basics.ipynb) first
- [ ] Set up your Milestones, Project board, and draft your team's initial product backlog as *User story* issues in your repo's Issues tab, covering what you want your agent to eventually do (see [One-time setup](#one-time-setup-do-this-during-sprint-0) below)

Nothing to merge for Sprint 0 — it's setup, not a sprint deliverable.

## Team setup: repos and accounts

This course runs in a GitHub Organization, with **one private repository per team — not one per student.** You don't create this repo yourself; your instructor generates it from the course template, one per team, and grants your team access once you're enrolled. See the main [README's "Getting access" section](../../README.md#getting-access-students) for the enrollment steps.

**Every team member still needs their own GitHub account**, added to the team in the organization. Your individual commits are how contribution within the team gets assessed.

### Collaborating without git experience

One branch per sprint, one pull request to close it out — beyond that, day-to-day work is the same simple loop as committing straight to `main`:

1. **At the start of each sprint**, create a branch named `sprint-<N>` (e.g. `sprint-2`): click the branch name in the bottom-left corner of VS Code → **Create new branch...**. Everyone on the team works on this same branch for the rest of the sprint.
2. Edit a file normally (in VS Code/Cursor).
3. Open the **Source Control** panel (the branching-lines icon in the sidebar).
4. Type a one-line commit message, click **✓ Commit**.
5. Click **Sync Changes** — this pulls any teammate's changes and pushes yours, in one step.
6. **At the end of the sprint**, open a pull request from `sprint-<N>` into `main` — GitHub shows a "Compare & pull request" banner right after you push a new branch, or use the **GitHub Pull Requests** panel in VS Code. Skim the diff as a team, then merge it yourselves — no approval needed. Start the next sprint by branching `sprint-<N+1>` from the now-updated `main`.

No terminal, no `git add`/`commit`/`push`/`merge` commands.

**Divide files between teammates** where you can — e.g. one person runs Step 09 and drafts the Architecture section of `REPORT.md`, another runs Step 11 and drafts the Tools subsection. `REPORT.md` is one shared file everyone contributes to, so take turns, or commit-and-sync every few minutes rather than editing it in parallel for a long stretch.

For quick edits without opening your local setup: open the file on github.com, switch the branch dropdown to your current `sprint-<N>` branch, click the pencil icon, edit in the browser, and click **"Commit changes"**.

## Working like an agile team: sprints, user stories & issues

*(If your separate Agile lecture already covered Scrum/Kanban theory, skip straight to "One-time setup" below — this section is only the "how" in GitHub.)*

Beyond the git mechanics above, your team also needs to plan and track *what* you're building each sprint, not just push code. You're already running this course as four sprints (the table at the top) — this section is about running each one the way an agile team would, using GitHub's own issue tracker instead of a separate tool.

A quick vocabulary bridge, in case the lecture hasn't reached this yet:

- **User story** — one concrete, closeable piece of work, ideally phrased as *"As a ___, I want ___, so that ___."* A sprint breaks down into roughly 3–6 of these.
- **Backlog** — everything not yet done: open issues not yet in progress.
- **Board** — a visual view of stories moving through states (To do → In progress → Done).

That's the whole vocabulary — the reasoning behind sprints, story-splitting, or estimation is what the separate Agile lecture covers. Here, it's just wiring these onto GitHub features you already have:

| Agile concept | GitHub feature | Use it like this |
| --- | --- | --- |
| Sprint | Milestone | One milestone per sprint: `Sprint 1` … `Sprint 4` |
| User story | Issue | One issue per concrete task; phrase the title as a story where it fits |
| Sprint backlog & board | Project (board view) | Columns: Backlog → To do → In progress → In review → Done |
| "This code closes that story" | PR description | `Closes #12` in your `sprint-<N>` PR — merging auto-closes the issue |

### One-time setup (do this during Sprint 0)

1. **Milestones** — **Issues → Milestones → New milestone**, once per sprint: `Sprint 1` … `Sprint 4`. Paste that sprint's "Team design task" cell from the table at the top as the description.
2. **Project board** — **Projects → New project → Board**. Add columns `Backlog`, `To do`, `In progress`, `In review`, `Done`.
3. **Issue template** — this repo already ships a *User story* issue template (**New issue → User story**): [`.github/ISSUE_TEMPLATE/user-story.yml`](../../.github/ISSUE_TEMPLATE/user-story.yml). It pre-fills the As a/I want/so that shape plus acceptance criteria.

### Running each sprint

1. **Sprint planning** (start of sprint, ~15 min, whole team): re-read that sprint's "Team design task" cell from the table at the top, and break it into 3–6 issues using the *User story* template. Set each one's milestone to the current sprint, assign an owner, and put it in "To do."
2. **During the sprint**: as you work, move your own issues across the board (`To do` → `In progress` → `In review` → `Done`) and reference the issue number in commits (`#12`) so the history stays traceable.
3. **Sprint review** (end of sprint, right before opening the PR): walk the board together as a team — everything in `Done` should be visible in the diff you're about to merge; anything unfinished rolls into next sprint's backlog rather than blocking the PR.
4. **Close the loop**: put `Closes #12` (and any others) in your `sprint-<N>` → `main` PR description — merging it auto-closes those issues and completes the milestone.

## Submission package

### Team repo (shared — `REPORT.md` and `src/` are graded directly from here)

| Artifact | Where | What it shows |
| --- | --- | --- |
| Project Report (40%) | `REPORT.md` — sprint progression, architecture, implementation, evaluation, theory | Your team's actual design decisions, specifically grounded in your topic — graded directly, and also the material your presentations are built from |
| Sprint history | one merged pull request per sprint (`sprint-<N>` → `main`) | A reviewable diff of how the design progressed each sprint |
| Team notes | `TEAM.md` | Members and who contributed what |
| Code (10%) | Either `src/` (agents, tasks, tools, config) or reworked exercise notebooks — pick one | Your working implementation — required, graded from your commit history and pull requests (see Grading) |

The chain of merged sprint PRs is what your instructor reads to follow how the design progressed, rather than diffing raw commit history by hand. Use the PR description to note what you decided and why at each step. If your team would rather not use the Markdown/GitHub workflow for the Project Report itself, a Word document submitted via OpenOlat is also accepted — see Grading below.

### Individual submission (per student — not via the repo)

Each of you writes your own copy of [`ethics-report-template.md`](ethics-report-template.md) and submits it via OpenOlat (not committed to GitHub) by the final deadline. Worth 20% of your grade, individually — see Grading below.

The Interim and Final Presentations aren't repo artifacts either — they're live talks; upload your slides to OpenOlat, nothing to commit in the repo for them.

## Grading

The final grade has four components — three are team grades, one is graded individually per student:

| Component | Weight | Team or individual? | What's assessed |
| --- | --- | --- | --- |
| Project Report | 40% | Team | Your `REPORT.md` — architecture, implementation choices, evaluation, theory, grounded specifically in your team's actual topic, not generic claims. Submitted via this repo (Markdown) or, if your team prefers, as a Word document via OpenOlat. |
| Final Presentation | 30% | Team | A live, in-class walkthrough of your agent's design — what it does, why you designed it this way, and a live demo of it actually running. Every team member should speak to at least one part. Plan for roughly 10 minutes + Q&A (your instructor may adjust this for class size); a working live demo is strongly preferred, but prepare a short recorded fallback in case of API hiccups during the talk. Upload your slides to OpenOlat; the grade itself comes from the live talk in the final course session, after the final submission deadline. |
| Ethics Report | 20% | **Individual** | Your own [`ethics-report-template.md`](ethics-report-template.md), submitted via OpenOlat, not GitHub (see Submission package above). Judges your agent against the EU's trustworthy-AI framework — graded on how specifically and honestly it engages with each dimension, grounded in your team's actual agent and your own observations, and on the concrete changes you propose to improve trustworthiness — not generic claims. Listed as "Schriftliche Ausarbeitung" on the official grading sheet. |
| Code | 10% | Team | A working implementation of your design that actually runs — pick **one** of two paths, not both: the `src/` template built out with your own agents/tasks/tools, or copies of the relevant exercise notebooks reworked with your own topic and committed to this repo. Either way, judged from your commit history and pull requests: does it run end-to-end without errors, is it reasonably organized, and does it match what `REPORT.md` describes? |

Your team also gives an **Interim Presentation** after sprint 2 — same format as the Final Presentation, and just as mandatory, but it isn't separately graded: it exists to surface design problems early, while there's still time to fix them before the deadlines above.

## For instructors

This is the one-time setup behind everything above. GitHub Classroom stopped taking new sign-ups in May 2026, so this replaces it with plain GitHub Organization features — Free plan covers all of it (unlimited members, unlimited private repos).

### 1. Create the organization and teams

Create a Free organization, then **Settings → Teams → New team** once per project group (e.g. `team-a`, `team-b`, ...). Optionally nest them all under one parent team (e.g. `students`) if you want a shared resources repo visible to everyone automatically.

### 2. Mark this repo as a template, then generate one repo per team

This repo's **Settings → check "Template repository"**. Then per team:
```bash
gh repo create <org>/<team-slug>-crew --template <org>/<this-repo> --private
gh api repos/<org>/<team-slug>-crew/teams/<team-slug> -X PUT -f permission=admin
```
**Admin** (not just Write) matters — managing a repo's secrets requires Admin, and you want each team able to set up their own API keys without you in the loop.

### 3. Set up team enrollment: students submit, you decide, a workflow executes

Students submit their **email and GitHub username** via a [team sign-up issue](../../.github/ISSUE_TEMPLATE/team-signup.yml) on this repo. That alone does nothing except notify you — **you decide the team assignment yourself**, by applying a label, and a [workflow](../../.github/workflows/add-to-team.yml) does the mechanical part.

1. **Create one label per team**, named exactly `team:<team-slug>` — **Issues → Labels → New label**, once per team.
2. **Create the automation's token**: a personal access token with **organization → Members: Read and write** and **repository → Issues: Read and write** scopes (fine-grained), or `admin:org` + `repo` (classic).
3. Add it as a secret named `ORG_ADMIN_TOKEN`.
4. **Triage as sign-ups arrive**: open the issue, apply `team:<their-team-slug>` — the workflow adds the username, replies, and closes the issue.

### 4. Ongoing: review submissions

Each team merges one pull request per sprint (`sprint-<N>` → `main`) — review that PR's diff on GitHub (**Pull requests → Closed**) for what was designed and decided. Grade `REPORT.md` (Project Report, 40%) and the team's Code (10%, either `src/` or reworked exercise notebooks) from the state of `main` at the final deadline, using the chain of merged sprint PRs as the step-by-step record of how the design got there — unless a team submitted the report as a Word document via OpenOlat instead. Grade the Final Presentation (30%) live; the Interim Presentation after sprint 2 is mandatory but not separately graded. Ethics Reports (20%, individual) arrive separately via OpenOlat, one per student — grade those individually. Solutions aren't included on purpose.
