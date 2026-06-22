# Assignment Milestones — The Crew Design Ladder

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-milestones.md)

Pick a topic for your crew before M0 — anything a two-agent research/analysis pipeline could plausibly tackle (a market, a technology, a policy question, a historical case). You'll keep the same topic through every milestone.

## M0: Baseline

**Unlocked by:** lectures 02–03

**Add:** two agents, a sequential process, no tools beyond what's already wired in the starter repo.

**Update:** `agents.yaml`, `tasks.yaml`.

**Risk & constraint prompts** (answer in `RISK_LOG.md`):
- Why this specific role split? What does each agent need from the other to do its job?
- What happens if one agent's output is subtly wrong — does the next agent have any way to notice, or does it trust it blindly?

**Suggested user story starter:** *"As a [reader of the final report], I want the analyst's conclusions to be traceable back to the researcher's findings, so that I can judge whether the conclusion is actually supported."*

## M1: Tools

**Unlocked by:** lecture 04

**Add:** one or two tools from `crewai_tools` (see the [README's tool table](../../README.md#adding-more-tools-or-rag-for-students)), chosen because your topic actually needs them — not just to check a box.

**Update:** `agents.yaml` (tools list), tool API key in `.env`.

**Risk & constraint prompts:**
- What happens if the tool is rate-limited, returns nothing useful, or the API is down mid-run? Does your crew degrade gracefully or just fail?
- Does the tool's description make misuse likely (e.g. the agent calling it with bad arguments, or not calling it when it should)?

**Suggested user story starter:** *"As a [stakeholder], I want the researcher to pull current information rather than relying on the LLM's training data, so that the report reflects up-to-date facts."*

## M2: RAG (interim submission)

**Unlocked by:** lecture 05

**Add:** a knowledge source (`TextFileKnowledgeSource`, `StringKnowledgeSource`, or `PDFKnowledgeSource`) relevant to your topic, using the Gemini embedder already configured in `crew.py`.

**Update:** `crew.py` (`knowledge_sources=[...]`), a new file under `knowledge/`.

**Risk & constraint prompts:**
- What's missing or stale in your knowledge source, and what does the agent do when retrieval returns nothing relevant — guess, refuse, or say it doesn't know?
- Embeddings have their own rate limits, separate from the chat LLM's. If a classmate uploaded a 100-page document instead of your few pages, would your design still work, or would it need pacing/retries?

**Suggested user story starter:** *"As a [stakeholder], I want answers grounded in [your specific source], so that the agent doesn't fabricate facts it was never given."*

**→ Interim submission is due at the end of this milestone.** Submit: `agents.yaml`, `tasks.yaml`, `RISK_LOG.md` (M0–M2 sections), and your backlog (Issues + Project board) as they stand.

## M3: Multi-agent and trust

**Unlocked by:** lectures 06 + 08

**Add:** a third agent, a decision between `Process.sequential` and `Process.hierarchical` (justify it), and a `guardrail` on at least one task.

**Update:** `crew.py`, `agents.yaml`, `tasks.yaml`.

**Risk & constraint prompts:**
- If you went hierarchical: what is the manager actually optimizing for when it delegates, and could that diverge from what you want? If you stayed sequential: what would hierarchical have bought you, and why wasn't it worth the cost?
- What specifically does your guardrail catch, and what plausible failure would it miss?

**Suggested user story starter:** *"As a [stakeholder], I want a check before the final report ships, so that an obviously broken or off-topic output never reaches me."*

## Final: Production and security

**Unlocked by:** lectures 10 + 14

**Add:** a short production plan (what you'd monitor, what would alert you to failure) and a threat model (what's the realistic prompt-injection or secret-leak risk for your specific topic and tools).

**Update:** no required code changes — this milestone is about the write-up.

**Risk & constraint prompts:**
- If this crew ran unattended for a semester on your topic, what's the first thing that breaks, and how would you know?
- Given the actual tools/knowledge sources your crew uses, construct one concrete (hypothetical, not executed) prompt-injection scenario specific to your design — not the generic one from lecture 14.

**Final submission:** everything above, plus `RETROSPECTIVE.md` answering: *what changed between your interim and final design, and what did you learn that made you change it?* That question is worth more than it looks — it's the one place you have to show your reasoning evolved, not just accumulated.
