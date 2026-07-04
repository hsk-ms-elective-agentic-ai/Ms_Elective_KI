"""
Step 1 — Simple Prompting
-------------------------
One API call, one message, one response. No role, no structure, no framework.

Run:
    uv run python src/exercises/step_01_simple_prompting.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# Change this to your team's topic. Keep it the same across all 5 steps.
TOPIC = "TODO: your topic here"

response = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[
        {"role": "user", "content": "TODO: write your question about the topic"},
    ],
)

print(response.choices[0].message.content)
