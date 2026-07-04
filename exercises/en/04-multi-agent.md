# Step 4 — Multi-Agent

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/04-multi-agent.md)

Add a second agent with a different, complementary role. The first agent's output is passed to the second via `context:` in `tasks.yaml`. This is multi-agent in the simplest sense: role specialization with task chaining, not dynamic delegation.

## Background

A single agent can do multiple things, but it can't hold two genuinely different epistemic roles at the same time — it can't be simultaneously credulous (collecting everything) and skeptical (questioning what it found). Two agents let you encode that tension into the architecture. The seminal demonstration of agents collaborating through conversation was:

> Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

![AutoGen: conversable agents solving tasks in joint or hierarchical patterns](../assets/autogen-wu2023-fig1.png)
*Figure 1 from Wu et al. (2023). Reproduced for educational use in this course.*

## In this repo

| File | What to change |
| --- | --- |
| [src/research_crew/config/agents.yaml](../../src/research_crew/config/agents.yaml) | Add a second agent with a role that complements the first |
| [src/research_crew/config/tasks.yaml](../../src/research_crew/config/tasks.yaml) | Add a second task; link it to the first with `context:` |
| [src/research_crew/crew.py](../../src/research_crew/crew.py) | Add a second `@agent` and `@task` method |

The `context:` field in `tasks.yaml` is how the second agent receives the first agent's output:

```yaml
second_task:
  description: ...
  expected_output: ...
  agent: agent_2
  context:
    - first_task
```

## Your task

1. In `agents.yaml`, add a second agent with a role that's genuinely different from the first — not the same job with a different label.

2. In `tasks.yaml`, add a second task assigned to that agent. Add `context: - first_task` so it receives the first agent's output.

3. In `crew.py`, add a second `@agent` method and a second `@task` method.

4. Run:
   ```bash
   uv run research_crew
   ```

5. Read both agents' verbose output. Does the second agent actually build on or push back against the first, or does it mostly repackage the same content? Does the final output feel qualitatively different from step 3?

6. **Experiment**: remove the `context:` line from the second task and run again. What happens to the second agent's output when it can no longer see the first agent's work?

7. Fill in the **Step 4** section of `EVALUATION.md`.

## Stretch goal

Add a third agent whose absence you'd actually notice — a critic, a translator for a non-expert audience, or a validator. Run it and check whether the output meaningfully changes. If it doesn't, ask yourself why.
