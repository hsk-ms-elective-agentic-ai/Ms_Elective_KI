# Sprint 2 — Tools

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/02-tools.md)

Tools verwandeln ein LLM von "erzeugt plausiblen Text" in "kann tatsächlich etwas tun": das Web durchsuchen, eine Datenbank abfragen, eine interne API aufrufen, Code ausführen. Der Agent entscheidet *wann* und *mit welchen Argumenten* er ein Tool aufruft — ihr müsst das Tool nur klar genug beschreiben, damit das LLM es korrekt einsetzen kann. Jedes CrewAI-Tool braucht einen **Namen** und eine **Beschreibung** (das liest der Agent, um zu entscheiden, ob/wie er es einsetzt — vage Beschreibungen führen zu Fehlgebrauch), ein **Eingabeschema** (ein Pydantic-Modell) und eine `_run()`-Methode mit der eigentlichen Implementierung.

Die Idee, dass ein Sprachmodell selbst lernen kann, *wann* es ein Tool aufruft, *welches* Tool, und *welche Argumente* es übergibt — statt dass ein Mensch hartcodiert, wann Tools ausgelöst werden — wurde demonstriert in:

> Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

![Toolformer-Beispiele: das Modell fügt API-Aufrufe für ein QA-System, einen Taschenrechner, ein Übersetzungssystem und eine Wikipedia-Suchmaschine in seinen eigenen generierten Text ein](../assets/toolformer-schick2023-fig1.png)
*Abbildung 1 aus Schick et al. (2023): Toolformer entscheidet autonom, APIs aufzurufen, um benötigte Informationen zu erhalten. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

## In diesem Repo

[src/research_crew/tools/custom_tool.py](../../src/research_crew/tools/custom_tool.py) ist eine Vorlage, noch nicht in die Crew eingebunden:

```python
class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        return "this is an example of a tool output, ignore it and move along."
```

Vergleicht es mit dem bereits genutzten Tool, [crew.py:22](../../src/research_crew/crew.py#L22): `SerperDevTool()` — ein vollständig fertiges Tool aus `crewai_tools`, das keine Implementierung benötigt, nur einen API-Schlüssel (`SERPER_API_KEY`). Die [Tool-Kategorientabelle](../../README.md#adding-more-tools-or-rag-for-students) im README listet ~90 fertige Tools auf, aufgeteilt danach, ob sie nur einen API-Schlüssel brauchen oder lokale Embeddings (das ist Sprint 3).

## Aufgabe

1. **Sprint Planning**: Öffnet 1–2 GitHub-Issues als User Stories, gelabelt `epic:tools`, mit Akzeptanzkriterien, die sowohl den Erfolgsfall als auch einen Fehlerfall (Rate-Limit, leeres Ergebnis, API down) abdecken.
2. Wählt ein Tool, das euer Anwendungsfall **wirklich braucht** — nicht eines, um ein Kästchen abzuhaken. Entweder ein fertiges aus der README-Tabelle, oder ein eigenes nach dem Muster von `custom_tool.py`, falls nichts Bestehendes passt.
3. Bindet es beim relevanten Agenten in `crew.py` ein (`tools=[...]`) und schreibt eine Task-Beschreibung, die den Agenten dazu bringen sollte, es nutzen zu wollen.
4. Führt es aus und prüft, dass der Agent das Tool tatsächlich aufruft — schaut in die ausführlichen Logs, nehmt es nicht einfach an.
5. Aktualisiert die Tools-Tabelle in `DESIGN.md`.
6. Bevor ihr das als fertig betrachtet, beantwortet in `DESIGN.md`: Was passiert, wenn dieses Tool rate-limitiert ist, nichts Brauchbares zurückgibt, oder die API mitten im Lauf ausfällt — degradiert eure Crew kontrolliert, oder scheitert sie einfach? Macht die Tool-Beschreibung Fehlgebrauch wahrscheinlich (falsche Argumente, oder es wird nicht aufgerufen, obwohl es sollte)? Was ist jetzt, mit Tool, konkret besser als euer MVP aus Sprint 1 — und wie würdet ihr das eurem Stakeholder zeigen, statt es nur zu behaupten?

## Zusatzaufgabe

Tauscht euer Tool gegen ein anderes, das dasselbe Problem löst (z. B. einen anderen Such-Anbieter), und vergleicht: gleicher Task, gleicher Agent, anderes Tool — ändert sich das Verhalten oder die Ausgabequalität des Agenten, und warum könnte das so sein?
