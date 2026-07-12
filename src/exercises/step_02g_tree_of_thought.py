"""
Step 2g — Tree of Thought
---------------------------
Instead of committing to one line of reasoning, ask several "experts" to
reason in parallel: each writes down one step, shares it with the group,
then all move on to the next step together. Any expert whose reasoning
turns out to be wrong drops out along the way.

This is a lightweight, zero-shot way to explore multiple reasoning paths
within a single prompt, instead of the search-and-backtrack procedure from
the original Tree-of-Thought paper.

Compare to step 2d (chain of thought): does exploring several reasoning
paths in parallel change the final answer, or just add discussion around it?

Run:
    uv run python src/exercises/step_02g_tree_of_thought.py
"""
import os

from dotenv import load_dotenv
from litellm import completion

load_dotenv()
os.makedirs("output", exist_ok=True)

# ── User message — ask several "experts" to reason step by step in parallel,
# sharing and checking each other's steps, dropping any expert who goes wrong ──
num_experts = 3
question = "TODO: same topic as previous steps, phrased as a question with a reasoned answer"

user_message = (
    f"Imagine {num_experts} different experts are answering this question. "
    f"All experts will write down 1 step of their thinking, then share it "
    f"with the group. Then all experts will go on to the next step, etc. "
    f"If any expert realizes they're wrong at any point then they leave. "
    f"The question is '{question}' Make sure to discuss the results."
)

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[
        {"role": "user", "content": user_message},
    ],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02g.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2g — Tree of Thought\n\n"
        f"**Question:** {question}\n\n"
        f"## User message\n\n```\n{user_message}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
