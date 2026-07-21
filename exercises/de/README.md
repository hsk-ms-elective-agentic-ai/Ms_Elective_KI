# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../README.md)

Das sind die praktischen Schritte zu **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**. Die Vorlesungstheorie wird über Folien im Kurs vermittelt; diese Reihe ist die praktische Begleitung dazu — und ist zugleich die benotete Team-Aufgabe, kein separates Ding daneben.

Das Prinzip ist einfach: Ihr führt fünf Versionen derselben Sache mit demselben Thema aus, wobei jede Version eine Schicht hinzufügt. Dann bewertet ihr, was jede Schicht tatsächlich verändert hat. Das Lernen entsteht aus dem Vergleich, nicht aus einem einzelnen Schritt.

Ihr solltet [Run the crew](../../README.md#getting-started--choose-one-option) in **eurem eigenen Team-Repo** funktionsfähig haben, bevor Schritt 1 beginnt — siehe den Abschnitt ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students), falls ihr das noch nicht habt. Falls Git, `uv`, Jupyter oder Python selbst für euch neu sind, startet zuerst mit [Schritt 0](../en/step_00_setup_and_python_basics.ipynb).

**Hinweis:** Alle Notebooks unten sind aktuell nur auf Englisch verfügbar (Code-Kommentare, Markdown-Zellen, alles) — es gibt keine deutsche Übersetzung der Notebooks selbst.

## Schritte

| # | Titel | Was hinzukommt |
| --- | --- | --- |
| [0](../en/step_00_setup_and_python_basics.ipynb) | Setup & Python-Grundlagen | Git/GitHub, `uv`, Jupyter und eine Python-Auffrischung *(optional)* |
| [0b](../en/step_00b_test_setup_and_first_agent.ipynb) | Setup testen & erster Agent | Prüft, ob eure Umgebung funktioniert, Projekt-Tour, ein eigenständiger `Agent` *(optional)* |
| [1](../en/step_01_zero_shot_prompting.ipynb) | Zero-Shot-Prompting | Der bloße API-Aufruf — eure Ausgangsbasis |
| [2](../en/step_02a_few_shot.ipynb) | Prompt-Vorlage | Eine Rolle + Ausgabeformat, derselbe Aufruf (5 Notebooks) |
| [3](../en/step_03_05_agents.ipynb) | Einzelner Agent | Ein Agent in `agents.yaml` + `crew.py` *(Zwischenabgabe fällig)* |
| [4](../en/step_03_05_agents.ipynb) | Multi-Agent | Zwei Agenten mit Task-Verkettung via `context:` |
| [5](../en/step_03_05_agents.ipynb) | RAG + Tools | `SerperDevTool` + Knowledge-Source hinzufügen *(Abschlussabgabe fällig)* |

Alle fünf Schritte verwenden dasselbe **Thema** — ihr wählt es einmal bei Schritt 1 und behaltet es. Das primäre Abgabeprodukt ist `EVALUATION.md`: ein schrittweiser Vergleich, was sich verändert hat und warum das für euren Anwendungsfall wichtig ist (oder nicht).

Was bewertet wird, das Abgabepaket, Team-Setup und Vorlagen (`EVALUATION.md`, `TEAM.md`, Peer Evaluation) sind im [Überblick zur Aufgabe](../../team_assignment/de/assignment-overview.md) beschrieben (Deutsch / [English](../../team_assignment/en/assignment-overview.md)).

## Selbstständig weiterlernen

Der "Hintergrund"-Abschnitt jedes Schritts gibt euch gerade genug, um das Konzept einzuordnen — für alles, was CrewAI selbst über das hinaus kann, was die Demo-Crew in diesem Repo zeigt, geht direkt zur Quelle:
- [CrewAI-Dokumentation](https://docs.crewai.com) — die vollständige Konzept-Referenz (Agents, Tasks, Prozesse, Tools, Memory, Knowledge, Flows) und der [Quickstart](https://docs.crewai.com/en/quickstart)
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) (DeepLearning.AI) — ein kurzer Videokurs, gehalten vom Gründer von CrewAI; kostenlos während der Beta-Phase der DeepLearning.AI-Plattform, bleibt möglicherweise nicht dauerhaft kostenlos

## Für Lehrende

Studierende arbeiten in ihrem eigenen Team-Repo (eines pro Team, aus dieser Vorlage unter eurer Kurs-Organisation erzeugt) — siehe ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students) für den studierendenseitigen Einschreibe-Ablauf, und den Abschnitt "Für Lehrende" im [Überblick zur Aufgabe](../../team_assignment/de/assignment-overview.md#für-lehrende) für die vollständige Einrichtung und den automatisierten Anmelde-Workflow. Musterlösungen sind bewusst nicht enthalten; bewertet Abgaben, indem ihr die gemergten Sprint-Pull-Requests jedes Teams direkt prüft.
