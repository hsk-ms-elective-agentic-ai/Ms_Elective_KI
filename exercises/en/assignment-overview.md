# Team Assignment — Design Your Own Crew

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-overview.md)

This is the graded assignment — and it's the same thing as the exercise series, not a separate track alongside it. In teams, you design a CrewAI crew for a use case of your choice, and each sprint both teaches a concept and grows your own crew with it. The primary deliverable at every stage is **your design plus your critical assessment of its risks and constraints** — working code is an optional bonus, never a requirement.

**Team size:** 3–5 students. Small enough that everyone has a real stake in the outcome, large enough to plausibly fill three distinct agent roles by Sprint 4 without one person quietly doing everything.

See [Assignment Templates](assignment-templates.md) for the documents you'll fill in (`DESIGN.md`, `TEAM.md`, user stories, peer evaluation). Sprint planning, the Definition of Done, and what to submit are built directly into each sprint's own page — there's no separate milestone ladder or sprint plan to cross-reference.

## How this works: one sprint, one concept, one piece of your crew

| Sprint | Unlocks |
| --- | --- |
| [0 — Vision & Architecture](00-vision-architecture.md) | Pick your use case, design your agents and tasks |
| [1 — First Runnable MVP](01-first-mvp.md) | A working sequential (or parallel) crew |
| [2 — Tools](02-tools.md) | A tool your use case actually needs |
| [3 — RAG](03-rag.md) | Grounded answers from a real knowledge source *(interim submission due)* |
| [4 — Dynamic Orchestration (Hierarchical)](04-dynamic-orchestration.md) | A third agent + manager-delegated process |
| [5 — Production Safety & Stability](05-production-safety.md) | Threat model, monitoring plan *(final submission due)* |

You don't redesign from scratch each sprint — you extend what you already have. Two submissions: an **interim submission** at the end of Sprint 3 (formative, lighter weight — catches weak foundations early) and a **final submission** at the end of Sprint 5 (the full design plus a retrospective on how your thinking changed).

## Team setup: repos and accounts

This course runs in a GitHub Organization, with **one private repository per team — not one per student.** You don't create this repo yourself; your instructor already generated it from the course template, one per team, and grants your team access to it once you're enrolled. See the main [README's "Getting access" section](../../README.md#getting-access-students) for the enrollment steps (GitHub account → team sign-up issue → accept invite).

**Every team member still needs their own GitHub account**, added to the team in the organization (not just to a repo directly). Two reasons: your individual commits are how contribution within the team gets assessed, and a real commit history under your own account is worth having beyond this course.

### Collaborating without git experience

You don't need branches or pull requests for day-to-day team work — one simple loop is enough:

1. Edit a file normally (in your Codespace).
2. Open the **Source Control** panel (the branching-lines icon in the sidebar).
3. Type a one-line commit message, click **✓ Commit**.
4. Click **Sync Changes** — this pulls any teammate's changes and pushes yours, in one step.

No terminal, no `git add`/`commit`/`push` commands. Everyone commits straight to `main`.

To avoid two people editing the same file at once, **divide files between teammates** where you can — e.g. one person owns `agents.yaml`, another `tasks.yaml`. `DESIGN.md` is one shared file everyone contributes to, so for that one specifically: take turns, or commit-and-sync every few minutes rather than both editing it for a long stretch in parallel. If a conflict does happen anyway, VS Code shows a merge view with clickable "Accept Current / Incoming / Both" buttons — ask your instructor for a quick live demo of this once, so it doesn't surprise anyone mid-deadline.

For quick edits (e.g. a `DESIGN.md` entry), you can skip Codespaces entirely: open the file on github.com, click the pencil icon, edit in the browser, and click **"Commit changes"** at the bottom.

## Submission package

At each submission deadline (interim: end of Sprint 3, final: end of Sprint 5), your submission is the state of your team repo's `main` branch:

| Artifact | Where | What it shows |
| --- | --- | --- |
| Executable crew config | `src/research_crew/config/agents.yaml` + `tasks.yaml` (+ `crew.py` once tools/RAG/process change) | The literal, runnable version of your design |
| Design document | `DESIGN.md` — architecture (agents/tasks/tools/RAG), risks, constraints, security, production considerations, design history | Your full design rationale, critically assessed, in one evolving report |
| Backlog | GitHub Issues (labeled by epic) + a Projects board | Your user stories and progress — lives on GitHub, nothing to export |
| Team notes | `TEAM.md` | Members and who contributed what |
| Optional bonus | a working `crew.py` + a successful `uv run research_crew` | Extra credit only — never required |

Submission is simply **the state of your team repo's `main` branch at the deadline** — there's no pull request to open. Share your repo URL once, at the start; your instructor checks your commit history against each deadline on that same repo (and may tag a specific commit for grading).

## Grading

The same weights apply at both the interim and final submission, scored against whatever's actually complete by that deadline:

| Component | Weight | What's assessed |
| --- | --- | --- |
| Architecture & design | 25% | `agents.yaml`/`tasks.yaml` + `DESIGN.md` §1–2 — is the role split genuinely suited to your use case, not a relabeled default? |
| Risk & constraint analysis | 30% | `DESIGN.md` §3–4 — specific to your design, growing across sprints, not generic |
| Security & production considerations | 15% | `DESIGN.md` §5–6 — a concrete threat model and monitoring plan for *your* design, not the generic example from sprint 5 |
| Process: backlog & epics | 15% | GitHub Issues/Project board — real user stories with acceptance criteria, Definition of Done actually used, not just checked off |
| Design history & retrospective | 15% | Honest evolution of thinking across sprints, not one polished answer written at the end |

**Optional bonus:** a working `crew.py` + a successful `uv run research_crew` — up to **+10%** extra credit on top of the above. Never required, never a substitute for a thin risk analysis.

**Individual adjustment within the team grade:** each student's share of the team grade can move by up to **±15%** based on the private [peer evaluation](assignment-templates.md#peer-evaluation-private--do-not-commit-this-to-your-repo) — submitted directly to your instructor, never committed to the repo, so feedback can be honest.

Each sprint's own page has the specific questions graded at that stage — answered directly in `DESIGN.md`, not as a separate "critical thinking" exercise.

## Agile practice: backlog and user stories

Run your design process like a real product backlog:
- Each sprint's new capability is an **epic**. Break it into 2–4 **user stories**: *"As a [stakeholder of the crew's output], I want [capability], so that [value]."*
- Write **acceptance criteria** for each story as testable conditions — these double as a draft of the task's `expected_output` field once you get to the YAML, which is a useful thing to notice in itself.
- Add "risks identified and mitigation documented" to every epic's definition of done, so risk analysis is a habit, not a one-off essay.
- If your team is larger than two, rotate a facilitator role each sprint.

Templates for all of this are in [Assignment Templates](assignment-templates.md). The sprint planning, Definition of Done, and review steps are built directly into each sprint's own "Your task" section — open the relevant sprint page when you're ready to plan it, rather than a separate sprint-plan document.

## For instructors

This is the one-time setup behind everything above. GitHub Classroom stopped taking new sign-ups in May 2026, so this replaces it with plain GitHub Organization features — Free plan covers all of it (unlimited members, unlimited private repos).

### 1. Create the organization and teams

Create a Free organization, then **Settings → Teams → New team** once per project group (e.g. `team-a`, `team-b`, ...). Optionally nest them all under one parent team (e.g. `students`) if you want a shared resources repo visible to everyone automatically — child teams inherit whatever the parent can see.

### 2. Mark this repo as a template, then generate one repo per team

This repo's **Settings → check "Template repository"**. Then per team:
```bash
gh repo create <org>/<team-slug>-crew --template <org>/<this-repo> --private
gh api repos/<org>/<team-slug>-crew/teams/<team-slug> -X PUT -f permission=admin
```
**Admin** (not just Write) matters here — managing a repo's secrets requires Admin, and you want each team able to set up their own API keys without you in the loop.

### 3. Enable Codespaces for the organization

**Org Settings → Codespaces → General** → enable for all repositories (or select the team repos specifically). On the Free plan, Codespaces usage bills to each student's own personal free quota, not the organization — no spending limit to configure.

### 4. Set up team enrollment: students submit, you decide, a workflow executes

Students submit their **email and GitHub username** via a [team sign-up issue](../../.github/ISSUE_TEMPLATE/team-signup.yml) on this repo. That alone does nothing except notify you — **you decide the team assignment yourself**, by applying a label, and a [workflow](../../.github/workflows/add-to-team.yml) does the mechanical part (adding them to the team, replying, closing the issue).

1. **Create one label per team**, named exactly `team:<team-slug>` (e.g. `team:team-a`) — **Issues → Labels → New label**, once per team.
2. **Create the automation's token**: a personal access token with **organization → Members: Read and write** and **repository → Issues: Read and write** scopes (fine-grained), or `admin:org` + `repo` (classic) — needed because team membership is an organization-level permission the default `GITHUB_TOKEN` can't grant.
3. Add it as a secret named `ORG_ADMIN_TOKEN` — either on this repo specifically (**Settings → Secrets and variables → Actions**) or at the org level scoped to this repo (**Org Settings → Secrets and variables → Actions**).
4. **Triage as sign-ups arrive**: each new issue gets an automatic comment reminding you to apply the right team label. Open the issue, use the email to figure out who this actually is against your own team list, and apply `team:<their-team-slug>` — that label *is* the trigger; the workflow reads it, adds the username, replies, and closes the issue. Wrong username or label typo? Fix it and re-apply the label to retry.

### 5. Ongoing: review submissions

Check each team's commit history on `main` at each deadline — tag a specific commit yourself (Releases → "Create a new release") if you want an immutable snapshot for grading. Solutions aren't included on purpose, the same as the rest of this series.
