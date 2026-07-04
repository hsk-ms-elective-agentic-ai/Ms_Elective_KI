"""
Step 2c — Chain Prompting
--------------------------
Break the task into two sequential API calls. The output of the first
call becomes the input for the second.

This is different from steps 2a and 2b (one big prompt): here you
deliberately split the problem into two separate LLM interactions,
each focused on a narrower sub-task.

Compare to steps 2a and 2b: does splitting the task change the final output?

Run:
    uv run python src/exercises/step_02c_chain_prompting.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

TOPIC = "TODO: same topic as steps 2a and 2b"

# ── First call — extract, plan, or prepare ────────────────────────────────────
prompt_1 = f"TODO: write a first prompt that extracts or prepares something from the topic: {TOPIC}"

response_1 = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": prompt_1}],
)
output_1 = response_1.choices[0].message.content

print("=== First call output ===")
print(output_1)

# ── Second call — use the first output to produce the final answer ────────────
prompt_2 = f"TODO: write a second prompt that uses the output below to produce the final answer\n\n{output_1}"

response_2 = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": prompt_2}],
)

print("\n=== Final output ===")
print(response_2.choices[0].message.content)
