# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../README.md)

Das sind die praktischen Schritte zu **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**. Die Vorlesungstheorie wird über Folien im Kurs vermittelt; diese Reihe ist die praktische Begleitung dazu — und ist zugleich die benotete Team-Aufgabe, kein separates Ding daneben.

Das Prinzip ist einfach: Ihr führt fünf Versionen derselben Sache mit demselben Thema aus, wobei jede Version eine Schicht hinzufügt. Dann bewertet ihr, was jede Schicht tatsächlich verändert hat. Das Lernen entsteht aus dem Vergleich, nicht aus einem einzelnen Schritt.

Ihr solltet [Run the crew](../../README.md#getting-started--choose-one-option) in **eurem eigenen Team-Repo** funktionsfähig haben, bevor Schritt 1 beginnt — siehe den Abschnitt ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students), falls ihr das noch nicht habt.

## Schritte

| # | Titel | Was hinzukommt |
| --- | --- | --- |
| [1](01-simple-prompting.md) | Einfaches Prompting | Der bloße API-Aufruf — eure Ausgangsbasis (`src/exercises/`) |
| [2](02-prompt-template.md) | Prompt-Vorlage | Eine Rolle + Ausgabeformat, derselbe Aufruf (`src/exercises/`) |
| [3](03-single-agent.md) | Einzelner Agent | Ein Agent in `agents.yaml` + `crew.py` *(Zwischenabgabe fällig)* |
| [4](04-multi-agent.md) | Multi-Agent | Zwei Agenten mit Task-Verkettung via `context:` |
| [5](05-rag-and-tools.md) | RAG + Tools | `SerperDevTool` + Knowledge-Source hinzufügen *(Abschlussabgabe fällig)* |

Alle fünf Schritte verwenden dasselbe **Thema** — ihr wählt es einmal bei Schritt 1 und behaltet es. Das primäre Abgabeprodukt ist `EVALUATION.md`: ein schrittweiser Vergleich, was sich verändert hat und warum das für euren Anwendungsfall wichtig ist (oder nicht).

Was bewertet wird, das Abgabepaket, Team-Setup und Vorlagen (`EVALUATION.md`, `TEAM.md`, Peer Evaluation) sind im [Überblick zur Aufgabe](assignment-overview.md) beschrieben (Deutsch / [English](../en/assignment-overview.md)).

## Selbstständig weiterlernen

Der "Hintergrund"-Abschnitt jedes Schritts gibt euch gerade genug, um das Konzept einzuordnen — für alles, was CrewAI selbst über das hinaus kann, was die Demo-Crew in diesem Repo zeigt, geht direkt zur Quelle:
- [CrewAI-Dokumentation](https://docs.crewai.com) — die vollständige Konzept-Referenz (Agents, Tasks, Prozesse, Tools, Memory, Knowledge, Flows) und der [Quickstart](https://docs.crewai.com/en/quickstart)
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) (DeepLearning.AI) — ein kurzer Videokurs, gehalten vom Gründer von CrewAI; kostenlos während der Beta-Phase der DeepLearning.AI-Plattform, bleibt möglicherweise nicht dauerhaft kostenlos

## Für Lehrende

Studierende arbeiten in ihrem eigenen Team-Repo (eines pro Team, aus dieser Vorlage unter eurer Kurs-Organisation erzeugt) — siehe ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students) für den studierendenseitigen Einschreibe-Ablauf, und den Abschnitt "Für Lehrende" im [Überblick zur Aufgabe](assignment-overview.md#für-lehrende) für die vollständige Einrichtung und den automatisierten Anmelde-Workflow. Musterlösungen sind bewusst nicht enthalten; bewertet Abgaben, indem ihr die gemergten Sprint-Pull-Requests jedes Teams direkt prüft.
