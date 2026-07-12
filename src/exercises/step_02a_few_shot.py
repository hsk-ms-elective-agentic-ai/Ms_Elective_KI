"""
Step 2a — Few-Shot Prompting
-----------------------------
Provide the model with 2–3 examples of input→output pairs before asking
your real question. The model learns the expected format and style from
the examples — no training, no fine-tuning, just context.

Each example is a real "user" -> "assistant" turn, not text glued into one
message: the "user" turn poses the example input, and the "assistant" turn
shows the ideal output, exactly as if the model had already answered it.
The final "user" turn is the real question, left for the model to complete.

This is "in-context learning": the examples are part of the prompt, not
part of the model weights.

Compare to step 1 (zero examples): does showing the model what good
output looks like change what it produces?

Run:
    uv run python src/exercises/step_02a_few_shot.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

os.makedirs("output", exist_ok=True)

# ── Examples — show the model what good output looks like ────────────────────
# Each pair is one "shot", encoded as a real user->assistant turn.
# Two examples = two-shot prompting.
example_1_input  = "TODO: a simpler or related input (not your main topic)"
example_1_output = "TODO: the ideal output for example 1 — this teaches format and style"

example_2_input  = "TODO: a second example input"
example_2_output = "TODO: ideal output for example 2"

# ── The actual question — the final "user" turn, left for the model to complete ──
user_message = "TODO: same topic as previous steps"

# ── Roles — no persona needed, so "system" is left out; "assistant" is used
# for real this time, holding the ideal answer to each example "user" turn ────
response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[
        {"role": "user", "content": example_1_input},
        {"role": "assistant", "content": example_1_output},
        {"role": "user", "content": example_2_input},
        {"role": "assistant", "content": example_2_output},
        {"role": "user", "content": user_message},
    ],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02a.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2a — Few-Shot Prompting\n\n"
        f"**Topic:** {user_message}\n\n"
        f"## Example 1\n\n"
        f"**User:**\n```\n{example_1_input}\n```\n\n"
        f"**Assistant:**\n```\n{example_1_output}\n```\n\n"
        f"## Example 2\n\n"
        f"**User:**\n```\n{example_2_input}\n```\n\n"
        f"**Assistant:**\n```\n{example_2_output}\n```\n\n"
        f"## Question\n\n```\n{user_message}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
