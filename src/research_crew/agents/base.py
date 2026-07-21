import os
from contextlib import contextmanager

from crewai import Agent, Crew, Process, Task


@contextmanager
def _no_model_env_collision():
    """crewai's Gemini embedder config reads a `model` alias that collides
    case-insensitively with this repo's own MODEL env var (used to pick the chat
    LLM, e.g. "gemini/gemini-3.1-flash-lite") - unrelated to the embedding model
    you actually want. Unsetting MODEL only for the instant Crew() validates the
    embedder avoids a spurious ValidationError.
    """
    saved = os.environ.pop("MODEL", None)
    try:
        yield
    finally:
        if saved is not None:
            os.environ["MODEL"] = saved


class BaseAgent:
    """One CrewAI `Agent`, re-wrapped in a fresh single-task `Crew` on every `run()` call.

    Subclasses set `self.role` / `self.goal` / `self.backstory` before calling
    `super().__init__()`, and may override `task_description()` to change how a
    user message becomes the `Task`'s description.

    Pass `memory=True` (plus an `embedder` config if you're not relying on
    `OPENAI_API_KEY`'s default) to let CrewAI's own short-term memory carry
    context across separate `run()` calls - see Step 0c for what that buys you.
    """

    def __init__(self, llm=None, memory: bool = False, embedder: dict | None = None):
        self.llm = llm
        self.memory = memory
        self.embedder = embedder
        self.agent = Agent(role=self.role, goal=self.goal, backstory=self.backstory, llm=self.llm)
        self.last_crew: Crew | None = None

    def task_description(self, message: str) -> str:
        return message

    def _build_crew(self, message: str) -> Crew:
        task = Task(
            description=self.task_description(message),
            expected_output="A direct, conversational reply to the user's message.",
            agent=self.agent,
        )
        if self.memory and self.embedder:
            with _no_model_env_collision():
                return Crew(
                    agents=[self.agent],
                    tasks=[task],
                    process=Process.sequential,
                    memory=True,
                    embedder=self.embedder,
                )
        return Crew(
            agents=[self.agent],
            tasks=[task],
            process=Process.sequential,
            memory=self.memory,
        )

    def run(self, message: str):
        self.last_crew = self._build_crew(message)
        return self.last_crew.kickoff()

    def reset_memory(self) -> None:
        """Clear this agent's short/long/entity memory. Requires `run()` to have been called at least once with `memory=True`."""
        if self.last_crew is None:
            raise RuntimeError("Call run() at least once before resetting memory.")
        self.last_crew.reset_memories("all")
