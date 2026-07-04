# Schritt 3 — Einzelner Agent

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/03-single-agent.md)

Verpackt den Prompt in einen CrewAI-`Agent` und einen `Task`. `role`, `goal` und `backstory` sind unter der Haube immer noch ein System-Prompt — CrewAI setzt ihn aus diesen drei Feldern für euch zusammen — und ein `Task` ist immer noch eine nutzerseitige Anweisung. Was das Framework hinzufügt, ist die Schleife: Der Agent kann in mehreren Schritten denken, bevor er eine Ausgabe produziert, Tools aufrufen (Schritt 5) und bei Fehlern erneut versuchen. Ein Agent, ein Task.

## Hintergrund

Die Beobachtung, dass LLM-basierte Agenten von einer expliziten Modulstruktur profitieren — Profil (wer dieser Agent ist), Gedächtnis (worauf er zugreifen kann), Planung (wie er Arbeit aufteilt) und Handlung (was er tun kann) — wurde systematisiert in:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Einheitliches Framework für LLM-basierte autonome Agenten: Profil-, Gedächtnis-, Planungs- und Handlungsmodule](../assets/agentsurvey-wang2023-fig2.png)
*Abbildung 2 aus Wang et al. (2023): Einheitliche LLM-Agenten-Architektur. Reproduziert für Bildungszwecke in diesem Kurs.*

In CrewAI-Begriffen: `role`/`goal`/`backstory` entsprechen dem **Profil**-Modul; `tools` und die Task-Schleife dem **Handlungs**-Modul.

## Der Code

Öffnet [src/exercises/step_03_single_agent.py](../../src/exercises/step_03_single_agent.py). Ordnet die Teile den Konzepten zu:

| Code | Was es ist |
| --- | --- |
| `Agent(role=..., goal=..., backstory=...)` | Das Profil-Modul — von CrewAI zu einem System-Prompt zusammengesetzt |
| `Task(description=..., expected_output=...)` | Der Auftrag, an dem der Agent arbeitet |
| `Crew(agents=[...], tasks=[...])` | Die Laufzeitumgebung, die die Schleife ausführt |
| `verbose=True` | Zeigt das interne Reasoning des Agenten — lest das, es ist der Kernpunkt |

## Aufgabe

1. Setzt `TOPIC` auf dasselbe Thema wie Schritte 1 und 2.

2. Führt es aus:
   ```bash
   uv run python src/exercises/step_03_single_agent.py
   ```

3. Beobachtet die verbose-Ausgabe sorgfältig — das ist der erste Schritt, bei dem ihr das *interne Reasoning* des Modells sehen könnt, nicht nur seine finale Antwort. Notiert:
   - Teilt der Agent die Aufgabe in Teilschritte auf?
   - Sieht die finale Antwort anders aus als das, was Schritt 2 produziert hat? Inwiefern genau?

4. **Experimentiert**: ändert `backstory` auf etwas Minimales (ein Satz) vs. Ausführliches (drei Sätze mit konkreter Spezialisierung). Verändert die Tiefe der backstory die Ausgabequalität, oder nutzt das Modell hauptsächlich `role` und `goal`?

5. Füllt den **Schritt 3**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Schaut euch im verbose-Log die "Final Answer" zusammen mit dem zwischenzeitlichen Reasoning des Agenten an. Findet eine Stelle, an der das Reasoning und die Schlussfolgerung leicht inkonsistent sind — wo der Agent auf etwas schließt und dann etwas leicht anderes schreibt. Was sagt euch das darüber, wie sehr man der Chain-of-Thought vertrauen kann?

---

**→ Die Zwischenabgabe ist nach diesem Schritt fällig.** Gebt den Zustand von `main` nach dem Mergen von `sprint-3` ab. Seht [Überblick zur Aufgabe](assignment-overview.md) für genaue Erwartungen.
