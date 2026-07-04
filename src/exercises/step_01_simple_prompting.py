"""
Step 1 — Simple Prompting
-------------------------
The simplest possible LLM interaction: one API call, one message, plain text back.
No role definition, no output structure, no framework — just the model.

This is the baseline for the whole exercise series. Run it first, observe the output,
then compare against each subsequent step using the same topic.

Run:
    uv run python src/exercises/step_01_simple_prompting.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# ── Change this to your team's topic. Keep it identical across all 5 steps. ──
TOPIC = "Artificial Intelligence in Healthcare"

response = completion(
    model=os.getenv("MODEL", "groq/llama-3.3-70b-versatile"),
    messages=[
        {"role": "user", "content": f"Write a short research summary about: {TOPIC}"}
    ],
)

print(response.choices[0].message.content)
