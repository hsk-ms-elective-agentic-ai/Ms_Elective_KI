"""
Step 2f — Structured Output (JSON Mode)
------------------------------------------------
Ask the model to return machine-readable JSON instead of free-form prose, using
the `response_format` parameter. This doesn't replace prompting — you still
have to describe the exact shape you want in the prompt itself — but it
constrains the model to emit valid JSON syntax, so your code can parse the
result directly instead of scraping a paragraph.

Compare to step 2b: same persona/instruction/audience pattern, but the output
is now something a program can index into (e.g. result["risk_tier"]) instead
of something only a human can read.

Run:
    uv run python src/exercises/step_02f_structured_output.py
"""
import json
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()
os.makedirs("output", exist_ok=True)

# ── System message — response_format only enforces valid JSON syntax; you
# still have to describe the exact shape you want in the prompt itself ───────
json_shape = 'TODO: describe the shape, e.g. {"field_1": string, "field_2": string[], "field_3": number}'
system_message = f"TODO: who is the model?\nRespond only with JSON matching this shape: {json_shape}"

# ── User message — the actual question ───────────────────────────────────────
user_message = "TODO: your question here"

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
    response_format={"type": "json_object"},
)

output = response.choices[0].message.content
parsed = json.loads(output)  # fails loudly if the model didn't return valid JSON

print(json.dumps(parsed, indent=2))

with open("output/step_02f.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2f — Structured Output (JSON Mode)\n\n"
        f"## System message\n\n```\n{system_message}\n```\n\n"
        f"## User message\n\n```\n{user_message}\n```\n\n"
        f"## Output (parsed JSON)\n\n```json\n{json.dumps(parsed, indent=2)}\n```\n"
    )
