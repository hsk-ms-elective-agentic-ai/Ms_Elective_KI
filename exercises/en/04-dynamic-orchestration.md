# Sprint 4 — Dynamic Orchestration (Hierarchical)

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/04-dynamic-orchestration.md)

Your sprint 1 MVP already has multiple agents — but you decided the order yourself, in `tasks.yaml`, before anything ran. That's still a fixed pipeline, just one with more than one agent in it. This sprint is about something genuinely different: a **manager agent decides at runtime** which worker agent handles each task, and in what order, instead of you hardcoding the sequence. That's the actual "multi-agent" pattern — collaboration that's dynamic, not just plural.

Tradeoff: more flexible, but less predictable and more expensive (the manager makes extra LLM calls to delegate).

> Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

![AutoGen architecture: conversable, customizable agents that converse to solve tasks, in joint chat or hierarchical chat patterns, shown solving a data-plotting task through multi-turn conversation](../assets/autogen-wu2023-fig1.png)
*Figure 1 from Wu et al. (2023): AutoGen agents are conversable and customizable, can converse in patterns including hierarchical chat, and can include humans in the loop. Reproduced for educational use in this course.*

## In this repo

Currently `process=Process.sequential` with agents in a fixed order ([crew.py:51](../../src/research_crew/crew.py#L51)). To go hierarchical, CrewAI requires either `manager_llm` or `manager_agent`:

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.hierarchical,
    manager_llm="groq/llama-3.3-70b-versatile",
    verbose=True,
)
```

In hierarchical mode, you also remove the fixed `agent:` field from each task in `tasks.yaml` — the manager assigns tasks to agents dynamically rather than reading a hardcoded assignment.

## Your task

1. **Sprint planning**: open 1–2 GitHub Issues as user stories labeled `epic:orchestration`, for the new agent's role and for the process-choice decision itself.
2. Add a third agent to your crew — a role that's genuinely missing from your first two, not one invented just to have three.
3. **Decide deliberately**: does your use case actually benefit from a manager dynamically delegating, or would a third agent in a fixed sequential slot serve just as well? Try the one you don't expect to win first, so you're not just confirming what you already assumed.
4. If you go hierarchical: switch `process`, add `manager_llm`, and strip the fixed `agent:` assignments from `tasks.yaml`. Run it and watch the verbose logs — which agent does the manager pick for each task, and does it match what you'd expect from each agent's role?
5. Update `DESIGN.md`'s Architecture section (Process, Agents) and Guardrails/trust mechanisms if you added any validation.
6. Before calling this done, answer in `DESIGN.md`: if you went hierarchical, what is the manager actually optimizing for when it delegates, and could that diverge from what you want? If you stayed sequential, what would hierarchical have bought you, and why wasn't it worth the cost? What does the third agent add that the first two couldn't already do between them — is its role truly necessary, or just splitting work that didn't need splitting?

## Stretch goal

If you went hierarchical with `manager_llm`, try `manager_agent` instead — define your own dedicated manager `Agent` with an explicit role, and compare whether the delegation decisions change.
