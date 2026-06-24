# Sprint 4 — Dynamische Orchestrierung (Hierarchisch)

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/04-dynamic-orchestration.md)

Euer MVP aus Sprint 1 hat schon mehrere Agenten — aber ihr habt die Reihenfolge selbst festgelegt, in `tasks.yaml`, bevor irgendetwas lief. Das ist immer noch eine feste Pipeline, nur mit mehr als einem Agenten darin. Dieser Sprint dreht sich um etwas wirklich Anderes: Ein **Manager-Agent entscheidet zur Laufzeit**, welcher Worker-Agent welchen Task übernimmt und in welcher Reihenfolge, statt dass ihr die Sequenz hartcodiert. Das ist das eigentliche "Multi-Agenten"-Pattern — Zusammenarbeit, die dynamisch ist, nicht nur mehrzählig.

Kompromiss: flexibler, aber weniger vorhersagbar und teurer (der Manager macht zusätzliche LLM-Aufrufe, um zu delegieren).

> Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

![AutoGen-Architektur: konversationsfähige, anpassbare Agenten, die zur Lösung von Aufgaben kommunizieren, in Joint-Chat- oder hierarchischen Chat-Mustern, gezeigt bei der Lösung einer Datenplot-Aufgabe durch Mehrturn-Konversation](../assets/autogen-wu2023-fig1.png)
*Abbildung 1 aus Wu et al. (2023): AutoGen-Agenten sind konversationsfähig und anpassbar, können in flexiblen Mustern einschließlich hierarchischem Chat kommunizieren und Menschen einbeziehen. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

## In diesem Repo

Aktuell `process=Process.sequential` mit Agenten in fester Reihenfolge ([crew.py:51](../../src/research_crew/crew.py#L51)). Um hierarchisch zu werden, braucht CrewAI entweder `manager_llm` oder `manager_agent`:

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.hierarchical,
    manager_llm="groq/llama-3.3-70b-versatile",
    verbose=True,
)
```

Im hierarchischen Modus entfernt ihr außerdem das feste `agent:`-Feld aus jedem Task in `tasks.yaml` — der Manager weist Tasks dynamisch Agenten zu, statt eine hartcodierte Zuordnung zu lesen.

## Aufgabe

1. **Sprint Planning**: Öffnet 1–2 GitHub-Issues als User Stories, gelabelt `epic:orchestration`, für die Rolle des neuen Agenten und für die Prozesswahl selbst.
2. Fügt eurer Crew einen dritten Agenten hinzu — eine Rolle, die euren ersten beiden wirklich fehlt, nicht eine, die nur erfunden wurde, um auf drei zu kommen.
3. **Entscheidet bewusst**: Profitiert euer Anwendungsfall tatsächlich davon, dass ein Manager dynamisch delegiert, oder würde ein dritter Agent in einem festen sequentiellen Slot genauso gut funktionieren? Probiert zuerst die Variante, von der ihr nicht erwartet, dass sie gewinnt, damit ihr nicht nur bestätigt, was ihr schon angenommen habt.
4. Falls ihr hierarchisch geht: Stellt `process` um, fügt `manager_llm` hinzu, und entfernt die festen `agent:`-Zuweisungen aus `tasks.yaml`. Führt es aus und beobachtet die ausführlichen Logs — welchen Agenten wählt der Manager für jeden Task, und entspricht das dem, was ihr von der Rolle jedes Agenten erwarten würdet?
5. Aktualisiert den Architektur-Abschnitt von `DESIGN.md` (Prozess, Agenten) und Guardrails/Vertrauensmechanismen, falls ihr Validierung hinzugefügt habt.
6. Bevor ihr das als fertig betrachtet, beantwortet in `DESIGN.md`: Falls hierarchisch — wofür optimiert der Manager beim Delegieren tatsächlich, und könnte das von dem abweichen, was ihr wollt? Falls sequentiell geblieben — was hätte hierarchisch gebracht, und warum war es den Aufwand nicht wert? Was trägt der dritte Agent bei, das die ersten beiden nicht schon zusammen leisten könnten — ist seine Rolle wirklich nötig, oder teilt sie nur Arbeit auf, die keine Teilung gebraucht hätte?

## Zusatzaufgabe

Falls ihr mit `manager_llm` hierarchisch gegangen seid, probiert stattdessen `manager_agent` — definiert euren eigenen dedizierten Manager-`Agent` mit einer expliziten Rolle, und vergleicht, ob sich die Delegationsentscheidungen ändern.
