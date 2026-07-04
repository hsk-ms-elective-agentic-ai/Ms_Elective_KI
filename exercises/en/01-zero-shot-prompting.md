# Step 1 — Zero-Shot Prompting

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/01-zero-shot-prompting.md)

The simplest path from question to answer: one API call, one message, one response. No role definition, no output structure, no examples, no framework — just the model and your text. This is the baseline everything else in this series builds on, and the right place to start: you can't evaluate what a technique adds until you've seen what you get without it.

## Background

"Zero-shot" means the model receives no examples of the expected output — it must answer entirely from what it learned during training. This is the default mode for most people using LLMs: type a question, get a response.

A large language model is, at the lowest level, a function that predicts the most probable next token given a context window of prior tokens. When you send a plain user message, you get whatever completion the model considers most likely given its training — which is powerful, but entirely dependent on how the topic is represented in the training data, and entirely dependent on *you* to post-process or rerun if the output is wrong.

No citation needed here. The point is empirical: observe what you get before any technique is applied.

## The code

Open [src/exercises/step_01_zero_shot_prompting.py](../../src/exercises/step_01_zero_shot_prompting.py). It's about 15 lines:

1. Load `.env` (for the API key and `MODEL`)
2. Call `litellm.completion()` with a single user message
3. Print the response and save it to `output/step_01.md`

`litellm` is already a dependency of this project — no new install needed.

## Your task

1. **Pick your topic** — use one from the [use case table in the main README](../../README.md#use-cases-to-pick-from), or propose your own. Be specific: "AI in healthcare" is a subject area; "AI-assisted early cancer detection in radiology" is a topic a specific person would have a specific use for. **This topic stays fixed for all 5 steps** — the whole point is comparing what changes as the system grows, with everything else held constant.

2. Set `TOPIC` in the file to your team's topic.

3. Run it:
   ```bash
   uv run python src/exercises/step_01_zero_shot_prompting.py
   ```

4. Read the output carefully. Note:
   - What structure did the model produce on its own, without being asked?
   - How specific vs. generic does it feel for your topic?
   - How confident does the tone sound — does that confidence feel earned, or is it the model hedging without actually knowing?

5. Fill in the **Step 1** section of `EVALUATION.md`.

## Stretch goal

Run the exact same script twice on the same topic. How different are the two outputs? What does that variability mean if someone were building a workflow that depends on this output being consistent?
