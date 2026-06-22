# Assignment Templates

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-templates.md)

Copy these into your team repo and fill them in. See [Assignment Overview](assignment-overview.md) for how they're used and [Assignment Milestones](assignment-milestones.md) for what to write at each stage.

## `RISK_LOG.md`

Append a new section per milestone — never edit a previous one, even if you'd answer it differently now. The history of your thinking is the point.

```markdown
# Risk Log

## M0 — Baseline (YYYY-MM-DD)
**Decision:** [what you chose and why, one or two sentences]
**Risk:** [what could go wrong]
**Mitigation / accepted tradeoff:** [what you'd do about it, or why you're accepting it as-is]

## M1 — Tools (YYYY-MM-DD)
...
```

## User story (per epic, in a GitHub Issue)

```markdown
**Story:** As a [stakeholder of the crew's output], I want [capability], so that [value].

**Acceptance criteria:**
- [ ] [testable condition 1]
- [ ] [testable condition 2]

**Definition of done:**
- [ ] Implemented in `agents.yaml`/`tasks.yaml`/`crew.py`
- [ ] Risk identified and logged in `RISK_LOG.md`
```

## `RETROSPECTIVE.md` (final submission only)

```markdown
# Retrospective

## What changed since the interim submission?
[Specific design decisions you reversed or revised]

## Why?
[What you learned — a lecture concept, a failed test, a teammate's challenge — that caused the change]

## What would you do differently with another four weeks?
[Honest answer, not a wish list]
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub handle | Primary contribution |
| --- | --- | --- |
| ... | ... | ... |

Topic: [your crew's topic]
```
