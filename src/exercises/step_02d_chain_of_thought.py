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

persona       = "You are a helpful assistant.\n"
instruction   = "You are an expert in EU AI Act compliance.\n"
context       = "You are assisting a B2B SaaS company that uses LLMs in its product.\n"
data_format   = "Provide your response in bullet points.\n"
audience      = "The output will be read by legal professionals and compliance officers.\n"
tone          = "Be professional and concise.\n"
reasoning     = "First, think through the problem step by step. Then, provide your final answer.\n"

text          = "EU AI Act compliance requirements for a B2B SaaS company that uses LLMs in its product"
data          = f"Topic: {text}\n"

query = persona + instruction + context + data_format + audience + tone + reasoning + data

os.makedirs("output", exist_ok=True)

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[{"role": "user", "content": query}],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02d.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2d — Chain of Thought\n\n"
        f"**Topic:** {text}\n\n"
        f"## Prompt\n\n```\n{query}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
