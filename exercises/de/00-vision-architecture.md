# Sprint 0 — Vision & Architektur

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/00-vision-architecture.md)

Ein agentisches *Framework* gibt euch wiederverwendbare Bausteine, damit ihr die Denken-Handeln-Beobachten-Schleife nicht selbst von Hand bauen müsst. Die vier Kern-Abstraktionen von CrewAI:

- **Agent** — Rolle, Ziel, Backstory, LLM, Tools
- **Task** — eine Beschreibung, das erwartete Ergebnis und welcher Agent dafür zuständig ist
- **Crew** — eine Sammlung von Agenten + Tasks + ein Prozess für deren Ausführung
- **Process** — die Orchestrierungsstrategie (Sprints 1 und 4 behandeln die beiden wichtigsten)

Diese Aufteilung ist eine konkrete Umsetzung eines allgemeineren Musters aus der LLM-Agenten-Literatur:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Vereinheitlichtes Framework für die Architektur von LLM-basierten autonomen Agenten: Profile, Memory, Planning, Action Module](../assets/agentsurvey-wang2023-fig2.png)
*Abbildung 2 aus Wang et al. (2023): ein vereinheitlichtes Framework für LLM-Agenten-Architektur mit den Modulen Profile, Memory, Planning und Action. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

Übertragen auf CrewAI: das `role`/`goal`/`backstory` eines `Agent` in `agents.yaml` ist das **Profile**-Modul; `tools` plus die Task-Schleife ist das **Action**-Modul.

Davor steht aber der eigentlich schwierige Teil: zu entscheiden, *für wen* diese Crew da ist und *was* sie tun soll — das ist ein Entwurfsproblem, kein Programmierproblem. Zwei Grundlagenwerke dafür:

> Simon, H. A. (1969). *The Sciences of the Artificial*. MIT Press.

> Brown, T. (2008). *Design Thinking*. Harvard Business Review, 86(6), 84–92.

## In diesem Repo

Öffnet [src/research_crew/crew.py](../../src/research_crew/crew.py) von oben bis unten — es ist bewusst kurz gehalten. Ordnet jeden Teil dem Konzept zu:

| Konzept | Wo |
| --- | --- |
| `@CrewBase`-Klasse | [crew.py:10](../../src/research_crew/crew.py#L10) — markiert `ResearchCrew` als CrewAI-Projekt, lädt automatisch die YAML-Konfigurationen |
| Agenten | Methoden `researcher` und `analyst`, jeweils mit `@agent` dekoriert |
| Tasks | `research_task` und `analysis_task`, jeweils mit `@task` dekoriert |
| Crew | die Methode `crew()`, mit `@crew` dekoriert, fügt alles zusammen |
| Konfigurationsgesteuerte Rollen | [config/agents.yaml](../../src/research_crew/config/agents.yaml) — Rolle/Ziel/Backstory leben in YAML, nicht in Python |
| Konfigurationsgesteuerte Tasks | [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) — Beschreibung/erwartetes Ergebnis/Agentenzuweisung |

Beachtet: Das Ziel der Demo wurde nirgendwo explizit aufgeschrieben — `researcher` und `analyst` existieren, weil dieser Split generell nützlich für "ein Thema recherchieren, dann darüber berichten" ist, nicht weil jemand vorher mit einem konkreten Stakeholder empathisiert hat. Genau diese Lücke soll dieser Sprint nicht wiederholen.

## Aufgabe

Hier wählt ihr euren Anwendungsfall (siehe die [Tabelle im Haupt-README](../../README.md#use-cases-to-pick-from)) und beginnt, eure eigene Crew zu entwerfen — nicht das `researcher`/`analyst`-Paar umbenannt.

1. **Sprint Planning**: Öffnet 2–3 GitHub-Issues als User Stories (Format in den [Vorlagen für die Aufgabe](assignment-templates.md)), gelabelt `epic:vision`.
2. **Für wen ist das?** Benennt den tatsächlichen Stakeholder des Ergebnisses eurer Crew — nicht "Nutzer" im Abstrakten, sondern eine konkrete Rolle oder Person. Was braucht *diese Person* davon, und was würde das Ergebnis für sie unbrauchbar machen, selbst wenn es technisch korrekt ist?
3. **Was ist das Problem, in ihren Worten?** Schreibt ein bis zwei Sätze, die das Ziel aus der Perspektive dieses Stakeholders formulieren, nicht aus der Perspektive der Technologie. Das kommt in den Überblick-Abschnitt von `DESIGN.md`.
4. **Bevor ihr euch auf einen Entwurf festlegt, skizziert mindestens zwei verschiedene Agenten-Rollensplits** für euren Anwendungsfall — nicht nur den Vorschlag aus der Anwendungsfall-Tabelle des READMEs. Schreibt auf, wie jede Version aussehen würde (wie viele Agenten, wer was übernimmt), bevor ihr euch entscheidet.
5. **Entwerft die Agenten und Tasks** für die Version, für die ihr euch entscheidet: Rollen, Ziele, Backstories, und wie Tasks voneinander abhängen. Füllt den Architektur-Abschnitt von `DESIGN.md` (Tabellen Agenten und Tasks) aus.
6. Bevor ihr das als fertig betrachtet, beantwortet direkt in `DESIGN.md`: Was braucht jeder Agent tatsächlich vom anderen, um seine Aufgabe zu erfüllen — und was passiert, wenn die Ausgabe eines Agenten subtil falsch ist, merkt der nächste Agent das überhaupt, oder vertraut er blind? Was ist das stärkste Argument dafür, dass der in Schritt 4 *verworfene* Rollensplit eigentlich besser gewesen wäre? Wie würdet ihr merken, dass euer aktueller Split falsch ist, statt nur anders als der von jemand anderem?

## Zusatzaufgabe

Findet jemanden außerhalb eures Teams (Kommiliton*in, Freund*in), der*die plausibel eurem gewählten Stakeholder ähnelt, und stellt eine Frage: "Würdest du einen Report, den diese Crew erstellt, tatsächlich nutzen?" Schreibt die Antwort ungefiltert in `DESIGN.md` — auch wenn es nicht das ist, was ihr hören wolltet.
