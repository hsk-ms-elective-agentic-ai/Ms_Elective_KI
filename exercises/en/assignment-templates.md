# Assignment Templates

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-templates.md)

**`EVALUATION.md` and `TEAM.md` already exist at your repo root** — every team's copy starts with them already in place. Fill them in directly; they're reproduced below for reference. See [Assignment Overview](assignment-overview.md) for how they're used, and each step's own page for what to write at each stage.

## `EVALUATION.md`

This is the main deliverable: a comparative analysis of what each step added, grounded specifically in your topic. Fill in each step's section as you run it — write observations right after running, not at the end. The comparison *is* the assignment; generic answers ("it's more accurate") score less than specific ones ("the analyst in step 4 flagged X as overstated, which the researcher in step 3 didn't question").

```markdown
# Step Evaluation

**Team:** [team name] · **Topic:** [your topic] · **Last updated:** [step N, YYYY-MM-DD]

## Your topic

[One or two sentences: what specific problem does your topic address, and who would use the output?
"AI in healthcare" is too broad. "How AI is being used for early cancer detection in radiology, 
aimed at radiologists evaluating diagnostic support tools" is the right level of specificity.]

## Step-by-step observations

Run each step with the same topic. Fill in right after running.

### Step 1 — Simple Prompting
**Date run:**
**What the output looks like (2–3 sentences):**
**One thing that surprised you:**

### Step 2 — Prompting Techniques
**Date run:**
**2a (Prompt Template) — what changed vs Step 1:**
**2b (Chain of Thought) — what changed vs 2a:**
**2c (Chain Prompting) — what changed vs 2a/2b:**
**Which technique worked best for your topic, and why:**
**One thing that surprised you:**

### Step 3 — Single Agent
**Date run:**
**What changed vs Step 2 (be specific):**
**What's better:**
**What's harder or more fragile:**
**One thing that surprised you:**

### Step 4 — Multi-Agent
**Date run:**
**What changed vs Step 3 (be specific):**
**What's better:**
**What's harder or more fragile:**
**One thing that surprised you:**

### Step 5 — RAG + Tools
**Date run:**
**What changed vs Step 4 (be specific):**
**What's better:**
**What's harder or more fragile:**
**One thing that surprised you:**

## Your recommendation

For your specific topic and use case: which step's level of complexity would you actually
deploy, and why? What would you lose by going one step simpler? What would you gain
by going one step more complex — and is that gain worth the added fragility?

[150–250 words. Specific to your topic, not generic.]

## Alternatives you tried

What else did you experiment with? (A different topic formulation, a different role 
definition in the agent backstory, a different knowledge document, a tool that didn't 
work as expected?) What did you find?

## What you'd add next

If you had two more weeks and one more API key, what specifically would you change, 
add, or test? Why that, and not something else?
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub handle | Primary contribution |
| --- | --- | --- |
| | | |

Topic: [your topic]
```

## Peer evaluation (private — do not commit this to your repo)

Submit this directly to your instructor (email, not GitHub) at each submission deadline. Keeping it out of the shared repo is what makes honest feedback possible; this feeds the individual adjustment described in [Assignment Overview](assignment-overview.md#grading).

```markdown
# Peer Evaluation — [your name] — [interim / final]

## Your teammates
One section per teammate, not yourself:

### [Teammate name]
- Contribution (1–5, 5 = pulled their full share or more):
- What did they actually do this stage, specifically?
- Anything else your instructor should know? (optional, confidential)

## Yourself
- What did you contribute this stage, specifically?
```
