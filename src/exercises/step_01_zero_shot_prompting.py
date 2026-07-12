"""
Step 1 — Zero-Shot Prompting
-----------------------------
One API call, one message, one response. No role, no structure, no framework,
no examples. The model answers from training data alone — this is the baseline.

Run:
    uv run python src/exercises/step_01_zero_shot_prompting.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

os.makedirs("output", exist_ok=True)

# Change this to your team's topic. Keep it the same across all 5 steps.
TOPIC = "Explain the EU AI Act in simple terms for a 10-year-old in a short paragraph."

# ── Zero-shot uses only "user" — no system persona, no assistant turns ───────
user_message = "Explain the EU AI Act in simple terms for a 10-year-old in a short paragraph."

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[{"role": "user", "content": user_message}],
)

output = response.choices[0].message.content
print(output)

with open("output/step_01.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 1 — Zero-Shot Prompting\n\n"
        f"**Topic:** {TOPIC}\n\n"
        f"## Prompt\n\n```\n{user_message}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
