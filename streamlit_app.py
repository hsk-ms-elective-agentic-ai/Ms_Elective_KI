"""Browser frontend for all five exercise steps.

Run with: uv run streamlit run streamlit_app.py
"""
import os
import queue
import threading

import streamlit as st
from dotenv import load_dotenv
from litellm import completion

from crewai.events.event_bus import crewai_event_bus
from crewai.events.types.agent_events import (
    AgentExecutionCompletedEvent,
    AgentExecutionStartedEvent,
)
from crewai.events.types.task_events import TaskCompletedEvent, TaskStartedEvent
from crewai.events.types.tool_usage_events import (
    ToolUsageErrorEvent,
    ToolUsageFinishedEvent,
    ToolUsageStartedEvent,
)

from research_crew.crew import ResearchCrew

load_dotenv()

os.makedirs("output", exist_ok=True)



def save_output(step_id: str, prompt: str, output: str, topic: str = "") -> str:
    """Overwrite output/step_<id>.md with the latest run and return the file path."""
    label = {
        "01":  "Step 1 — Zero-Shot Prompting",
        "02a": "Step 2a — Few-Shot Prompting",
        "02b": "Step 2b — Prompt Template",
        "02c": "Step 2c — Chain Prompting",
        "02d": "Step 2d — Chain of Thought",
    }.get(step_id, f"Step {step_id}")
    path = f"output/step_{step_id}.md"
    model = os.getenv("MODEL", "gpt-4o-mini")
    content = (
        f"# {label}\n\n"
        f"**Model:** `{model}`  \n"
        f"**Topic:** {topic or '—'}\n\n"
        f"## Prompt\n\n```\n{prompt.strip()}\n```\n\n"
        f"## Output\n\n{output.strip()}\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


ICONS = {
    "task_started": "📋",
    "task_completed": "✅",
    "agent_started": "🤖",
    "agent_completed": "✔️",
    "tool_started": "🔧",
    "tool_finished": "🔧✅",
    "tool_error": "⚠️",
}


def run_crew(crew, topic: str, events: queue.Queue) -> None:
    with crewai_event_bus.scoped_handlers():
        @crewai_event_bus.on(TaskStartedEvent)
        def _on_task_started(source, event):
            task = event.task
            name = getattr(task, "description", None) or "Task"
            events.put(("task_started", name.strip()[:200]))

        @crewai_event_bus.on(TaskCompletedEvent)
        def _on_task_completed(source, event):
            events.put(("task_completed", ""))

        @crewai_event_bus.on(AgentExecutionStartedEvent)
        def _on_agent_started(source, event):
            events.put(("agent_started", getattr(event.agent, "role", "Agent")))

        @crewai_event_bus.on(AgentExecutionCompletedEvent)
        def _on_agent_completed(source, event):
            events.put(("agent_completed", getattr(event.agent, "role", "Agent")))

        @crewai_event_bus.on(ToolUsageStartedEvent)
        def _on_tool_started(source, event):
            events.put(("tool_started", event.tool_name))

        @crewai_event_bus.on(ToolUsageFinishedEvent)
        def _on_tool_finished(source, event):
            events.put(("tool_finished", event.tool_name))

        @crewai_event_bus.on(ToolUsageErrorEvent)
        def _on_tool_error(source, event):
            events.put(("tool_error", f"{event.tool_name}: {event.error}"))

        try:
            result = crew.kickoff(inputs={"topic": topic})
            events.put(("done", result.raw))
        except Exception as exc:
            events.put(("error", str(exc)))


# ── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(page_title="AI Exercises", page_icon="🧑‍🔬", layout="wide")
st.title("🧑‍🔬 Generative & Agentic AI — Hands-On Exercises")

tab_prompting, tab_crew = st.tabs(["Prompting — Steps 1 & 2", "Research Crew — Steps 3–5"])

# ── Tab 1: Prompting exercises ────────────────────────────────────────────────

with tab_prompting:
    _model = os.getenv("MODEL", "gpt-4o-mini")
    st.caption(f"Model: `{_model}`  ·  Set `MODEL` in `.env` to change it.")

    step = st.radio(
        "Step",
        [
            "1 — Zero-Shot Prompting",
            "2a — Few-Shot Prompting",
            "2b — Prompt Template",
            "2c — Chain Prompting",
            "2d — Chain of Thought",
        ],
        horizontal=True,
    )

    st.divider()

    # ── Step 1 ────────────────────────────────────────────────────────────────
    if step == "1 — Zero-Shot Prompting":
        st.markdown("One message, one response. No structure, no examples, no persona — the model answers from training data alone.")
        message = st.text_area("Your message", height=120)
        if st.button("Run", type="primary", key="run_1"):
            if not message.strip():
                st.warning("Enter a message first.")
            else:
                with st.spinner("Calling model…"):
                    try:
                        resp = completion(
                            model=_model,
                            messages=[{"role": "user", "content": message}],
                        )
                        output = resp.choices[0].message.content
                        path = save_output("01", message, output, topic=message[:80])
                        st.caption(f"Saved to `{path}`")
                        st.markdown("**Output**")
                        st.markdown(output)
                    except Exception as exc:
                        st.error(str(exc))

    # ── Step 2a ───────────────────────────────────────────────────────────────
    elif step == "2a — Few-Shot Prompting":
        st.markdown(
            "Provide 2–3 input/output examples before your real question. "
            "The model learns format and style from the examples — no training, just context (Brown et al., 2020)."
        )
        st.markdown("**Example 1**")
        c1, c2 = st.columns(2)
        with c1:
            ex1_in  = st.text_area("Input", height=80, key="ex1_in")
        with c2:
            ex1_out = st.text_area("Output", height=80, key="ex1_out")

        st.markdown("**Example 2**")
        c1, c2 = st.columns(2)
        with c1:
            ex2_in  = st.text_area("Input", height=80, key="ex2_in")
        with c2:
            ex2_out = st.text_area("Output", height=80, key="ex2_out")

        text = st.text_area("Your actual question / topic", height=80, key="fewshot_text")

        if st.button("Run", type="primary", key="run_2a"):
            if not text.strip():
                st.warning("Enter your actual question first.")
            else:
                parts = []
                if ex1_in.strip() and ex1_out.strip():
                    parts.append(f"Input: {ex1_in}\nOutput: {ex1_out}")
                if ex2_in.strip() and ex2_out.strip():
                    parts.append(f"Input: {ex2_in}\nOutput: {ex2_out}")
                parts.append(f"Input: {text}\nOutput:")
                prompt = "\n\n".join(parts)
                with st.expander("Assembled prompt"):
                    st.code(prompt)
                with st.spinner("Calling model…"):
                    try:
                        resp = completion(
                            model=_model,
                            messages=[{"role": "user", "content": prompt}],
                        )
                        output = resp.choices[0].message.content
                        path = save_output("02a", prompt, output, topic=text[:80])
                        st.caption(f"Saved to `{path}`")
                        st.markdown("**Output**")
                        st.markdown(output)
                    except Exception as exc:
                        st.error(str(exc))

    # ── Step 2b ───────────────────────────────────────────────────────────────
    elif step == "2b — Prompt Template":
        st.markdown(
            "Same question as step 1, but split across two roles: "
            "a **system** message (who the model is, how it should behave) "
            "and a **user** message (the actual question). "
            "Try leaving some system fields blank to see what each one does."
        )
        st.markdown("**System message** — background instructions, not shown to the end user")
        c1, c2 = st.columns(2)
        with c1:
            persona     = st.text_input("Persona — who is the model?")
            instruction = st.text_input("Instruction — what should it do?")
            context     = st.text_input("Context — what background does it need?")
        with c2:
            data_format = st.text_input("Data format — what should the output look like?")
            audience    = st.text_input("Audience — who will read the output?")
            tone        = st.text_input("Tone — what tone should it use?")
        st.markdown("**User message** — the actual question")
        text = st.text_area("Your topic / question", height=80)

        if st.button("Run", type="primary", key="run_2b"):
            if not text.strip():
                st.warning("Enter a topic first.")
            else:
                parts = [p + "\n" for p in [persona, instruction, context, data_format, audience, tone] if p.strip()]
                system_message = "".join(parts)
                with st.expander("System message"):
                    st.code(system_message or "(empty)")
                with st.expander("User message"):
                    st.code(text)
                with st.spinner("Calling model…"):
                    try:
                        resp = completion(
                            model=_model,
                            messages=[
                                {"role": "system", "content": system_message},
                                {"role": "user",   "content": text},
                            ],
                        )
                        output = resp.choices[0].message.content
                        combined = f"SYSTEM:\n{system_message.strip()}\n\nUSER:\n{text}"
                        path = save_output("02b", combined, output, topic=text[:80])
                        st.caption(f"Saved to `{path}`")
                        st.markdown("**Output**")
                        st.markdown(output)
                    except Exception as exc:
                        st.error(str(exc))

    # ── Step 2c ───────────────────────────────────────────────────────────────
    elif step == "2c — Chain Prompting":
        st.markdown(
            "Two sequential API calls. Write the first prompt, run it, then write a second prompt "
            "that builds on the first output. The first output is appended to your second prompt automatically."
        )

        if "chain_output_1" not in st.session_state:
            st.session_state.chain_output_1 = None

        prompt_1 = st.text_area("First prompt", height=120)
        if st.button("Run first call", key="run_2c_1"):
            if not prompt_1.strip():
                st.warning("Enter the first prompt.")
            else:
                with st.spinner("Running first call…"):
                    try:
                        resp = completion(
                            model=_model,
                            messages=[{"role": "user", "content": prompt_1}],
                        )
                        st.session_state.chain_output_1 = resp.choices[0].message.content
                    except Exception as exc:
                        st.error(str(exc))

        if st.session_state.chain_output_1:
            st.markdown("**First call output**")
            st.info(st.session_state.chain_output_1)

            st.divider()
            prompt_2 = st.text_area(
                "Second prompt",
                height=120,
                help="The first call's output will be appended below your prompt automatically.",
            )
            if st.button("Run second call", type="primary", key="run_2c_2"):
                if not prompt_2.strip():
                    st.warning("Enter the second prompt.")
                else:
                    full_prompt_2 = f"{prompt_2}\n\n{st.session_state.chain_output_1}"
                    with st.expander("Assembled second prompt"):
                        st.code(full_prompt_2)
                    with st.spinner("Running second call…"):
                        try:
                            resp = completion(
                                model=_model,
                                messages=[{"role": "user", "content": full_prompt_2}],
                            )
                            output = resp.choices[0].message.content
                            combined = (
                                f"FIRST PROMPT:\n{prompt_1}\n\n"
                                f"FIRST OUTPUT:\n{st.session_state.chain_output_1}\n\n"
                                f"SECOND PROMPT:\n{full_prompt_2}"
                            )
                            path = save_output("02c", combined, output, topic=prompt_1[:80])
                            st.caption(f"Saved to `{path}`")
                            st.markdown("**Final output**")
                            st.markdown(output)
                        except Exception as exc:
                            st.error(str(exc))

    # ── Step 2d ───────────────────────────────────────────────────────────────
    elif step == "2d — Chain of Thought":
        st.markdown(
            "Same structure as 2b, with one extra component: an explicit reasoning instruction. "
            "Ask the model to think through the problem before giving its answer (Kojima et al., 2022)."
        )
        c1, c2 = st.columns(2)
        with c1:
            persona     = st.text_input("Persona — who is the model?", key="cot_persona")
            instruction = st.text_input("Instruction — what should it do?", key="cot_instruction")
            context     = st.text_input("Context — what background does it need?", key="cot_context")
        with c2:
            data_format = st.text_input("Data format — what should the output look like?", key="cot_format")
            audience    = st.text_input("Audience — who will read the output?", key="cot_audience")
            tone        = st.text_input("Tone — what tone should it use?", key="cot_tone")
        reasoning = st.text_input("Reasoning — how should the model think before answering?", key="cot_reasoning")
        text = st.text_area("Text / topic", height=80, key="cot_text")

        if st.button("Run", type="primary", key="run_2d"):
            if not text.strip():
                st.warning("Enter a topic first.")
            else:
                parts = [p + "\n" for p in [persona, instruction, context, data_format, audience, tone, reasoning] if p.strip()]
                query = "".join(parts) + f"Topic: {text}\n"
                with st.expander("Assembled prompt"):
                    st.code(query)
                with st.spinner("Calling model…"):
                    try:
                        resp = completion(
                            model=_model,
                            messages=[{"role": "user", "content": query}],
                        )
                        output = resp.choices[0].message.content
                        path = save_output("02d", query, output, topic=text[:80])
                        st.caption(f"Saved to `{path}`")
                        st.markdown("**Output**")
                        st.markdown(output)
                    except Exception as exc:
                        st.error(str(exc))

# ── Tab 2: Research Crew ──────────────────────────────────────────────────────

with tab_crew:
    st.caption("A sequential CrewAI crew: a researcher agent gathers facts, then an analyst agent writes the report.")

    topic = st.text_input("Topic", value="Artificial Intelligence in Healthcare")
    go = st.button("Run Crew", type="primary")

    if go:
        # Build the crew in the main thread — CrewAI's telemetry registers
        # signal handlers, which Python only permits on the main thread.
        try:
            crew = ResearchCrew().crew()
        except Exception as exc:
            st.error(f"Failed to initialize crew: {exc}")
            st.stop()
        events: queue.Queue = queue.Queue()
        thread = threading.Thread(target=run_crew, args=(crew, topic, events), daemon=True)
        thread.start()

        st.subheader("Live agent activity")
        log_container = st.container(border=True)
        final_output = None
        error_message = None

        while thread.is_alive() or not events.empty():
            try:
                label, detail = events.get(timeout=0.2)
            except queue.Empty:
                continue

            if label == "done":
                final_output = detail
                break
            if label == "error":
                error_message = detail
                break

            icon = ICONS.get(label, "•")
            with log_container:
                st.markdown(f"{icon} **{label.replace('_', ' ')}** — {detail}")

        if error_message:
            st.error(f"The crew hit an error: {error_message}")
        elif final_output:
            st.success("Crew finished!")
            st.subheader("Final report")
            st.markdown(final_output)
