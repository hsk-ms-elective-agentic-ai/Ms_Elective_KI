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

os.makedirs("output", exist_ok=True)

# Change this to your team's topic. Keep it the same across all 5 steps.
TOPIC = "EU AI Act compliance requirements for a B2B SaaS company that uses LLMs in its product"

message = TOPIC

response = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": message}],
)

output = response.choices[0].message.content
print(output)

with open("output/step_01.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 1 — Simple Prompting\n\n"
        f"**Topic:** {TOPIC}\n\n"
        f"## Prompt\n\n```\n{message}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
