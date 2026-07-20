# Team Assignment — Evaluate the Progression

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-overview.md)

This is the graded assignment — and it's the same thing as the exercise series, not a separate track alongside it. In teams, you work through five versions of the same AI system on the same topic, adding one layer at each step, and evaluate what each layer actually changes. The primary deliverable is `EVALUATION.md`: a comparative analysis of what you observed and what it means for your use case.

**Team size:** 3–5 students.

See [Assignment Templates](assignment-templates.md) for the documents you'll fill in (`EVALUATION.md`, `TEAM.md`, peer evaluation).

## How this works: one step, one layer, one comparison

| Step | Adds |
| --- | --- |
| [1 — Zero-Shot Prompting](prompting/step_01_zero_shot_prompting.ipynb) | The bare API call — your baseline |
| [2 — Prompt Template](prompting/02-prompt-template.md) | A role + output structure, same call |
| [3 — Single Agent](agents/03-single-agent.md) | The CrewAI framework loop *(interim submission due)* |
| [4 — Multi-Agent](agents/04-multi-agent.md) | Role specialization + task chaining |
| [5 — RAG + Tools](agents/05-rag-and-tools.md) | External grounding: web search + document retrieval *(final submission due)* |

You don't redesign anything between steps — you add one piece each time, running on the same topic throughout. Two submissions: an **interim submission** after Step 3 and a **final submission** after Step 5.

## Team setup: repos and accounts

This course runs in a GitHub Organization, with **one private repository per team — not one per student.** You don't create this repo yourself; your instructor generates it from the course template, one per team, and grants your team access once you're enrolled. See the main [README's "Getting access" section](../../README.md#getting-access-students) for the enrollment steps.

**Every team member still needs their own GitHub account**, added to the team in the organization. Your individual commits are how contribution within the team gets assessed.

### Collaborating without git experience

One branch per step, one pull request to close it out — beyond that, day-to-day work is the same simple loop as committing straight to `main`:

1. **At the start of each step**, create a branch named `sprint-<N>` (e.g. `sprint-2`): click the branch name in the bottom-left corner of VS Code → **Create new branch...**. Everyone on the team works on this same branch for the rest of the step.
2. Edit a file normally (in VS Code/Cursor).
3. Open the **Source Control** panel (the branching-lines icon in the sidebar).
4. Type a one-line commit message, click **✓ Commit**.
5. Click **Sync Changes** — this pulls any teammate's changes and pushes yours, in one step.
6. **At the end of the step**, open a pull request from `sprint-<N>` into `main` — GitHub shows a "Compare & pull request" banner right after you push a new branch, or use the **GitHub Pull Requests** panel in VS Code. Skim the diff as a team, then merge it yourselves — no approval needed. Start the next step by branching `sprint-<N+1>` from the now-updated `main`.

No terminal, no `git add`/`commit`/`push`/`merge` commands.

**Divide files between teammates** where you can — e.g. one person runs step 3 and writes that section of `EVALUATION.md`, another runs step 4. `EVALUATION.md` is one shared file everyone contributes to, so take turns, or commit-and-sync every few minutes rather than editing it in parallel for a long stretch.

For quick edits without opening your local setup: open the file on github.com, switch the branch dropdown to your current `sprint-<N>` branch, click the pencil icon, edit in the browser, and click **"Commit changes"**.

## Submission package

At each submission deadline (interim: after Step 3, final: after Step 5), your submission is the state of your team repo's `main` branch:

| Artifact | Where | What it shows |
| --- | --- | --- |
| Evaluation document | `EVALUATION.md` — step-by-step observations, comparisons, final recommendation | Your actual comparative analysis, specifically grounded in your topic |
| Code edits | Any changes you made to the exercise scripts (e.g. TOPIC, custom knowledge sources) | What you actually ran |
| Step history | one merged pull request per step (`sprint-<N>` → `main`) | A reviewable diff of what changed each step |
| Team notes | `TEAM.md` | Members and who contributed what |

The chain of merged sprint PRs is what your instructor reads to follow how the work progressed, rather than diffing raw commit history by hand. Use the PR description to note what you ran and what you found at each step.

## Grading

The same weights apply at both the interim and final submission, scored against whatever's complete by that deadline:

| Component | Weight | What's assessed |
| --- | --- | --- |
| Evaluation quality | 40% | `EVALUATION.md` — are the step-by-step comparisons specific and honest? Do they identify real differences, not just "it's better"? |
| Critical reflection | 30% | Does the team understand *why* each step differs? Do they connect it to their specific topic rather than giving generic answers? |
| Final recommendation | 20% | Is the recommendation for their use case reasoned and specific — not "RAG + Tools is always best"? |
| Process (PRs, team) | 10% | One clean PR per step, all team members contributing, PR descriptions say what was run |

**Optional bonus:** a working custom setup (modified agents, custom knowledge source, different topic variations tested) — up to **+10%** extra credit. Never required, never a substitute for a thin evaluation.

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

Each team merges one pull request per step (`sprint-<N>` → `main`) — review that PR's diff on GitHub (**Pull requests → Closed**) for what was run and what was observed. Grade against the state of `main` at each deadline, using the chain of merged sprint PRs as the step-by-step record. Solutions aren't included on purpose.
