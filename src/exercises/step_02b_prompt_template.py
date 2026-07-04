"""
Step 2b — Prompt Template
-------------------------
Same API call as step 1, but the prompt is broken into named components.
Each component shapes a different aspect of the output.

Try removing individual components from query to see what each one actually does.

Run:
    uv run python src/exercises/step_02b_prompt_template.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# ── Prompt components — fill in each one, then try removing some ──────────────
persona       = "You are a helpful assistant.\n"
instruction   = "You are an expert in EU AI Act compliance.\n"
context       = "You are assisting a B2B SaaS company that uses LLMs in its product.\n"
data_format   = "Provide your response in bullet points.\n"
audience      = "The output will be read by legal professionals and compliance officers.\n"
tone          = "Be professional and concise.\n"

text          = "EU AI Act compliance requirements for a B2B SaaS company that uses LLMs in its product"
data          = f"Topic: {text}\n"

# The full prompt — remove and add components to observe the impact
query = persona + instruction + context + data_format + audience + tone + data

os.makedirs("output", exist_ok=True)

response = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": query}],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02b.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2b — Prompt Template\n\n"
        f"**Topic:** {text}\n\n"
        f"## Prompt\n\n```\n{query}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
