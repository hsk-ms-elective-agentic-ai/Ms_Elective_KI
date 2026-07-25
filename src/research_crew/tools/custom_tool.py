# Template for a custom CrewAI tool — not imported by crew.py yet. Rename the
# class, fill in `name`/`description` (the agent reads these to decide when to
# call it — see Step 10 for how `SerperDevTool` does the same), and implement
# `_run`. To wire it in, import the class in crew.py and add it to an agent's
# `tools=[...]` list, the same way `researcher` already gets `SerperDevTool()`.

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
