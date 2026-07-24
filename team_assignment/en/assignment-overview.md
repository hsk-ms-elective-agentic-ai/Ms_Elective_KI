# Team Assignment — Evaluate the Progression

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-overview.md)

This is the graded assignment — and it's the same thing as the exercise series, not a separate track alongside it. In teams, you work through a sequence of versions of the same AI system on the same topic, organized into four sprints (preceded by a Sprint 0 setup phase), adding one layer at each sprint, and evaluate what each layer actually changes. The primary deliverable is `REPORT.md`: a full project report — architecture, implementation choices, evaluation, and ethical considerations — for the agent your team designs and builds, informed by everything you observe running the exercise sprints.

**Team size:** 3–5 students.

See [Assignment Templates](assignment-templates.md) for the documents you'll fill in (`REPORT.md`, `TEAM.md`, peer evaluation).

## How this works: one sprint, one layer, one comparison

| Sprint | Dates | Steps | Adds |
| --- | --- | --- | --- |
| 0 | 08.10.–22.10. | [Steps 00–02 — Setup, Python Basics & Intro to CrewAI](../../exercises/en/step_00_setup_and_python_basics.ipynb) | Technical setup — get your environment and team backlog ready, no PR required *(see checklist below)* |
| 1 | 22.10.–05.11. | [Steps 03–08 — Zero-Shot & Prompting Techniques](../../exercises/en/step_03_zero_shot_prompting.ipynb) | The bare API call through a role + output structure — your baseline through prompting |
| 2 | 05.11.–19.11. | [Step 09 — Single Agent](../../exercises/en/step_09_single_agent.ipynb) | The CrewAI framework loop *(interim submission due)* |
| 3 | 19.11.–03.12. | [Steps 10–12 — Tools, MCP & RAG](../../exercises/en/step_10_tools.ipynb) | External grounding: web search, an MCP server, document retrieval |
| 4 | 03.12.–17.12. | [Step 13 — Multi-Agent](../../exercises/en/step_13_multi_agent_seq.ipynb) | Role specialization + output chaining *(final submission due)* |

You don't redesign anything between sprints — you add one piece each time, running on the same topic throughout. Two submissions: an **interim submission** after Step 09 (sprint 2), which includes a short interim presentation, and a **final submission** after Step 13 (sprint 4).

**Sprint 0 checklist** — before Sprint 1 starts, as a team:

- [ ] Every member has a GitHub account and access to your team repo ([Getting access](../../README.md#getting-access-students))
- [ ] Clone your team repo and get [Run the crew](../../README.md#run-the-crew) working locally: install dependencies with `uv sync`, get your API keys and fill in `.env`, register the Jupyter kernel ([Getting started](../../README.md#getting-started)) — if Git, `uv`, Jupyter, or Python itself are new to you, work through [Steps 00–02](../../exercises/en/step_00_setup_and_python_basics.ipynb) first
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

**Divide files between teammates** where you can — e.g. one person runs Step 09 and drafts the Architecture section of `REPORT.md`, another runs Step 10 and drafts the Tools subsection. `REPORT.md` is one shared file everyone contributes to, so take turns, or commit-and-sync every few minutes rather than editing it in parallel for a long stretch.

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

1. **Milestones** — **Issues → Milestones → New milestone**, once per sprint: `Sprint 1` … `Sprint 4`. Paste that sprint's "Adds" cell from the table at the top as the description.
2. **Project board** — **Projects → New project → Board**. Add columns `Backlog`, `To do`, `In progress`, `In review`, `Done`.
3. **Issue template** — this repo already ships a *User story* issue template (**New issue → User story**): [`.github/ISSUE_TEMPLATE/user-story.yml`](../../.github/ISSUE_TEMPLATE/user-story.yml). It pre-fills the As a/I want/so that shape plus acceptance criteria.

### Running each sprint

1. **Sprint planning** (start of sprint, ~15 min, whole team): re-read that sprint's "Adds" cell from the table at the top, and break it into 3–6 issues using the *User story* template. Set each one's milestone to the current sprint, assign an owner, and put it in "To do."
2. **During the sprint**: as you work, move your own issues across the board (`To do` → `In progress` → `In review` → `Done`) and reference the issue number in commits (`#12`) so the history stays traceable.
3. **Sprint review** (end of sprint, right before opening the PR): walk the board together as a team — everything in `Done` should be visible in the diff you're about to merge; anything unfinished rolls into next sprint's backlog rather than blocking the PR.
4. **Close the loop**: put `Closes #12` (and any others) in your `sprint-<N>` → `main` PR description — merging it auto-closes those issues and completes the milestone.

## Submission package

At each submission deadline (interim: after Step 09, final: after Step 13), your submission is the state of your team repo's `main` branch:

| Artifact | Where | What it shows |
| --- | --- | --- |
| Report document | `REPORT.md` — sprint progression, architecture, implementation, evaluation, and ethics of your own agent | Your actual project report, specifically grounded in your topic |
| Code edits | Any changes you made to the exercise scripts (e.g. TOPIC, custom knowledge sources) | What you actually ran |
| Sprint history | one merged pull request per sprint (`sprint-<N>` → `main`) | A reviewable diff of what changed each sprint |
| Team notes | `TEAM.md` | Members and who contributed what |

The chain of merged sprint PRs is what your instructor reads to follow how the work progressed, rather than diffing raw commit history by hand. Use the PR description to note what you ran and what you found at each step.

The Interim and Final Presentations (see Grading below) aren't repo artifacts — they're live talks, nothing to commit for them.

## Grading

The final grade has three components:

| Component | Weight | What's assessed |
| --- | --- | --- |
| Interim Presentation | 10% | A short live walkthrough of progress so far, given at the interim submission (after Step 09, sprint 2) — what you've built, what you've learned, and what's planned for the remaining sprints. Every team member should speak to at least one part. |
| Report (`REPORT.md`) | 70% | See the breakdown below. Assessed once, at the final submission. |
| Final Presentation | 20% | A live, in-class walkthrough of your agent — what it does, why you built it this way, and a live demo of it actually running. Every team member should speak to at least one part. Plan for roughly 10 minutes + Q&A (your instructor may adjust this for class size); a working live demo is strongly preferred, but prepare a short recorded fallback in case of API hiccups during the talk. No separate file to submit — this happens live in the final course session, after the final submission deadline. |

The Report's 70% breaks down further into four sub-criteria:

| Sub-criterion | Weight (of total grade) | What's assessed |
| --- | --- | --- |
| Report quality | 28% | `REPORT.md` — is the analysis specific and honest, grounded in your own agent's actual behavior and the exercise steps you ran, not generic claims? |
| Critical reflection | 21% | Does the team understand *why* each design choice matters? Do they connect it to their specific topic and agent rather than giving generic answers? |
| Design & conclusion | 14% | Is the agent's architecture (Section 3) reasoned and specific to their use case — not "RAG + Tools is always best" — and does the Conclusion (Section 8) honestly assess whether they met their objectives? |
| Process (PRs, team) | 7% | One clean PR per sprint, all team members contributing, PR descriptions say what was run, `REPORT.md`'s Sprint Progression table kept current sprint-by-sprint |

**Optional bonus:** a working implementation that actually runs end-to-end (`crew.kickoff()` completes without errors, code is reasonably organized, and matches what `REPORT.md` describes), and/or a working custom setup (modified agents, custom knowledge source, different topic variations tested) — up to **+10%** extra credit combined. Never required, never a substitute for a thin evaluation.

**Individual adjustment within the team grade:** each student's share of the team grade can move by up to **±15%** based on the private [peer evaluation](assignment-templates.md#peer-evaluation-private--do-not-commit-this-to-your-repo) — submitted directly to your instructor, never committed to the repo.

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

Each team merges one pull request per sprint (`sprint-<N>` → `main`) — review that PR's diff on GitHub (**Pull requests → Closed**) for what was run and what was observed. Grade against the state of `main` at each deadline, using the chain of merged sprint PRs as the step-by-step record. Solutions aren't included on purpose.
