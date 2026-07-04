"""
Step 2d — Few-Shot Prompting
-----------------------------
Provide the model with 2–3 examples of input→output pairs before asking
your real question. The model learns the expected format and style from
the examples — no training, no fine-tuning, just context.

This is "in-context learning": the examples are part of the prompt, not
part of the model weights.

Compare to step 1 (zero examples) and step 2a (structure, but no examples):
does showing the model what good output looks like change what it produces?

Run:
    uv run python src/exercises/step_02d_few_shot.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

os.makedirs("output", exist_ok=True)

# ── Examples — show the model what good output looks like ────────────────────
# Each pair is one "shot". Two examples = two-shot prompting.
example_1_input  = "TODO: a simpler or related input (not your main topic)"
example_1_output = "TODO: the ideal output for example 1 — this teaches format and style"

example_2_input  = "TODO: a second example input"
example_2_output = "TODO: ideal output for example 2"

# ── The actual question ───────────────────────────────────────────────────────
text = "TODO: same topic as previous steps"

# Assemble: examples first, real question last — the model completes the pattern
prompt = (
    f"Input: {example_1_input}\n"
    f"Output: {example_1_output}\n\n"
    f"Input: {example_2_input}\n"
    f"Output: {example_2_output}\n\n"
    f"Input: {text}\n"
    f"Output:"
)

response = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": prompt}],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02d.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2d — Few-Shot Prompting\n\n"
        f"**Topic:** {text}\n\n"
        f"## Prompt\n\n```\n{prompt}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
