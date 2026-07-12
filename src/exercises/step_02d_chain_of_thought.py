"""
Step 2d — Chain of Thought Prompting
-------------------------------------
Same structure as step 2b (prompt template), but with an explicit reasoning
instruction added. Instead of asking for the answer directly, ask the model
to reason through the problem before giving its final answer.

Compare to step 2b: does making the reasoning explicit change the output?

Run:
    uv run python src/exercises/step_02d_chain_of_thought.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# ── System message — same components as step 2b, plus an explicit reasoning
# instruction telling the model to think step by step before answering ────────
persona       = "You are a helpful assistant.\n"
instruction   = "You are an expert in EU AI Act compliance.\n"
context       = "You are assisting a B2B SaaS company that uses LLMs in its product.\n"
data_format   = "Provide your response in bullet points.\n"
audience      = "The output will be read by legal professionals and compliance officers.\n"
tone          = "Be professional and concise.\n"
reasoning     = "First, think through the problem step by step. Then, provide your final answer.\n"

system_message = persona + instruction + context + data_format + audience + tone + reasoning

# ── User message — the actual question ───────────────────────────────────────
text = "EU AI Act compliance requirements for a B2B SaaS company that uses LLMs in its product"
user_message = f"Topic: {text}\n"

os.makedirs("output", exist_ok=True)

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02d.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2d — Chain of Thought\n\n"
        f"**Topic:** {text}\n\n"
        f"## System message\n\n```\n{system_message.strip()}\n```\n\n"
        f"## User message\n\n```\n{user_message.strip()}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
