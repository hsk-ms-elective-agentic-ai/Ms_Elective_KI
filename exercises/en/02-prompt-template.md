# Step 2 — Prompting Techniques

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/02-prompt-template.md)

Six scripts, same topic, same model. Each is a different strategy for shaping what the model produces — without a framework, without agents. Run all six and compare the outputs.

## Background

A prompt is a program. The strategies you apply — providing examples, structuring inputs into named components, splitting a task into sequential calls, asking for explicit reasoning — are the code. The model is the runtime.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

**Few-shot prompting** — providing input/output examples in the prompt so the model learns the expected format and style from context alone, without any weight updates — was the central finding of:

> Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., … Amodei, D. (2020). *Language Models are Few-Shot Learners*. NeurIPS 2020. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

**Zero-shot chain-of-thought** — adding a short instruction asking the model to reason step by step before answering, with no worked examples — was demonstrated in:

> Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). *Large Language Models are Zero-Shot Reasoners*. NeurIPS 2022. [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)

Wei et al. (2022) showed separately that including full worked reasoning chains as few-shot examples also improves performance — the two results are complementary:

> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

**Tree of thought** — exploring multiple reasoning paths instead of a single chain, with the ability to compare, backtrack, or discard a path partway through — was introduced in:

> Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. NeurIPS 2023. [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)

## The six scripts

### 2a — Few-Shot Prompting
[src/exercises/step_02a_few_shot.py](../../src/exercises/step_02a_few_shot.py)

Two or three input/output example pairs appear in the prompt before the real question. The model learns the expected format and style from those examples — this is in-context learning (Brown et al., 2020). No structure, no reasoning instruction, just patterns.

### 2b — Prompt Template
[src/exercises/step_02b_prompt_template.py](../../src/exercises/step_02b_prompt_template.py)

One API call, no examples, no reasoning instruction — but now the message is split across two *roles*:

- **`system`**: background instructions the end user never sees — `persona`, `instruction`, `context`, `data_format`, `audience`, `tone`. This tells the model who it is and how it should behave for every response in the conversation.
- **`user`**: the actual question — just the topic you want answered.

This is the standard structure of the OpenAI Chat Completions API (and any model that follows it). The `system` role is a first-class concept in the protocol, not just a formatting convention. Try removing individual system components to see what each one actually controls.

### 2c — Chain Prompting
[src/exercises/step_02c_chain_prompting.py](../../src/exercises/step_02c_chain_prompting.py)

Two sequential API calls: the first extracts or prepares something from the topic; the second receives that output and produces the final answer. The task is deliberately split across calls.

### 2d — Chain of Thought
[src/exercises/step_02d_chain_of_thought.py](../../src/exercises/step_02d_chain_of_thought.py)

Same component structure as 2b, with one addition: a `reasoning` component that asks the model to think through the problem before giving its answer. This is the zero-shot CoT pattern from Kojima et al. (2022) — no examples needed, just the instruction.

### 2f — Structured Output (JSON Mode)
[src/exercises/step_02f_structured_output.py](../../src/exercises/step_02f_structured_output.py)

Same persona/instruction pattern as 2b, but the API call adds `response_format={"type": "json_object"}`. This constrains the model to emit valid JSON syntax — the prompt still has to describe the exact shape you want, but the output is now something your code can parse directly (`result["field"]`) instead of a paragraph you'd have to scrape.

### 2g — Tree of Thought
[src/exercises/step_02g_tree_of_thought.py](../../src/exercises/step_02g_tree_of_thought.py)

One user message asks several "experts" to reason in parallel: each writes down one step, shares it with the group, then all move on to the next step together — and any expert whose reasoning turns out to be wrong drops out. This is a zero-shot, single-prompt approximation of the tree-of-thought idea (Yao et al., 2023) — it explores multiple reasoning paths at once instead of committing to a single chain like 2d, without the full search-and-backtrack procedure from the paper.

## Your task

1. Set your topic in all six scripts — same topic as step 1, same topic across 2a–2g.

2. Fill in the `TODO` fields and run each script:
   ```bash
   uv run python src/exercises/step_02a_few_shot.py
   uv run python src/exercises/step_02b_prompt_template.py
   uv run python src/exercises/step_02c_chain_prompting.py
   uv run python src/exercises/step_02d_chain_of_thought.py
   uv run python src/exercises/step_02f_structured_output.py
   uv run python src/exercises/step_02g_tree_of_thought.py
   ```

3. Compare the six outputs (each is saved to `output/step_02*.md`):
   - In 2a, do the examples steer the model toward a specific format or conclusion? What happens if you change just one example?
   - Which components in 2b had the most visible effect? Try removing one at a time.
   - In 2c, does the two-step split improve the final output, or does the model produce something similar in one shot?
   - Does the `reasoning` instruction in 2d produce noticeably different conclusions — or just more text?
   - In 2f, try asking for a shape the model can't cleanly fill from the question you gave it — does it fill fields with guesses, or leave them empty/null?
   - In 2g, compare to 2d — do the "experts" actually disagree and drop out, or do they converge immediately on the same answer? Try changing `num_experts`.

4. Fill in the **Step 2** section of `EVALUATION.md`.

## Stretch goal

In 2a, try a "zero-shot" variant by removing the examples entirely and just asking the question — then compare to the few-shot version. Is the improvement from examples large, small, or unexpected?
