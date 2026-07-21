from research_crew.agents.base import BaseAgent


class SimpleAgent(BaseAgent):
    """A ready-to-use conversational agent: give it a name and a system prompt."""

    def __init__(self, name: str, system_prompt: str, llm=None, **kwargs):
        self.name = name
        self.role = name
        self.goal = "Have a helpful, natural conversation with the user"
        self.backstory = system_prompt
        super().__init__(llm=llm, **kwargs)
