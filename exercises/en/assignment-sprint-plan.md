# Sprint Plan — Running the Team Assignment as Scrum

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-sprint-plan.md)

This turns the [milestone ladder](assignment-milestones.md) into five Scrum sprints, one per exercise (or exercise pair). It reuses artifacts you already have — the suggested user stories from each milestone, the backlog (GitHub Issues + Projects board) from [Assignment Templates](assignment-templates.md), and `DESIGN.md` — rather than introducing new ones. Adapt the cadence to your team's real meeting schedule: a daily standup doesn't make sense for a team that meets once a week — a short async check-in (a comment on your Issues board) covers the same need.

Each sprint below has the same five parts: **Sprint Goal**, **Sprint Planning** (what to do at the start), **Definition of Done**, **Sprint Review** (what to check at the end), and a pointer to the **Sprint Retrospective** (the same three prompts every time — see the bottom of this page).

## Sprint 1: Baseline

**Tied to:** [exercise 01](01-agentic-frameworks.md) → [Milestone M0](assignment-milestones.md#m0-baseline)

**Sprint goal:** a working two-agent, sequential crew with roles your team designed, not the starter repo's `researcher`/`analyst` relabeled.

**Sprint Planning:**
- Pick your use case from the [use-case table](../../README.md#use-cases-to-pick-from), or propose your own.
- Break "design two agents + a task flow" into 2–3 user-story issues (use the [user story template](assignment-templates.md)), labeled `epic:baseline`.
- Pick this sprint's facilitator — rotate the role each sprint if your team is larger than two.

**Definition of Done:**
- `agents.yaml` and `tasks.yaml` updated with your own roles, goals, and backstories
- `DESIGN.md` sections 1–2 (Overview, Architecture) filled in, M0 rows added to the Risks/Constraints tables

**Sprint Review:** run the crew, read the output together as a team; check it against the [M0 risk prompts](assignment-milestones.md#m0-baseline) before calling it done.

## Sprint 2: Tools

**Tied to:** [exercise 02](02-tool-use.md) → [Milestone M1](assignment-milestones.md#m1-tools)

**Sprint goal:** a tool your use case actually needs, wired in and reasoned about, not added to check a box.

**Sprint Planning:**
- Pick the tool from the [README's tool table](../../README.md#adding-more-tools-or-rag-for-students) (or write a custom one per exercise 02) that your use case genuinely needs.
- Write 1–2 user-story issues labeled `epic:tools`, with acceptance criteria covering both the happy path and the failure case (rate limit / empty result / API down).

**Definition of Done:**
- `agents.yaml` (tools list) and the tool's API key in `.env`
- `DESIGN.md`'s Tools table filled in, M1 rows added to Risks/Constraints

**Sprint Review:** demo the agent actually calling the tool (not just configured); confirm the failure-mode risk prompt from [M1](assignment-milestones.md#m1-tools) has a real answer, not a placeholder.

## Sprint 3: RAG (interim submission)

**Tied to:** [exercise 03](03-agentic-rag.md) → [Milestone M2](assignment-milestones.md#m2-rag-interim-submission)

**Sprint goal:** answers grounded in a real knowledge source instead of the model guessing.

**Sprint Planning:**
- Decide what document/source actually matters for your use case (see the table's "Natural M2 RAG source" column for ideas).
- Write a user-story issue labeled `epic:rag`; if you're short on time, `knowledge_source_example.py` is a working starting point (see exercise 03).

**Definition of Done:**
- `crew.py`'s `knowledge_sources=[...]` wired in, a new file under `knowledge/`
- `DESIGN.md`'s Knowledge sources/RAG table filled in, M2 rows added to Risks/Constraints

**Sprint Review:** this is also your **interim submission** — see [M2 in the milestone ladder](assignment-milestones.md#m2-rag-interim-submission) for exactly what to submit. Double-check `DESIGN.md` sections 1–4 are complete before the deadline, not just this sprint's section.

## Sprint 4: Multi-agent

**Tied to:** [exercise 04](04-multi-agent-pattern.md) → [Milestone M3](assignment-milestones.md#m3-multi-agent)

**Sprint goal:** a third agent and a deliberate, justified process choice — not multi-agent for its own sake.

**Sprint Planning:**
- Before writing any code: as a team, argue both sides of sequential vs. hierarchical for your specific use case. Write down the losing argument too — it's good material for `DESIGN.md`'s "Alternatives considered" section.
- Write a user-story issue labeled `epic:multi-agent` for the third agent's role.

**Definition of Done:**
- Third agent added; `process` decision made and implemented
- `DESIGN.md` Architecture updated, M3 rows added to Risks/Constraints

**Sprint Review:** check the third-agent risk prompt from [M3](assignment-milestones.md#m3-multi-agent) — could you cut this agent and just give its work to one of the other two? If yes, say so honestly in `DESIGN.md` rather than defending a design that doesn't hold up.

## Sprint 5: Production and security (final submission)

**Tied to:** [exercise 05](05-production.md) + [exercise 06](06-securing-agents.md) → [Final milestone](assignment-milestones.md#final-production-and-security)

**Sprint goal:** a credible answer to "what breaks first, and how would you know" — not a feature to build.

**Sprint Planning:**
- No new user-story issues needed for new features — this sprint's "backlog" is the write-up itself. If you want one anyway, write an issue labeled `epic:hardening` for whichever gap your team finds most concerning.
- Re-read your own Sprint 1–4 retrospectives before writing the final Design History entry — that's literally the source material for "what changed and why."

**Definition of Done:**
- `DESIGN.md`'s Security & threat model and Production considerations sections complete
- A concrete, hypothetical prompt-injection scenario specific to *your* tools/knowledge sources (not the generic one from exercise 06)
- Final Design History entry answering what changed since the interim submission, and why

**Sprint Review:** this is your **final submission** — see [the Final milestone](assignment-milestones.md#final-production-and-security) for the exact deliverable list.

## The 3 retrospective prompts (every sprint)

At the end of each sprint, answer these three questions as a team:
1. What went well this sprint?
2. What didn't, and why?
3. What's the one thing you'll change next sprint?

Write the answers straight into `DESIGN.md`'s **Design history** section as that milestone's entry — your retrospective and your graded design-evolution record are the same artifact, not two separate things to maintain. This is also why Design history is append-only: a real retrospective trail, not a cleaned-up afterthought.
