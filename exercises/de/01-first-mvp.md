# Sprint 1 — Erster lauffähiger MVP

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/01-first-mvp.md)

Die Aufgabe eines Prototyps ist es, euch etwas zu lehren, nicht, fertig poliert zu sein — der schnellste Weg herauszufinden, ob euer Entwurf aus Sprint 0 tatsächlich funktioniert, ist, ihn auszuführen, nicht, ihn weiter auf Papier zu verfeinern. CrewAI bietet zwei Wege, die Reihenfolge zu verkabeln, in der Tasks laufen:

- **`Process.sequential`** — Agent A schließt seine Arbeit vollständig ab und gibt sein Ergebnis dann an Agent B weiter. Die richtige Standardwahl, wenn Schritte wirklich in einer festen Reihenfolge voneinander abhängen.
- **Parallele Tasks innerhalb einer sequentiellen Crew** — setzt `async_execution: true` auf einem `Task`, und er läuft in einem Hintergrund-Thread statt zu blockieren; ein späterer Task, der davon abhängt (über `context`), wartet trotzdem darauf, aber Tasks, die *nicht* voneinander abhängen, können gleichzeitig laufen statt nacheinander.

Die zugrundeliegenden Agenten-Architekturen, auf denen das aufbaut, stammen aus der klassischen Taxonomie in:

> Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4. Aufl.), Kapitel 2: Intelligent Agents. Pearson.

Hier keine Abbildung — es ist ein Buch, kein offen lizenziertes Paper, daher zitieren wir, statt die Diagramme zu reproduzieren.

## In diesem Repo

[crew.py:48-60](../../src/research_crew/crew.py#L48-L60):

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
    ...
)
```

`Process.sequential` bedeutet: `research_task` vollständig ausführen (der `researcher`-Agent arbeitet allein), dann `analysis_task` ausführen (der `analyst`-Agent arbeitet allein, erhält aber das Recherche-Ergebnis über `context: - research_task` in [tasks.yaml](../../src/research_crew/config/tasks.yaml)). Zwei Agenten, feste Reihenfolge, keine Verhandlung — die einfachstmögliche Pipeline, und *noch nicht* die dynamische, manager-delegierte Art von Multi-Agenten-Zusammenarbeit (das ist Sprint 4).

Falls sich zwei eurer Tasks als völlig unabhängig voneinander herausstellen, könnte `async_execution: true` in `tasks.yaml` einen davon laufen lassen, während ein anderer noch läuft, statt grundlos zu warten:

```yaml
research_task:
  description: ...
  async_execution: true
```

## Aufgabe

1. **Sprint Planning**: Öffnet 2–3 GitHub-Issues als User Stories, gelabelt `epic:mvp`, die abdecken: "die Crew läuft Ende-zu-Ende und produziert echte Ausgaben."
2. Implementiert die Agenten und Tasks, die ihr in Sprint 0 entworfen habt, wirklich, in `agents.yaml` und `tasks.yaml`.
3. Entscheidet für jedes Task-Paar: Braucht eines wirklich das Ergebnis des anderen zuerst? Falls nicht, erwägt `async_execution: true`. Falls ihr unsicher seid, bleibt bei sequentiell — die sicherere, vorhersagbarere Wahl, und Parallelität, die ihr nicht braucht, ist nur zusätzliche Komplexität.
4. Führt es aus: `uv run research_crew`. Prüft, dass `output/report.md` (oder eure eigene Ausgabe) tatsächlich euren spezifischen Anwendungsfall widerspiegelt, nicht eine generische Antwort, die zu jedem Thema passen könnte.
5. Aktualisiert den Architektur-Abschnitt von `DESIGN.md`, damit er dem entspricht, was ihr tatsächlich gebaut habt (nicht nur dem, was ihr in Sprint 0 geplant habt — falls es sich geändert hat, ist das in Ordnung, haltet einfach die echte Version fest).
6. Bevor ihr das als fertig betrachtet, beantwortet in `DESIGN.md`: Warum sequentiell (oder async) für jedes Task-Paar konkret, nicht andersrum? Wenn euer echter Anwendungsfall das Zehnfache an Volumen verarbeiten müsste, was würde als Erstes kaputtgehen? Eure Crew läuft gerade fehlerfrei — wie würdet ihr tatsächlich prüfen, dass sie etwas *Nützliches* für euren Stakeholder tut, nicht nur technisch funktioniert?

## Zusatzaufgabe

Bringt absichtlich etwas zum Scheitern — benennt einen YAML-Schlüssel um, entfernt eine `context`-Abhängigkeit, oder gebt bewusst eine schlechte Eingabe — und seht, ob der Fehler offensichtlich oder still ist. Eine Crew, die laut scheitert, ist leichter zu debuggen als eine, die leise eine plausibel aussehende, falsche Antwort produziert.

---

**Das ist auch euer informeller Zwischenstand** — am Ende dieses Sprints sollte euer Team eine funktionierende Baseline haben, die ihr weiter ausbauen könnt, nicht einen Papierentwurf, den ihr noch nicht getestet habt.
