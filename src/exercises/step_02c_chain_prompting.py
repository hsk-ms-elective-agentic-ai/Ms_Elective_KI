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


def build_messages(system_message: str, user_message: str, assistant_message: str) -> list[dict]:
    """Only "user" is populated in this step — system and assistant stay empty
    because each call is independent; no history carries over between them."""
    return [
        {"role": role, "content": content}
        for role, content in [
            ("system", system_message),
            ("user", user_message),
            ("assistant", assistant_message),
        ]
        if content
    ]


# ── First call — extract, plan, or prepare ────────────────────────────────────
prompt_1 = f"TODO: write a first prompt that extracts or prepares something from the topic: {TOPIC}"

response_1 = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=build_messages(system_message="", user_message=prompt_1, assistant_message=""),
)
output_1 = response_1.choices[0].message.content

print("=== First call output ===")
print(output_1)

# ── Second call — use the first output to produce the final answer ────────────
# The first call's output is passed along as plain text inside this "user"
# message, not as an "assistant" turn — the two calls share no conversation history.
prompt_2 = f"TODO: write a second prompt that uses the output below to produce the final answer\n\n{output_1}"

response_2 = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=build_messages(system_message="", user_message=prompt_2, assistant_message=""),
)

output_2 = response_2.choices[0].message.content
print("\n=== Final output ===")
print(output_2)

os.makedirs("output", exist_ok=True)
with open("output/step_02c.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2c — Chain Prompting\n\n"
        f"**Topic:** {TOPIC}\n\n"
        f"## First prompt\n\n```\n{prompt_1}\n```\n\n"
        f"## First output\n\n{output_1}\n\n"
        f"## Second prompt\n\n```\n{prompt_2}\n```\n\n"
        f"## Final output\n\n{output_2}\n"
    )
