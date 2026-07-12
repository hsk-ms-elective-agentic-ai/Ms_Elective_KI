"""
Step 2b — Prompt Template
-------------------------
Same question as step 1, but the prompt is split into two roles:
- "system": tells the model who it is and how to behave (persona, rules, format)
- "user":   the actual question — what you want answered

The system message is invisible to the end user but shapes every response.
Try removing individual components to see what each one actually does.

Run:
    uv run python src/exercises/step_02b_prompt_template.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

os.makedirs("output", exist_ok=True)

# ── System message — who the model is and how it should behave ───────────────
# These components are sent as background instructions, not as a question.
persona       = "TODO: who is the model?\n"
instruction   = "TODO: what should it do?\n"
context       = "TODO: what background does it need to do it well?\n"
data_format   = "TODO: what should the output look like?\n"
audience      = "TODO: who will read the output?\n"
tone          = "TODO: what tone should it use?\n"

system_message = persona + instruction + context + data_format + audience + tone

# ── User message — the actual question ───────────────────────────────────────
user_message = "TODO: your topic here"

assistant_message = ""

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": assistant_message},
    ],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02b.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2b — Prompt Template\n\n"
        f"**Topic:** {user_message}\n\n"
        f"## System message\n\n```\n{system_message.strip()}\n```\n\n"
        f"## User message\n\n```\n{user_message}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
