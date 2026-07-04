# Step 2 — Prompting Techniques

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/02-prompt-template.md)

Four scripts, same topic, same model. Each is a different strategy for shaping what the model produces — without a framework, without agents. Run all four and compare the outputs.

## Background

A prompt is a program. The strategies you apply — providing examples, structuring inputs into named components, splitting a task into sequential calls, asking for explicit reasoning — are the code. The model is the runtime.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

**Few-shot prompting** — providing input/output examples in the prompt so the model learns the expected format and style from context alone, without any weight updates — was the central finding of:

> Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., … Amodei, D. (2020). *Language Models are Few-Shot Learners*. NeurIPS 2020. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

**Zero-shot chain-of-thought** — adding a short instruction asking the model to reason step by step before answering, with no worked examples — was demonstrated in:

> Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). *Large Language Models are Zero-Shot Reasoners*. NeurIPS 2022. [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)

Wei et al. (2022) showed separately that including full worked reasoning chains as few-shot examples also improves performance — the two results are complementary:

> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

## The four scripts

### 2a — Few-Shot Prompting
[src/exercises/step_02a_few_shot.py](../../src/exercises/step_02a_few_shot.py)

Two or three input/output example pairs appear in the prompt before the real question. The model learns the expected format and style from those examples — this is in-context learning (Brown et al., 2020). No structure, no reasoning instruction, just patterns.

### 2b — Prompt Template
[src/exercises/step_02b_prompt_template.py](../../src/exercises/step_02b_prompt_template.py)

The prompt is split into named components (`persona`, `instruction`, `context`, `data_format`, `audience`, `tone`, `data`) concatenated into a single query. One API call, no examples, no reasoning instruction.

### 2c — Chain Prompting
[src/exercises/step_02c_chain_prompting.py](../../src/exercises/step_02c_chain_prompting.py)

Two sequential API calls: the first extracts or prepares something from the topic; the second receives that output and produces the final answer. The task is deliberately split across calls.

### 2d — Chain of Thought
[src/exercises/step_02d_chain_of_thought.py](../../src/exercises/step_02d_chain_of_thought.py)

Same component structure as 2b, with one addition: a `reasoning` component that asks the model to think through the problem before giving its answer. This is the zero-shot CoT pattern from Kojima et al. (2022) — no examples needed, just the instruction.

## Your task

1. Set your topic in all four scripts — same topic as step 1, same topic across 2a/2b/2c/2d.

2. Fill in the `TODO` fields and run each script:
   ```bash
   uv run python src/exercises/step_02a_few_shot.py
   uv run python src/exercises/step_02b_prompt_template.py
   uv run python src/exercises/step_02c_chain_prompting.py
   uv run python src/exercises/step_02d_chain_of_thought.py
   ```

3. Compare the four outputs (each is saved to `output/step_02*.md`):
   - In 2a, do the examples steer the model toward a specific format or conclusion? What happens if you change just one example?
   - Which components in 2b had the most visible effect? Try removing one at a time.
   - In 2c, does the two-step split improve the final output, or does the model produce something similar in one shot?
   - Does the `reasoning` instruction in 2d produce noticeably different conclusions — or just more text?

4. Fill in the **Step 2** section of `EVALUATION.md`.

## Stretch goal

In 2a, try a "zero-shot" variant by removing the examples entirely and just asking the question — then compare to the few-shot version. Is the improvement from examples large, small, or unexpected?
