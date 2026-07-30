# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](de/README.md)

These are the hands-on steps for **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**. Lecture theory is delivered via slides in class; this series is the practice companion — and it's also the graded team assignment, not a separate thing alongside it.

The premise is simple: you'll run a sequence of versions of the same thing on the same topic, with each version adding one layer. Then you evaluate what each layer actually changed. The learning comes from the comparison, not from any single step.

You should have [Run the crew](../README.md#run-the-crew) working in **your team's own repo** before Step 02 — see the main [README's "Getting access"](../README.md#getting-access-students) section if you don't have that yet. If Git, `uv`, or Jupyter are new to you, start with Step 00 first.

## Steps

| # | Title | What it adds |
| --- | --- | --- |
| [00](en/step_00_setup_and_python_basics.ipynb) | Setup & Python Basics | Git/GitHub, `uv`, and Jupyter *(optional, if any of this is new to you)* |
| [01](en/step_01_test_setup_and_first_llm_call.ipynb) | Test Your Setup & First LLM Call | Verify your environment works, tour the project, make your first `crewai.LLM` call *(optional)* |
| [02](en/step_02_zero_shot_prompting.ipynb) | Zero-Shot Prompting | The bare API call — your baseline |
| [03](en/step_03_few_shot.ipynb) | Few-Shot Prompting | 2–3 examples before the real question |
| [04](en/step_04_prompt_template.ipynb) | Prompt Template | A role + output structure, same call |
| [05](en/step_05_chain_prompting.ipynb) | Chain Prompting | Two sequential calls, one feeding the next |
| [06](en/step_06_chain_of_thought.ipynb) | Chain of Thought | Explicit reasoning before the final answer |
| [07](en/step_07_tree_of_thought.ipynb) | Tree of Thought | Several reasoning paths explored in parallel |
| [08](en/step_08_intro_to_crewai.ipynb) | Introduction to CrewAI | What CrewAI is, `Agent`/`Task`/`Crew`/`Process`, and built-in memory — built up from a plain LLM call |
| [09](en/step_09_single_agent.ipynb) | Single Agent | A standalone `Agent`, no framework project needed *(Interim Presentation)* |
| [10](en/step_10_memory.ipynb) | Memory | Recall across separate `kickoff()` calls |
| [11](en/step_11_tools.ipynb) | Tools | Live web search via a CrewAI tool |
| [12](en/step_12_mcp.ipynb) | MCP | An external tool server via Model Context Protocol |
| [13](en/step_13_rag.ipynb) | RAG | Retrieval from your own knowledge source |
| [14](en/step_14_multi_agent_seq.ipynb) | Multi-Agent (Sequential) | Two agents, chained by passing one's output into the next *(Final Presentation)* |
| [15](en/step_15_multi_agent_hierarchical.ipynb) | Multi-Agent (Hierarchical) | The same two agents, delegated to at runtime by a manager instead of fixed in code *(optional)* |
| [16](en/step_16_design_patterns.ipynb) | Agentic Workflow Design Patterns | Anthropic's five workflow patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), each mapped to a working CrewAI mechanism *(optional)* |
| [17](en/step_17_evaluation_harness.ipynb) | Evaluating Speed, Accuracy & Cost | A reusable harness measuring latency, token cost, and an LLM-judged Goal Completion Rate — feeds `REPORT.md` Section 5.2 *(optional)* |

Steps 02–14 use the **same topic** — you pick it once at step 02 and keep it. These notebooks are individual practice, not a team submission; `REPORT.md` is where your team then captures the design of the agent you build together — architecture, implementation, evaluation — as prep for your Interim and Final Presentations. Each student separately writes and submits their own Ethics Report. Steps 15–17 are optional and not part of the graded assignment.

For what's graded, the submission package, team setup, and templates (`REPORT.md`, `TEAM.md`, Ethics Report), see [Assignment Overview](../team_assignment/en/assignment-overview.md) (English / [Deutsch](../team_assignment/de/assignment-overview.md)).

## Learn more on your own

Each step's "Background" section gives you just enough to place the concept — for everything CrewAI itself can do beyond what this repo's demo crew demonstrates, go straight to the source:
- [CrewAI documentation](https://docs.crewai.com) — the full concept reference (agents, tasks, processes, tools, memory, knowledge, flows) and the [quickstart](https://docs.crewai.com/en/quickstart)
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) (DeepLearning.AI) — a short video course taught by CrewAI's founder; free during DeepLearning.AI's platform beta, may not stay free indefinitely

## For instructors

Students work in their own team's repo (one per team, provisioned from this template under your course organization) — see the main [README's "Getting access"](../README.md#getting-access-students) for the student-facing enrollment flow, and the "For instructors" section in the [Assignment Overview](../team_assignment/en/assignment-overview.md#for-instructors) for the full org/team/repo provisioning and the automated sign-up workflow. Solutions aren't included on purpose; review submissions by checking each team's merged sprint pull requests directly.
