# Step 3 — Single Agent

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/03-single-agent.md)

Wrap the prompt in a CrewAI `Agent` and `Task`. The `role`, `goal`, and `backstory` are still just a system prompt under the hood — CrewAI assembles it for you from those three fields — and a `Task` is still just a user-side instruction. What the framework adds is the loop: the agent can reason in multiple steps before producing output, call tools (step 5), and retry on failure. One agent, one task.

## Background

The observation that LLM-based agents benefit from an explicit module structure — profile (who this agent is), memory (what it has access to), planning (how it breaks down work), and action (what it can do) — was systematized in:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Unified framework for the architecture design of LLM-based autonomous agents: Profile, Memory, Planning, Action modules](../assets/agentsurvey-wang2023-fig2.png)
*Figure 2 from Wang et al. (2023): a unified LLM-agent architecture. Reproduced for educational use in this course.*

In CrewAI terms: `role`/`goal`/`backstory` in `agents.yaml` map to **Profile**; `tools` plus the task loop map to **Action**. Planning and Memory are present but implicit at this step (single-turn reasoning, no persistent memory yet).

## The code

Open [src/exercises/step_03_single_agent.py](../../src/exercises/step_03_single_agent.py). Map each piece to the concepts above:

| Code | What it is |
| --- | --- |
| `Agent(role=..., goal=..., backstory=...)` | The Profile module — assembled into a system prompt by CrewAI |
| `Task(description=..., expected_output=...)` | The assignment the agent works on |
| `Crew(agents=[...], tasks=[...])` | The runtime that runs the loop |
| `verbose=True` | Shows the agent's internal reasoning — read this, it's the point |

## Your task

1. Set `TOPIC` to the same topic as steps 1 and 2.

2. Run it:
   ```bash
   uv run python src/exercises/step_03_single_agent.py
   ```

3. Watch the verbose output carefully — this is the first step where you can see the model's *internal reasoning*, not just its final answer. Note:
   - Does the agent break the task into sub-steps?
   - Does the final answer look different from what step 2 produced? In what specific way?

4. **Experiment**: change `backstory` to something minimal (one sentence) vs. rich (three sentences with concrete specialization). Does backstory depth change the output quality, or does the model mostly use `role` and `goal`?

5. Fill in the **Step 3** section of `EVALUATION.md`.

## Stretch goal

Look at the verbose log's "Final Answer" alongside the agent's intermediate thinking. Find one place where the agent's reasoning and its conclusion seem inconsistent — where it reasons toward one thing and writes something slightly different. What does this tell you about trusting the chain-of-thought?

---

**→ Interim submission is due after this step.** Submit the state of `main` after merging `sprint-3`. See [Assignment Overview](assignment-overview.md) for exactly what's expected.
