# Step 2 — Prompting Techniques

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/02-prompt-template.md)

Five notebooks, same topic, same model throughout. Each is a different strategy for shaping what the model produces — without a framework, without agents. Work through them in order and compare the outputs.

## Background

A prompt is a program. The strategies you apply — providing examples, structuring inputs into named components, splitting a task into sequential calls, asking for explicit reasoning — are the code. The model is the runtime.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

Each notebook below includes the specific citation for its technique.

## The five notebooks

| # | Notebook | What it adds |
| --- | --- | --- |
| 2a | [step_02a_few_shot.ipynb](step_02a_few_shot.ipynb) | Few-shot examples (Brown et al., 2020) |
| 2b | [step_02b_prompt_template.ipynb](step_02b_prompt_template.ipynb) | `system`/`user` role split, structured components |
| 2c | [step_02c_chain_prompting.ipynb](step_02c_chain_prompting.ipynb) | Two sequential calls, output chained into the next prompt |
| 2d | [step_02d_chain_of_thought.ipynb](step_02d_chain_of_thought.ipynb) | Explicit reasoning instruction (Kojima et al., 2022) |
| 2e | [step_02e_tree_of_thought.ipynb](step_02e_tree_of_thought.ipynb) | Parallel "expert" reasoning paths (Yao et al., 2023) |

## Your task

1. Open each notebook in VS Code/Cursor, select the **"research_crew"** kernel, and set your topic — same topic as step 1, same topic across 2a–2e.

2. Fill in the `TODO` fields and run the cells in each notebook (Setup cell first, then the exercise cell). Each notebook's own "Your task" section has the specific comparison question for that technique.

3. Fill in the **Step 2** section of `EVALUATION.md` as you go.

## Stretch goal

In 2a, try a "zero-shot" variant by removing the examples entirely and just asking the question — then compare to the few-shot version. Is the improvement from examples large, small, or unexpected?
