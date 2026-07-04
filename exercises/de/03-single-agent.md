# Schritt 3 — Einzelner Agent

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/03-single-agent.md)

Wechselt von einem handgeschriebenen Prompt zu einem CrewAI-`Agent` und einem `Task`. `role`, `goal` und `backstory` in `agents.yaml` sind unter der Haube immer noch ein System-Prompt — CrewAI setzt ihn aus diesen drei Feldern für euch zusammen. Was das Framework hinzufügt, ist die Schleife: Der Agent denkt in mehreren Schritten, bevor er eine Ausgabe produziert, kann Tools aufrufen (Schritt 5) und bei Fehlern erneut versuchen. Ein Agent, ein Task.

## Hintergrund

Die grundlegende Schleife, die einen Agenten zu einem Agenten macht — abwechselndes Reasoning über den nächsten Schritt und Ausführen einer Aktion (Tool aufrufen, Ergebnis lesen, Plan aktualisieren) — wurde eingeführt in:

> Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

ReAct (Reason + Act) ist das Muster, dem CrewAI-Agenten folgen: Das Modell denkt („Ich muss X finden"), handelt (ruft ein Tool auf), beobachtet das Ergebnis, denkt erneut nach und wiederholt dies, bis es eine finale Antwort produzieren kann. Das trennt einen Agenten von einem einzelnen Prompt-Aufruf — die Schleife.

Die weitergehende Beobachtung, dass LLM-basierte Agenten von einer expliziten Modulstruktur profitieren — Profil, Gedächtnis, Planung, Handlung — wurde systematisiert in:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Einheitliches Framework für LLM-basierte autonome Agenten: Profil-, Gedächtnis-, Planungs- und Handlungsmodule](../assets/agentsurvey-wang2023-fig2.png)
*Abbildung 2 aus Wang et al. (2023). Reproduziert für Bildungszwecke in diesem Kurs.*

In CrewAI-Begriffen: `role`/`goal`/`backstory` in `agents.yaml` = **Profil**; `tools` + die ReAct-Task-Schleife = **Handlung**.

## In diesem Repo

| Datei | Was ihr ändert |
| --- | --- |
| [src/research_crew/config/agents.yaml](../../src/research_crew/config/agents.yaml) | Definiert EINEN Agenten für euer Thema — role, goal, backstory |
| [src/research_crew/config/tasks.yaml](../../src/research_crew/config/tasks.yaml) | Definiert EINEN Task — description, expected_output, agent |
| [src/research_crew/crew.py](../../src/research_crew/crew.py) | Behaltet nur eine `@agent`- und eine `@task`-Methode |

Das Template hat bereits zwei Agenten (`researcher` und `analyst`). Für diesen Schritt reduziert auf einen — kommentiert den Analysten und seinen Task aus oder entfernt sie.

## Aufgabe

1. Öffnet `agents.yaml`. Ersetzt den vorhandenen Agenten durch euren eigenen: gebt ihm eine `role`, ein `goal` und eine `backstory`, die zu eurem Thema passen.

2. Öffnet `tasks.yaml`. Ersetzt den vorhandenen Task durch einen, der zu eurem Agenten und Thema passt: schreibt eine `description` und einen `expected_output`.

3. Behaltet in `crew.py` nur eine `@agent`- und eine `@task`-Methode (entfernt oder kommentiert den Analysten aus).

4. Führt aus:
   ```bash
   uv run research_crew
   ```

5. Lest die verbose-Ausgabe — das ist das erste Mal, dass ihr das interne Reasoning des Agenten sehen könnt, nicht nur die finale Antwort. Teilt der Agent die Aufgabe in Teilschritte auf? Fühlt sich die Ausgabe anders an als das, was Schritt 2 produziert hat?

6. Füllt den **Schritt 3**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Schaut euch im verbose-Log die "Final Answer" zusammen mit dem zwischenzeitlichen Reasoning an. Findet eine Stelle, an der Reasoning und Schlussfolgerung leicht inkonsistent sind. Was sagt euch das über das Vertrauen in Chain-of-Thought?

---

**→ Die Zwischenabgabe ist nach diesem Schritt fällig.** Gebt den Zustand von `main` nach dem Mergen von `sprint-3` ab. Seht [Überblick zur Aufgabe](assignment-overview.md) für genaue Erwartungen.
