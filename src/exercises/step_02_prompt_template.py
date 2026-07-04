"""
Step 2 — Prompt Template
------------------------
Same API call as step 1, but now with a system prompt that defines a role
and a user prompt with a specific structure.

Compare the output to step 1: what changed, and why?

Run:
    uv run python src/exercises/step_02_prompt_template.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

TOPIC = "TODO: same topic as step 1"

SYSTEM_PROMPT = """TODO: write a system prompt that gives the model a role
and specifies the structure of the output"""

USER_PROMPT = f"""TODO: write a user message for the topic: {TOPIC}"""

response = completion(
    model=os.getenv("MODEL", "groq/llama-3.3-70b-versatile"),
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
)

print(response.choices[0].message.content)
