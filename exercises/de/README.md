# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../README.md)

Das sind die praktischen Schritte zu **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**. Die Vorlesungstheorie wird über Folien im Kurs vermittelt; diese Reihe ist die praktische Begleitung dazu — und ist zugleich die benotete Team-Aufgabe, kein separates Ding daneben.

Das Prinzip ist einfach: Ihr führt eine Abfolge von Versionen derselben Sache mit demselben Thema aus, wobei jede Version eine Schicht hinzufügt. Dann bewertet ihr, was jede Schicht tatsächlich verändert hat. Das Lernen entsteht aus dem Vergleich, nicht aus einem einzelnen Schritt.

Ihr solltet [Run the crew](../../README.md#getting-started--choose-one-option) in **eurem eigenen Team-Repo** funktionsfähig haben, bevor Schritt 02 beginnt — siehe den Abschnitt ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students), falls ihr das noch nicht habt. Falls Git, `uv` oder Jupyter für euch neu sind, startet zuerst mit [Schritt 00](../en/step_00_setup_and_python_basics.ipynb).

**Hinweis:** Alle Notebooks unten sind aktuell nur auf Englisch verfügbar (Code-Kommentare, Markdown-Zellen, alles) — es gibt keine deutsche Übersetzung der Notebooks selbst.

## Schritte

| # | Titel | Was hinzukommt |
| --- | --- | --- |
| [00](../en/step_00_setup_and_python_basics.ipynb) | Setup & Python-Grundlagen | Git/GitHub, `uv` und Jupyter *(optional)* |
| [01](../en/step_01_test_setup_and_first_llm_call.ipynb) | Setup testen & erster LLM-Aufruf | Prüft, ob eure Umgebung funktioniert, Projekt-Tour, euer erster `crewai.LLM`-Aufruf *(optional)* |
| [02](../en/step_02_zero_shot_prompting.ipynb) | Zero-Shot-Prompting | Der bloße API-Aufruf — eure Ausgangsbasis |
| [03](../en/step_03_few_shot.ipynb) | Few-Shot-Prompting | 2–3 Beispiele vor der eigentlichen Frage |
| [04](../en/step_04_prompt_template.ipynb) | Prompt-Vorlage | Eine Rolle + Ausgabeformat, derselbe Aufruf |
| [05](../en/step_05_chain_prompting.ipynb) | Chain Prompting | Zwei aufeinanderfolgende Aufrufe, einer speist den nächsten |
| [06](../en/step_06_chain_of_thought.ipynb) | Chain of Thought | Explizites Schlussfolgern vor der finalen Antwort |
| [07](../en/step_07_tree_of_thought.ipynb) | Tree of Thought | Mehrere Gedankenpfade parallel erkundet |
| [08](../en/step_08_intro_to_crewai.ipynb) | Einführung in CrewAI | Was CrewAI ist, `Agent`/`Task`/`Crew`/`Process` und eingebautes Memory — aufgebaut ausgehend von einem einfachen LLM-Aufruf |
| [09](../en/step_09_single_agent.ipynb) | Einzelner Agent | Ein eigenständiger `Agent`, kein Framework-Projekt nötig *(Zwischenpräsentation)* |
| [10](../en/step_10_memory.ipynb) | Memory | Erinnerung über getrennte `kickoff()`-Aufrufe hinweg |
| [11](../en/step_11_tools.ipynb) | Tools | Live-Websuche über ein CrewAI-Tool |
| [12](../en/step_12_mcp.ipynb) | MCP | Ein externer Tool-Server über das Model Context Protocol |
| [13](../en/step_13_rag.ipynb) | RAG | Retrieval aus eurer eigenen Knowledge-Source |
| [14](../en/step_14_multi_agent_seq.ipynb) | Multi-Agent (Sequenziell) | Zwei Agenten, verkettet durch Weitergabe der Ausgabe *(Abschlusspräsentation)* |
| [15](../en/step_15_multi_agent_hierarchical.ipynb) | Multi-Agent (Hierarchisch) | Dieselben zwei Agenten, zur Laufzeit von einem Manager delegiert statt im Code fest verdrahtet *(optional)* |
| [16](../en/step_16_design_patterns.ipynb) | Agentic Workflow Design Patterns | Anthropics fünf Workflow-Muster (Chaining, Routing, Parallelisierung, Orchestrator-Workers, Evaluator-Optimizer), jedes auf einen funktionierenden CrewAI-Mechanismus abgebildet *(optional)* |
| [17](../en/step_17_evaluation_harness.ipynb) | Geschwindigkeit, Genauigkeit & Kosten evaluieren | Ein wiederverwendbarer Test-Harness misst Latenz, Token-Kosten und eine per LLM bewertete Goal Completion Rate — Grundlage für `REPORT.md` Abschnitt 5.2 *(optional)* |

Die Schritte 02–14 verwenden dasselbe **Thema** — ihr wählt es einmal bei Schritt 02 und behaltet es. Diese Notebooks sind individuelle Übung, keine Team-Abgabe; in `REPORT.md` hält euer Team dann den Entwurf des gemeinsam gebauten Agenten fest — Architektur, Implementierung, Evaluierung — als Vorbereitung für eure Zwischen- und Abschlusspräsentation. Jede*r Studierende schreibt und reicht zusätzlich einen eigenen Ethik-Report ein. Die Schritte 15–17 sind optional und nicht Teil der bewerteten Aufgabe.

Was bewertet wird, das Abgabepaket, Team-Setup und Vorlagen (`REPORT.md`, `TEAM.md`, Ethik-Report) sind im [Überblick zur Aufgabe](../../team_assignment/de/assignment-overview.md) beschrieben (Deutsch / [English](../../team_assignment/en/assignment-overview.md)).

## Selbstständig weiterlernen

Der "Hintergrund"-Abschnitt jedes Schritts gibt euch gerade genug, um das Konzept einzuordnen — für alles, was CrewAI selbst über das hinaus kann, was die Demo-Crew in diesem Repo zeigt, geht direkt zur Quelle:
- [CrewAI-Dokumentation](https://docs.crewai.com) — die vollständige Konzept-Referenz (Agents, Tasks, Prozesse, Tools, Memory, Knowledge, Flows) und der [Quickstart](https://docs.crewai.com/en/quickstart)
- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) (DeepLearning.AI) — ein kurzer Videokurs, gehalten vom Gründer von CrewAI; kostenlos während der Beta-Phase der DeepLearning.AI-Plattform, bleibt möglicherweise nicht dauerhaft kostenlos

## Für Lehrende

Studierende arbeiten in ihrem eigenen Team-Repo (eines pro Team, aus dieser Vorlage unter eurer Kurs-Organisation erzeugt) — siehe ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students) für den studierendenseitigen Einschreibe-Ablauf, und den Abschnitt "Für Lehrende" im [Überblick zur Aufgabe](../../team_assignment/de/assignment-overview.md#für-lehrende) für die vollständige Einrichtung und den automatisierten Anmelde-Workflow. Musterlösungen sind bewusst nicht enthalten; bewertet Abgaben, indem ihr die gemergten Sprint-Pull-Requests jedes Teams direkt prüft.
