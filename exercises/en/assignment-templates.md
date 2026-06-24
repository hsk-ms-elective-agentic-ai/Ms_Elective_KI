# Assignment Templates

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-templates.md)

**`DESIGN.md` and `TEAM.md` already exist at your repo root** — every team's "Use this template" copy starts with them already in place, same as `knowledge/user_preference.txt` or `.env.example`. Fill them in directly rather than recreating them; they're reproduced below for reference. The user story format further down is for GitHub Issues, which you create yourself — there's no file for that one. See [Assignment Overview](assignment-overview.md) for how they're used — each sprint's own page (starting at [Sprint 0](00-vision-architecture.md)) says what to write at that stage.

## `DESIGN.md`

This is the main report: a structured design document for your crew's architecture, covering what you built, why, and what could go wrong. Fill in each section as the relevant sprint unlocks it — mark later sections "not yet" rather than deleting them. For the **Risks**, **Constraints**, and **Design history** tables specifically: this is append-only — add new rows per sprint, never edit or delete a previous row. If a later sprint changes your assessment, add a new row noting the update instead.

```markdown
# Crew Design Document

**Team:** [team name] · **Topic:** [your crew's topic] · **Last updated:** [sprint, YYYY-MM-DD]

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

### Sprint 2 — Tools (YYYY-MM-DD)
**Changed:**
**Why:**
```

At the final submission, the last Design History entry should answer specifically: *what changed between your interim and final design, and what did you learn that made you change it?*

## User story (per epic, in a GitHub Issue)

```markdown
**Story:** As a [stakeholder of the crew's output], I want [capability], so that [value].

**Acceptance criteria:**
- [ ] [testable condition 1]
- [ ] [testable condition 2]

**Definition of done:**
- [ ] Implemented in `agents.yaml`/`tasks.yaml`/`crew.py`
- [ ] Risk identified and logged in `DESIGN.md`'s Risks table
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub handle | Primary contribution |
| --- | --- | --- |
| ... | ... | ... |

Topic: [your crew's topic]
```

## Peer evaluation (private — do not commit this to your repo)

Submit this directly to your instructor (email, not GitHub) at each submission deadline. Keeping it out of the shared repo — where teammates would see it — is what makes honest feedback possible; this is what feeds the individual adjustment described in [Assignment Overview](assignment-overview.md#grading).

```markdown
# Peer Evaluation — [your name] — [interim / final]

## Your teammates
One section per teammate, not yourself:

### [Teammate name]
- Contribution (1–5, 5 = pulled their full share or more):
- What did they actually do this stage, specifically?
- Anything else your instructor should know? (optional, confidential)

## Yourself
- What did you contribute this stage, specifically?
```
