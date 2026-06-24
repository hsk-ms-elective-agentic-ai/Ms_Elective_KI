# Crew Design Document

**Team:** [team name] · **Topic:** [your crew's topic] · **Last updated:** [sprint, YYYY-MM-DD]

> Fill in each section as the relevant sprint unlocks it — mark later sections "not yet" rather than deleting them. For the **Risks**, **Constraints**, and **Design history** tables specifically: this is append-only — add new rows per sprint, never edit or delete a previous row. If a later sprint changes your assessment, add a new row noting the update instead. See each sprint's own page (e.g. [exercises/en/00-vision-architecture.md](exercises/en/00-vision-architecture.md), or the German twin) for what belongs in each section at each stage.

## 1. Overview
- **Problem / goal:** what is this crew for, in one or two sentences?
- **Stakeholders:** who reads the output, and what do they need from it?

## 2. Architecture

**Process:** `Process.sequential` or `Process.hierarchical` — and why this one, not the other.

### Agents
| Agent | Role | Goal | Owns which task(s) |
| --- | --- | --- | --- |
| | | | |

### Tasks
| Task | Description (summary) | Expected output | Agent | Depends on (`context`) |
| --- | --- | --- | --- | --- |
| | | | | |

### Tools
| Tool | Purpose | Why this tool for this topic | Needs API key / embeddings? | What happens if it fails |
| --- | --- | --- | --- | --- |
| | | | | |

### Knowledge sources / RAG
*(leave as "not yet added" until Sprint 3)*

| Source | Type | Why this content | Embedder | Known gaps (what's NOT covered) |
| --- | --- | --- | --- | --- |
| | | | | |

### Guardrails / trust mechanisms
*(leave as "none yet" until Sprint 5)*
-

## 3. Risks
*(append-only — add new rows per sprint, never edit old ones)*

| # | Sprint | Risk | Where it lives (agent/task/tool/RAG) | Mitigation or accepted tradeoff |
| --- | --- | --- | --- | --- |
| | | | | |

## 4. Constraints
*(append-only — add new rows per sprint, never edit old ones)*

| # | Sprint | Constraint | Type (rate limit / cost / latency / data / time / team) | How the design accounts for it |
| --- | --- | --- | --- | --- |
| | | | | |

## 5. Security & threat model
*(fill in by Sprint 5 — final submission)*
- Concrete prompt-injection scenario specific to this design:
- Secrets handling:
- Tool permission scope:

## 6. Production considerations
*(fill in by Sprint 5 — final submission)*
- What you'd monitor:
- What would alert you to failure:
- What's still missing for real production use:

## 7. Alternatives considered
- What other design did you consider (a different process, a different tool, no RAG, a different role split) and why did you reject it?

## 8. Design history
*(append-only — one entry per sprint, never edit a previous entry)*

### Sprint 0 — Baseline (YYYY-MM-DD)
**Changed:**
**Why:**
