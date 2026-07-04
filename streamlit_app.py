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

ICONS = {
    "task_started": "📋",
    "task_completed": "✅",
    "agent_started": "🤖",
    "agent_completed": "✔️",
    "tool_started": "🔧",
    "tool_finished": "🔧✅",
    "tool_error": "⚠️",
}


def run_crew(topic: str, events: queue.Queue) -> None:
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
            result = ResearchCrew().crew().kickoff(inputs={"topic": topic})
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
            "1 — Simple Prompting",
            "2a — Prompt Template",
            "2b — Chain of Thought",
            "2c — Chain Prompting",
        ],
        horizontal=True,
    )

    st.divider()

    # ── Step 1 ────────────────────────────────────────────────────────────────
    if step == "1 — Simple Prompting":
        st.markdown("One message, one response. No structure, no persona — a raw question to the model.")
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
                        st.markdown("**Output**")
                        st.markdown(resp.choices[0].message.content)
                    except Exception as exc:
                        st.error(str(exc))

    # ── Step 2a ───────────────────────────────────────────────────────────────
    elif step == "2a — Prompt Template":
        st.markdown(
            "Same API call as step 1, but the prompt is broken into named components. "
            "Try leaving some blank to see what each one actually does."
        )
        c1, c2 = st.columns(2)
        with c1:
            persona     = st.text_input("Persona — who is the model?")
            instruction = st.text_input("Instruction — what should it do?")
            context     = st.text_input("Context — what background does it need?")
        with c2:
            data_format = st.text_input("Data format — what should the output look like?")
            audience    = st.text_input("Audience — who will read the output?")
            tone        = st.text_input("Tone — what tone should it use?")
        text = st.text_area("Text / topic", height=80)

        if st.button("Run", type="primary", key="run_2a"):
            if not text.strip():
                st.warning("Enter a topic first.")
            else:
                parts = [p + "\n" for p in [persona, instruction, context, data_format, audience, tone] if p.strip()]
                query = "".join(parts) + f"Topic: {text}\n"
                with st.expander("Assembled prompt"):
                    st.code(query)
                with st.spinner("Calling model…"):
                    try:
                        resp = completion(
                            model=_model,
                            messages=[{"role": "user", "content": query}],
                        )
                        st.markdown("**Output**")
                        st.markdown(resp.choices[0].message.content)
                    except Exception as exc:
                        st.error(str(exc))

    # ── Step 2b ───────────────────────────────────────────────────────────────
    elif step == "2b — Chain of Thought":
        st.markdown(
            "Same structure as 2a, with one extra component: an explicit reasoning instruction. "
            "Ask the model to think through the problem before giving its answer."
        )
        c1, c2 = st.columns(2)
        with c1:
            persona     = st.text_input("Persona — who is the model?")
            instruction = st.text_input("Instruction — what should it do?")
            context     = st.text_input("Context — what background does it need?")
        with c2:
            data_format = st.text_input("Data format — what should the output look like?")
            audience    = st.text_input("Audience — who will read the output?")
            tone        = st.text_input("Tone — what tone should it use?")
        reasoning = st.text_input("Reasoning — how should the model think before answering?")
        text = st.text_area("Text / topic", height=80)

        if st.button("Run", type="primary", key="run_2b"):
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
                        st.markdown("**Output**")
                        st.markdown(resp.choices[0].message.content)
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
                            st.markdown("**Final output**")
                            st.markdown(resp.choices[0].message.content)
                        except Exception as exc:
                            st.error(str(exc))

# ── Tab 2: Research Crew ──────────────────────────────────────────────────────

with tab_crew:
    st.caption("A sequential CrewAI crew: a researcher agent gathers facts, then an analyst agent writes the report.")

    topic = st.text_input("Topic", value="Artificial Intelligence in Healthcare")
    go = st.button("Run Crew", type="primary")

    if go:
        events: queue.Queue = queue.Queue()
        thread = threading.Thread(target=run_crew, args=(topic, events), daemon=True)
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
