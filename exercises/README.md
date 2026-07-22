# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](de/README.md)

These are the hands-on steps for **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**. Lecture theory is delivered via slides in class; this series is the practice companion — and it's also the graded team assignment, not a separate thing alongside it.

The premise is simple: you'll run a sequence of versions of the same thing on the same topic, with each version adding one layer. Then you evaluate what each layer actually changed. The learning comes from the comparison, not from any single step.

You should have [Run the crew](../README.md#run-the-crew) working in **your team's own repo** before Step 03 — see the main [README's "Getting access"](../README.md#getting-access-students) section if you don't have that yet. If Git, `uv`, Jupyter, or Python itself are new to you, start with Step 00 first.

## Steps

| # | Title | What it adds |
| --- | --- | --- |
| [00](en/step_00_setup_and_python_basics.ipynb) | Setup & Python Basics | Git/GitHub, `uv`, Jupyter, and a Python refresher *(optional, if any of this is new to you)* |
| [01](en/step_01_test_setup_and_first_agent.ipynb) | Test Your Setup & First Agent | Verify your environment works, tour the project, meet a standalone `Agent` *(optional)* |
| [02](en/step_02_intro_to_crewai.ipynb) | Introduction to CrewAI | What CrewAI is, `Agent`/`Task`/`Crew`/`Process`, and built-in memory — built up from a plain LLM call *(optional)* |
| [03](en/step_03_zero_shot_prompting.ipynb) | Zero-Shot Prompting | The bare API call — your baseline |
| [04](en/step_04_few_shot.ipynb) | Few-Shot Prompting | 2–3 examples before the real question |
| [05](en/step_05_prompt_template.ipynb) | Prompt Template | A role + output structure, same call |
| [06](en/step_06_chain_prompting.ipynb) | Chain Prompting | Two sequential calls, one feeding the next |
| [07](en/step_07_chain_of_thought.ipynb) | Chain of Thought | Explicit reasoning before the final answer |
| [08](en/step_08_tree_of_thought.ipynb) | Tree of Thought | Several reasoning paths explored in parallel |
| [09](en/step_09_single_agent.ipynb) | Single Agent | A standalone `Agent`, no framework project needed *(interim submission due)* |
| [10](en/step_10_tools.ipynb) | Tools | Live web search via a CrewAI tool |
| [11](en/step_11_mcp.ipynb) | MCP | An external tool server via Model Context Protocol |
| [12](en/step_12_rag.ipynb) | RAG | Retrieval from your own knowledge source |
| [13](en/step_13_multi_agent.ipynb) | Multi-Agent | Two agents, chained by passing one's output into the next *(final submission due)* |

Steps 03–13 use the **same topic** — you pick it once at step 03 and keep it. The primary deliverable is `EVALUATION.md`: a full project report — architecture, implementation, evaluation, ethics — on the agent your team designs and builds, informed by what changed at each step.

For what's graded, the submission package, team setup, and templates (`EVALUATION.md`, `TEAM.md`, peer evaluation), see [Assignment Overview](../team_assignment/en/assignment-overview.md) (English / [Deutsch](../team_assignment/de/assignment-overview.md)).

## Learn more on your own

Each step's "Background" section gives you just enough to place the concept — for everything CrewAI itself can do beyond what this repo's demo crew demonstrates, go straight to the source:
- [CrewAI documentation](https://docs.crewai.com) — the full concept reference (agents, tasks, processes, tools, memory, knowledge, flows) and the [quickstart](https://docs.crewai.com/en/quickstart)
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) (DeepLearning.AI) — a short video course taught by CrewAI's founder; free during DeepLearning.AI's platform beta, may not stay free indefinitely

## For instructors

Students work in their own team's repo (one per team, provisioned from this template under your course organization) — see the main [README's "Getting access"](../README.md#getting-access-students) for the student-facing enrollment flow, and the "For instructors" section in the [Assignment Overview](../team_assignment/en/assignment-overview.md#for-instructors) for the full org/team/repo provisioning and the automated sign-up workflow. Solutions aren't included on purpose; review submissions by checking each team's merged sprint pull requests directly.
