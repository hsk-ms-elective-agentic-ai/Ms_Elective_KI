# Sprint 0 — Vision & Architecture

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/00-vision-architecture.md)

An agentic *framework* gives you reusable building blocks so you don't hand-roll the think-act-observe loop yourself. CrewAI's four core abstractions:

- **Agent** — role, goal, backstory, LLM, tools
- **Task** — a description, expected output, and which agent is assigned to it
- **Crew** — a collection of agents + tasks + a process for running them
- **Process** — the orchestration strategy (sprints 1 and 4 cover the two main ones)

This split is one concrete implementation of a more general pattern from the LLM-agent literature:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Unified framework for the architecture design of LLM-based autonomous agents: Profile, Memory, Planning, Action modules](../assets/agentsurvey-wang2023-fig2.png)
*Figure 2 from Wang et al. (2023): a unified LLM-agent architecture of Profile, Memory, Planning, and Action modules. Reproduced for educational use in this course.*

Mapped onto CrewAI: an `Agent`'s `role`/`goal`/`backstory` in `agents.yaml` is the **Profile** module; `tools` plus the task loop is the **Action** module.

Before any of that, though, the actual hard part is deciding *who* this crew is for and *what* it should do — which is a design problem, not a coding problem. Two grounding references for that part:

> Simon, H. A. (1969). *The Sciences of the Artificial*. MIT Press.

> Brown, T. (2008). *Design Thinking*. Harvard Business Review, 86(6), 84–92.

## In this repo

Open [src/research_crew/crew.py](../../src/research_crew/crew.py) top to bottom — it's short on purpose. Map each part to the concept:

| Concept | Where |
| --- | --- |
| `@CrewBase` class | [crew.py:10](../../src/research_crew/crew.py#L10) — marks `ResearchCrew` as a CrewAI project, auto-loads the YAML configs |
| Agents | `researcher` and `analyst` methods, each decorated `@agent` |
| Tasks | `research_task` and `analysis_task`, each decorated `@task` |
| Crew | the `crew()` method, decorated `@crew`, assembles everything |
| Config-driven roles | [config/agents.yaml](../../src/research_crew/config/agents.yaml) — role/goal/backstory live in YAML, not Python |
| Config-driven tasks | [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) — description/expected_output/agent assignment |

Notice the demo's own goal was never written down anywhere explicit — `researcher` and `analyst` exist because that split is generically useful for "research a topic, then report on it," not because anyone empathized with a specific stakeholder first. That's the gap this sprint asks you to not repeat.

## Your task

This is where you pick your use case (see the [table in the main README](../../README.md#use-cases-to-pick-from)) and start designing your own crew — not the `researcher`/`analyst` pair relabeled.

1. **Sprint planning**: open 2–3 GitHub Issues as user stories (format in [Assignment Templates](assignment-templates.md)), labeled `epic:vision`.
2. **Who is this for?** Name the actual stakeholder of your crew's output — not "users" in the abstract, a specific role or person. What do *they* need from it, and what would make the output useless to them even if it's technically correct?
3. **What's the problem, in their words?** Write one or two sentences stating the goal from that stakeholder's perspective, not from the technology's perspective. This goes in `DESIGN.md`'s Overview section.
4. **Before settling on one design, sketch at least two different agent role-splits** for your use case — not just the suggestion in the README's use-case table. Write down what each version would look like (how many agents, what each owns) before picking one.
5. **Design the agents and tasks** for the version you're going with: roles, goals, backstories, and how tasks depend on each other. Fill in `DESIGN.md`'s Architecture section (Agents and Tasks tables).
6. Before calling this done, answer directly in `DESIGN.md`: what does each agent actually need from the other to do its job — and what happens if one agent's output is subtly wrong, does the next agent have any way to notice, or does it trust it blindly? What's the strongest reason the role-split you *rejected* in step 4 might actually have been better? How would you know if your current split was wrong, rather than just different from someone else's?

## Stretch goal

Find someone outside your team (a classmate, a friend) who plausibly resembles your chosen stakeholder, and ask them one question: "would you actually use a report this crew produces?" Write down their answer, unfiltered, in `DESIGN.md` — even if it's not what you wanted to hear.
