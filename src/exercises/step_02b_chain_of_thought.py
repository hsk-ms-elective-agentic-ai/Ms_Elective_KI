"""
Step 2b — Chain of Thought Prompting
-------------------------------------
Same structure as step 2a, but with an explicit reasoning instruction added.
Instead of asking for the answer directly, ask the model to reason through
the problem before giving its final answer.

Compare to step 2a: does making the reasoning explicit change the output?

Run:
    uv run python src/exercises/step_02b_chain_of_thought.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

persona       = "TODO: who is the model?\n"
instruction   = "TODO: what should it do?\n"
context       = "TODO: what background does it need?\n"
data_format   = "TODO: what should the output look like?\n"
audience      = "TODO: who will read the output?\n"
tone          = "TODO: what tone should it use?\n"
reasoning     = "TODO: add an instruction that asks the model to reason step by step before answering\n"

text          = "TODO: same topic as step 2a"
data          = f"Topic: {text}\n"

query = persona + instruction + context + data_format + audience + tone + reasoning + data

response = completion(
    model=os.getenv("MODEL", "gpt-4o-mini"),
    messages=[
        {"role": "user", "content": query},
    ],
)

print(response.choices[0].message.content)
