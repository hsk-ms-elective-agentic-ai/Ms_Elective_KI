"""
Step 2 — Prompt Template
------------------------
Same model, same single API call — but now with a system prompt that defines a role
and enforces an output structure. No framework, just two messages.

The question: how much of the quality difference between step 1 and step 2 comes from
the model itself, and how much from what you tell it to be?

Run:
    uv run python src/exercises/step_02_prompt_template.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

TOPIC = "Artificial Intelligence in Healthcare"

SYSTEM_PROMPT = """You are a senior research analyst specializing in technology and business strategy.
Structure every response with these four sections:
## Overview
## Key Developments (3–5 bullet points)
## Practical Implications
## Open Questions"""

USER_PROMPT = f"""Research and summarize the following topic for a professional audience.
Be specific and include concrete examples where possible.

Topic: {TOPIC}"""

response = completion(
    model=os.getenv("MODEL", "groq/llama-3.3-70b-versatile"),
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
)

print(response.choices[0].message.content)
