# Sprint 1 — First Runnable MVP

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/01-first-mvp.md)

A prototype's job is to teach you something, not to be polished — the fastest way to find out whether your Sprint 0 design actually works is to run it, not to keep refining it on paper. CrewAI gives you two ways to wire up the order tasks run in:

- **`Process.sequential`** — agent A finishes completely, then hands its output to agent B. The right default when steps genuinely depend on each other in order.
- **Parallel tasks within a sequential crew** — set `async_execution: true` on a `Task` and it runs in a background thread instead of blocking; a later task that depends on it (via `context`) still waits for it, but tasks that *don't* depend on each other can run concurrently instead of one after another.

The underlying agent architectures these build on come from the classic taxonomy in:

> Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 2: Intelligent Agents. Pearson.

No figure here — it's a book, not an openly licensed paper, so we cite rather than reproduce its diagrams.

## In this repo

[crew.py:48-60](../../src/research_crew/crew.py#L48-L60):

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
    ...
)
```

`Process.sequential` means: run `research_task` to completion (the `researcher` agent works alone), then run `analysis_task` (the `analyst` agent works alone, but receives the research output via `context: - research_task` in [tasks.yaml](../../src/research_crew/config/tasks.yaml)). Two agents, fixed order, zero negotiation — the simplest possible pipeline, and *not yet* the dynamic, manager-delegated kind of multi-agent collaboration (that's sprint 4).

If two of your tasks turn out not to depend on each other at all, marking one `async_execution: true` in `tasks.yaml` would let it run while another task is still going, instead of waiting its turn for no reason:

```yaml
research_task:
  description: ...
  async_execution: true
```

## Your task

1. **Sprint planning**: open 2–3 GitHub Issues as user stories labeled `epic:mvp`, covering "the crew runs end to end and produces real output."
2. Implement the agents and tasks you designed in Sprint 0 for real, in `agents.yaml` and `tasks.yaml`.
3. For each pair of tasks, decide: does one genuinely need the other's output first? If not, consider `async_execution: true`. If you're not sure, default to sequential — it's the safer, more predictable choice, and parallelism you don't need is just complexity.
4. Run it: `uv run research_crew`. Confirm `output/report.md` (or your own output) actually reflects your specific use case, not a generic answer that could have come from any topic.
5. Update `DESIGN.md`'s Architecture section to match what you actually built (not just what you planned in Sprint 0 — if it changed, that's fine, just record the real version).
6. Before calling this done, answer in `DESIGN.md`: why sequential (or async) for each task pair specifically, not the other way around? If your real use case had to handle ten times the volume, what's the first thing that would break? Right now your crew runs without errors — how would you actually check it's doing something *useful* for your stakeholder, not just technically functioning?

## Stretch goal

Deliberately break something — rename a YAML key, remove a `context` dependency, or feed it a deliberately bad input — and see whether the failure mode is obvious or silent. A crew that fails loudly is easier to debug than one that quietly produces a plausible-looking wrong answer.

---

**This is also your interim checkpoint of sorts** — by the end of this sprint, your team should have a working baseline you can keep extending, not a paper design you haven't tested yet.
