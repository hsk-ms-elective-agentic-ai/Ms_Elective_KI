"""Live, browser-based view of the research_crew agents at work.

Run with: uv run streamlit run streamlit_app.py
"""
import queue
import threading

import streamlit as st
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


st.set_page_config(page_title="Research Crew", page_icon="🧑‍🔬", layout="wide")
st.title("🧑‍🔬 Research Crew — Agentic AI Demo")
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
