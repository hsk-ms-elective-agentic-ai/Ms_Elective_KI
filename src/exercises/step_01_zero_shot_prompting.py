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
TOPIC = "TODO: your topic here"

# ── Roles — zero-shot uses only "user"; system and assistant stay empty ──────
system_message    = ""  # no persona, no rules — nothing to steer the model
user_message      = "TODO: write your question about the topic"
assistant_message = ""  # no prior turns, no examples

messages = [
    {"role": role, "content": content}
    for role, content in [
        ("system", system_message),
        ("user", user_message),
        ("assistant", assistant_message),
    ]
    if content
]

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=messages,
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
