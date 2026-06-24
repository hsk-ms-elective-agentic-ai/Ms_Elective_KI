# Sprint 5 — Production Safety & Stability

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/05-production-safety.md)

Moving an agent from "works on my machine" to production means: reproducible environments, observability into what the agent is actually doing, and a way for non-developers to run it — none of which changes agent logic, it's the operational layer around it. Agent-specific security adds its own risks beyond standard appsec: secrets leaking into version control, prompt injection (untrusted content from a tool, like a search result, containing instructions that hijack the agent), and over-broad tool permissions. The common thread: agents act on content they retrieve, so anything that content can influence is an attack surface.

There's no single seminal paper for "agent operations" the way there is for RAG or tool use:

> Lakshmanan, V. (2025). *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications*. O'Reilly Media. (See the deployment/observability chapters.)

Indirect prompt injection — malicious instructions arriving not from the user's own prompt, but from content the model *retrieves* — was first systematically demonstrated against real LLM-integrated applications in:

> Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security, 79–90. [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)

![Indirect prompt injection: an adversary injects prompts into content (webpages, files, emails) that an LLM-integrated application retrieves, steering its output without ever talking to the model directly](../assets/promptinjection-greshake2023-fig1.png)
*Figure 1 from Greshake et al. (2023): an adversary can indirectly control the LLM by injecting prompts into sources it retrieves. Reproduced for educational use in this course.*

## In this repo

Production, demonstrated already in this template: [.devcontainer/devcontainer.json](../../.devcontainer/devcontainer.json) + `uv.lock` give everyone an identical environment; [streamlit_app.py](../../streamlit_app.py) subscribes to CrewAI's event bus (`crewai_event_bus`) and streams events live instead of only showing a final report — the same mechanism real production monitoring would use, just rendered in a demo UI instead of a logging backend.

Security, a real near-miss from building this project: a `.env.example` file (the *template*, tracked by git) almost got real API keys committed to it instead of the real `.env` file (gitignored), because the names look similar. The pattern that prevented an actual leak: `.env` is listed in [.gitignore](../../.gitignore), `.env.example` ships with empty placeholders only, and `git status`/`git diff` get checked before every push.

## Your task

1. **Sprint planning**: open 1–2 GitHub Issues as user stories labeled `epic:hardening`, for whichever gap your team finds most concerning.
2. Write a short production plan: what would you monitor, and what would actually alert you to failure, specifically for your use case (not a generic list).
3. **Prompt injection drill**: construct one concrete, hypothetical (not executed) prompt-injection scenario specific to *your* tools and knowledge sources — not the generic search-result example from this page. Reason through what would actually happen given your task's `context` dependencies — does the receiving agent treat upstream output as data or as instructions?
4. Optional: add a `guardrail` to one task that checks for suspicious content and fails validation if found — `Task(guardrail=fn)`, a function `(output) -> (bool, Any)`.
5. Complete `DESIGN.md`'s Security & threat model and Production considerations sections.
6. Write the final **Design history** entry: what changed between your interim (sprint 3) and final design, and what did you learn that made you change it? That's worth more than it looks — it's the one place you have to show your reasoning evolved, not just accumulated.
7. Before calling this done, answer in `DESIGN.md`: if this crew ran unattended for a semester on your real use case, what's the first thing that breaks, and how would you actually know — not "someone would notice eventually," a specific signal you'd see.

## Stretch goal

Run `git log --all --oneline -- .env` on your own team repo to confirm `.env` itself has never been committed in your history. If it has, that's a real finding for your threat model, not a hypothetical one.

---

**This is your final submission.** See [Assignment Overview](assignment-overview.md) for the full grading rubric and exactly what to submit.
