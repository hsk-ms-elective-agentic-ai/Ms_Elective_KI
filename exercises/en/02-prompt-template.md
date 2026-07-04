# Step 2 — Prompt Template

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/02-prompt-template.md)

Same model, same single API call, same topic — but now with a **system prompt** that assigns a role and specifies an output format. No framework, just two messages. The question this step is built around: how much of the difference between a mediocre and a useful LLM response comes from the model, and how much from how you instruct it?

## Background

"System", "user", and "assistant" roles are a convention — a labeling scheme that tells the model which parts of the context window are instructions vs. questions vs. prior answers. The model processes them all as tokens, but its training included enough examples of role-labeled conversations that the labels shift which part of its training distribution the response draws from.

The key insight this step demonstrates:

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

The core idea: a prompt is a program. The role, format instructions, and constraints you write are the code; the model is the runtime. You can change what the program produces without changing the runtime at all.

## The code

Open [src/exercises/step_02_prompt_template.py](../../src/exercises/step_02_prompt_template.py). Compare it to step 1 — the only additions are:

| Added | What it does |
| --- | --- |
| `SYSTEM_PROMPT` | Assigns a role ("senior research analyst") and mandates four output sections |
| `USER_PROMPT` | Formatted string with the topic substituted in |
| Two messages instead of one | System message sets context; user message poses the question |

No new dependencies, no framework.

## Your task

1. Set `TOPIC` to the same topic you used in step 1.

2. Run it:
   ```bash
   uv run python src/exercises/step_02_prompt_template.py
   ```

3. Compare the output to step 1:
   - Did the four sections from `SYSTEM_PROMPT` actually appear?
   - Is the output more or less useful for your specific topic — or just differently formatted?
   - What does the model do with the "Open Questions" section — does it generate genuine open questions, or filler?

4. **Experiment**: try at least one of these and observe what changes:
   - Remove the section headings from `SYSTEM_PROMPT` — does the format disappear, or does the model keep it anyway?
   - Change the role from "senior research analyst" to something different (e.g. "skeptical journalist", "first-year student"). Does the output change in the way you'd expect?

5. Fill in the **Step 2** section of `EVALUATION.md`.

## Stretch goal

Write a second template for the same topic but for a different audience (e.g. a student vs. a board member). Run both. Does the audience specification meaningfully change what information appears — or just the tone?
