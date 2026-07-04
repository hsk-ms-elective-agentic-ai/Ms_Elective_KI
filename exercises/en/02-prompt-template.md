# Step 2 — Prompting Techniques

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/02-prompt-template.md)

Three scripts, same topic, same model. Each one is a different strategy for shaping what the model produces — without a framework, without agents. Run all three and compare the outputs.

## Background

A prompt is a program. The strategies you apply — structuring inputs into named components, asking for explicit reasoning, splitting a task into sequential calls — are the code. The model is the runtime.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

Chain-of-thought prompting specifically — showing that asking the model to reason before answering improves performance on complex tasks — was demonstrated in:

> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

## The three scripts

### 2a — Prompt Template
[src/exercises/step_02a_prompt_template.py](../../src/exercises/step_02a_prompt_template.py)

The prompt is split into named components (`persona`, `instruction`, `context`, `data_format`, `audience`, `tone`, `data`) concatenated into a single query. One API call.

### 2b — Chain of Thought
[src/exercises/step_02b_chain_of_thought.py](../../src/exercises/step_02b_chain_of_thought.py)

Same component structure as 2a, with one addition: a `reasoning` component that asks the model to think through the problem before giving its answer. One API call.

### 2c — Chain Prompting
[src/exercises/step_02c_chain_prompting.py](../../src/exercises/step_02c_chain_prompting.py)

Two sequential API calls: the first extracts or prepares something from the topic; the second receives that output and produces the final answer. The task is deliberately split.

## Your task

1. Set your topic in all three scripts — same topic as step 1, same topic across 2a/2b/2c.

2. Fill in the `TODO` fields and run each script:
   ```bash
   uv run python src/exercises/step_02a_prompt_template.py
   uv run python src/exercises/step_02b_chain_of_thought.py
   uv run python src/exercises/step_02c_chain_prompting.py
   ```

3. Compare the three outputs:
   - Which components in 2a had the most visible effect? Try removing one at a time.
   - Does the `reasoning` component in 2b produce noticeably different conclusions — or just more text?
   - In 2c, does the two-step split improve the final output, or does the model produce something similar in one shot?

4. Fill in the **Step 2** section of `EVALUATION.md`.

## Stretch goal

In step 2c, try reversing the order of the two prompts — do the "final" step first, then refine it with the output of the "preparation" step. Does the order matter?
