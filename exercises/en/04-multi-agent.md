# Step 4 — Multi-Agent

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/04-multi-agent.md)

Add a second agent with a different, complementary role. The researcher gathers and structures; the analyst receives that output and challenges it, extracting strategic implications a pure researcher wouldn't. Sequential pipeline: `researcher → analyst`. This is multi-agent in the simplest sense — not dynamic delegation, just role specialization with task chaining.

## Background

A single agent can do multiple things, but it can't embody genuinely different epistemic roles at the same time — it can't be simultaneously credulous (collecting everything it can find) and skeptical (questioning what it just found). Multiple agents let you encode that tension into the architecture. The seminal demonstration that agents can collaborate via conversation rather than a shared database was:

> Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

![AutoGen: conversable, customizable agents that converse to solve tasks in joint or hierarchical patterns](../assets/autogen-wu2023-fig1.png)
*Figure 1 from Wu et al. (2023): AutoGen agents solving tasks through multi-turn conversation. Reproduced for educational use in this course.*

The CrewAI version here is simpler: no conversation loop, just a one-way handoff of the researcher's output to the analyst via `context=[research_task]`.

## The code

Open [src/exercises/step_04_multi_agent.py](../../src/exercises/step_04_multi_agent.py). The additions from step 3:

| Added | What it does |
| --- | --- |
| `analyst = Agent(...)` | Second agent, explicitly skeptical role |
| `analysis_task` | Task assigned to the analyst, with `context=[research_task]` |
| `context=[research_task]` | Passes the researcher's output to the analyst |
| Two agents in `Crew(agents=[...])` | Both run, in order |

## Your task

1. Set `TOPIC` to the same topic as previous steps.

2. Run it:
   ```bash
   uv run python src/exercises/step_04_multi_agent.py
   ```

3. Read both verbose logs — the researcher's and the analyst's. Note:
   - Does the analyst actually challenge anything the researcher found, or does it mostly repackage it?
   - What specifically in the analyst's backstory ("skeptical", "looks for what's missing") shows up in the output — and what doesn't?
   - Does the final analysis feel qualitatively different from what a single agent produced in step 3, or is it mostly the same content in two passes?

4. **Experiment**: remove `context=[research_task]` from `analysis_task` and run again. What happens to the analyst's output when it can no longer see the researcher's work?

5. Fill in the **Step 4** section of `EVALUATION.md`.

## Stretch goal

Add a third role — not for the sake of having three agents, but one whose absence you'd actually notice. Candidates: a critic who writes counterarguments, a translator who rewrites the output for a non-expert audience, or a validator who checks each claim against a known constraint. Run it and check whether the output meaningfully changes. If it doesn't, why not?
