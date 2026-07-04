"""
Step 2a — Prompt Template
-------------------------
Same API call as step 1, but the prompt is broken into named components.
Each component shapes a different aspect of the output.

Try removing individual components from query to see what each one actually does.

Run:
    uv run python src/exercises/step_02a_prompt_template.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# ── Prompt components — fill in each one, then try removing some ──────────────
persona       = "TODO: who is the model?\n"
instruction   = "TODO: what should it do?\n"
context       = "TODO: what background does it need to do it well?\n"
data_format   = "TODO: what should the output look like?\n"
audience      = "TODO: who will read the output?\n"
tone          = "TODO: what tone should it use?\n"

text          = "TODO: your topic or text here"
data          = f"Topic: {text}\n"

# The full prompt — remove and add components to observe the impact
query = persona + instruction + context + data_format + audience + tone + data

response = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[
        {"role": "user", "content": query},
    ],
)

print(response.choices[0].message.content)
