# Sprint 2 — Tools

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/02-tools.md)

Tools turn an LLM from "generates plausible text" into "can actually do things": search the web, query a database, call an internal API, run code. The agent decides *when* and *with what arguments* to call a tool — you just need to describe the tool clearly enough that the LLM can use it correctly. Every CrewAI tool needs a **name** and **description** (what the agent reads to decide whether/how to use it — vague descriptions cause misuse), an **input schema** (a Pydantic model), and a `_run()` method with the actual implementation.

The idea that a language model can learn *when* to call a tool, *which* tool, and *what arguments* to pass — rather than a human hardcoding when tools fire — was demonstrated in:

> Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

![Toolformer examples: the model inserts API calls for a QA system, a calculator, a translation system, and a Wikipedia search engine into its own generated text](../assets/toolformer-schick2023-fig1.png)
*Figure 1 from Schick et al. (2023): Toolformer autonomously deciding to call APIs to obtain information it needs. Reproduced for educational use in this course.*

## In this repo

[src/research_crew/tools/custom_tool.py](../../src/research_crew/tools/custom_tool.py) is a template, not wired into the crew yet:

```python
class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        return "this is an example of a tool output, ignore it and move along."
```

Compare it to the tool already in use, [crew.py:22](../../src/research_crew/crew.py#L22): `SerperDevTool()` — a fully pre-built tool from `crewai_tools`, requiring zero implementation, just an API key (`SERPER_API_KEY`). The README's [tool category table](../../README.md#adding-more-tools-or-rag-for-students) lists ~90 pre-built tools split by whether they need just an API key or local embeddings (that's sprint 3).

## Your task

1. **Sprint planning**: open 1–2 GitHub Issues as user stories labeled `epic:tools`, with acceptance criteria covering both the happy path and a failure case (rate limit, empty result, API down).
2. Pick a tool your use case **actually needs** — not one to check a box. Either a pre-built one from the README's table, or a custom one following `custom_tool.py`'s pattern if nothing existing fits.
3. Wire it into the relevant agent in `crew.py` (`tools=[...]`) and write a task description that should make the agent want to use it.
4. Run it and confirm the agent actually calls the tool — check the verbose logs, don't just assume.
5. Update `DESIGN.md`'s Tools table.
6. Before calling this done, answer in `DESIGN.md`: what happens if this tool is rate-limited, returns nothing useful, or the API is down mid-run — does your crew degrade gracefully or just fail? Does the tool's description make misuse likely (wrong arguments, or not calling it when it should)? Now that you have a tool, what's actually better than your Sprint 1 MVP, specifically — and how would you show that to your stakeholder, not just claim it?

## Stretch goal

Swap your tool for a different one solving the same problem (e.g. a different search provider) and compare: same task, same agent, different tool — does the agent's behavior or output quality change, and why might that be?
