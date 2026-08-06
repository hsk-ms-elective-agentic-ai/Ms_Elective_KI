# Ethics & Trustworthy AI Report — [Your Name] ([GitHub Username])

**Course:** Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI
**Team:** [Your Team Name] — **Topic:** [your team's topic]

This is your **individual** deliverable — 20% of your grade — submitted via OpenOlat, separately from your team's repo (see [Assignment Overview](assignment-overview.md#submission-package) for where and how). Even though you and your teammates are writing about the same agent, this is not a shared document: write your own analysis, in your own words, grounded in your team's actual `REPORT.md` (architecture, implementation, evaluation) and in what you personally observed while building and testing it. Two students on the same team should not read alike.

The lens for this report is **trustworthy AI**: don't just catalogue what could theoretically go wrong with agents in general — judge how trustworthy *your specific agent* actually is, and propose concrete changes that would make it more so.

> European Commission, High-Level Expert Group on AI (2019). *Ethics Guidelines for Trustworthy AI*. https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai — the framework behind the dimensions below.

Generic answers ("our agent could have bias, so we should be careful") score low. Specific, grounded ones score high — tie every claim to something concrete about *this* agent: a `role`/`goal`/`backstory` you can quote, a tool it actually calls, a memory/knowledge source it actually stores or retrieves, a real test run where something did or didn't go wrong. Each dimension below asks for two things, not one: a grounded reflection on where your agent actually stands, **and** a specific proposed change or amendment that would make it more trustworthy — not just naming a risk, but saying exactly what you'd build differently.

---

## 1. Your Agent, Briefly

_(2–4 sentences, in your own words: what does your team's agent do, and what does it actually touch — tools, memory, knowledge sources, external systems? This grounds everything below; don't just restate the Executive Summary from `REPORT.md`.)_

---

## 2. Bias & Fairness

Does your agent have the potential to exhibit bias? How might it treat different users or groups differently? What steps did you (or should you) take to mitigate bias?

- _(e.g., "Our agent uses a language model that may have been trained on biased data. I tested it with queries phrased from three different user personas and monitored for discriminatory outputs. We added explicit instructions in the agents' `backstory` to treat all users fairly.")_
- **Proposed change:** _(One concrete, specific change to your agent's design that would reduce this risk — not "be more careful," but something you could actually implement: a `backstory` addition, a test you'd add to your evaluation set, a guardrail. Be specific enough that a teammate could implement it from your sentence alone.)_

## 3. Privacy & Data Security

What data does your agent collect, store, or process? How is user data handled? What privacy concerns arise from your agent's memory or tool usage?

- _(e.g., "CrewAI's `memory=True` stores interaction data locally under `CREWAI_STORAGE_DIR`. I reviewed what gets written there and confirmed no sensitive information is included. Users can clear it via `crew.reset_memories('all')`.")_
- **Proposed change:** _(A concrete change — e.g. scoping what gets written to memory, adding a data-retention limit, restricting which fields a tool can access.)_

## 4. Transparency & Explainability

Can users understand how your agent makes decisions? Is the agent's reasoning process transparent? What happens when the agent makes a mistake?

- _(e.g., "Running with `verbose=True` exposes the agent's full ReAct reasoning trail, which we used for debugging. However, end users of our final output only see the final report, not this reasoning — I think that's a gap worth flagging because...")_
- **Proposed change:** _(A concrete change — e.g. surfacing a summary of the reasoning trail to end users, adding a confidence indicator, logging which knowledge source a claim came from.)_

## 5. Autonomy & Control

What level of autonomy does your agent have, and what safeguards are in place? Can the agent take actions that have real-world consequences? How can users override or stop the agent?

- _(e.g., "Our agent can only read data via tools/`knowledge_sources` — it has no tool that writes to or modifies an external system, so the blast radius of an error is limited to a bad answer, not a bad action.")_
- **Proposed change:** _(A concrete change — e.g. adding `Task(human_input=True)` before a consequential step, a hard cap via `max_iter`, an explicit "ask before acting" instruction in the `backstory`.)_

## 6. Misuse & Safety

How could your agent be misused? What harmful behaviors could it enable? What safety measures did you implement?

- _(e.g., "A web-search-enabled agent could be misused to gather information for harmful purposes. We scoped the Researcher's `goal`/`backstory` narrowly to our topic and did not give it unrestricted search access.")_
- **Proposed change:** _(A concrete change — e.g. narrowing a tool's scope further, adding an output guardrail that rejects certain request types, rate-limiting a sensitive action.)_

## 7. Accountability

Who is responsible when the agent makes an error or causes harm? How do you handle errors and edge cases?

- _(e.g., "We designed the agents' `expected_output` to include an explicit 'I don't know' path rather than guessing, and we log every `kickoff()`'s `tracing=True` trace URL for after-the-fact review.")_
- **Proposed change:** _(A concrete change — e.g. an explicit escalation path when the agent is uncertain, a required human sign-off before output ships, better logging of which agent/task produced a given claim.)_

---

## 8. Trustworthiness Verdict & Priority Amendments

_(1–2 paragraphs, genuinely yours: overall, how trustworthy is this agent as it stands today — not agents in general, *this* one? Of the six proposed changes above, which one would make the biggest difference, and why that one first? Would you deploy this agent as-is? If not, what's the minimum set of changes that would have to happen before you would?)_
