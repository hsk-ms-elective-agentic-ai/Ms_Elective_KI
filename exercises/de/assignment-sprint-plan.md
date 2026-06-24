# Sprint-Plan — Die Team-Aufgabe als Scrum durchführen

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-sprint-plan.md)

Das übersetzt die [Meilenstein-Leiter](assignment-milestones.md) in fünf Scrum-Sprints, einen pro Übung (oder Übungspaar). Es nutzt Artefakte, die ihr schon habt — die vorgeschlagenen User Stories aus jedem Meilenstein, das Backlog (GitHub Issues + Projects-Board) aus den [Vorlagen für die Aufgabe](assignment-templates.md), und `DESIGN.md` — statt neue einzuführen. Passt den Takt an euren echten Sitzungsrhythmus an: ein Daily Standup ergibt für ein Team keinen Sinn, das sich nur einmal pro Woche trifft — ein kurzer asynchroner Check-in (ein Kommentar auf eurem Issues-Board) erfüllt denselben Zweck.

Jeder Sprint unten hat dieselben fünf Teile: **Sprint-Ziel**, **Sprint Planning** (was am Anfang zu tun ist), **Definition of Done**, **Sprint Review** (was am Ende zu prüfen ist), und einen Verweis auf die **Sprint-Retrospektive** (dieselben drei Fragen jedes Mal — siehe das Ende dieser Seite).

## Sprint 1: Baseline

**Verknüpft mit:** [Übung 01](01-agentic-frameworks.md) → [Meilenstein M0](assignment-milestones.md#m0-baseline)

**Sprint-Ziel:** eine funktionierende, zweistufige, sequentielle Crew mit Rollen, die euer Team entworfen hat — nicht das `researcher`/`analyst`-Paar des Starter-Repos mit neuem Thema.

**Sprint Planning:**
- Wählt euren Anwendungsfall aus der [Anwendungsfall-Tabelle](../../README.md#use-cases-to-pick-from), oder schlagt einen eigenen vor.
- Brecht "zwei Agenten + einen Task-Flow entwerfen" in 2–3 User-Story-Issues herunter (nutzt die [User-Story-Vorlage](assignment-templates.md)), gelabelt `epic:baseline`.
- Bestimmt die Facilitator-Person für diesen Sprint — wechselt die Rolle jeden Sprint, falls euer Team größer als zwei ist.

**Definition of Done:**
- `agents.yaml` und `tasks.yaml` mit euren eigenen Rollen, Zielen und Backstories aktualisiert
- `DESIGN.md`-Abschnitte 1–2 (Überblick, Architektur) ausgefüllt, M0-Zeilen in den Tabellen Risiken/Grenzen ergänzt

**Sprint Review:** führt die Crew aus, lest die Ausgabe gemeinsam als Team; prüft sie gegen die [Risikofragen von M0](assignment-milestones.md#m0-baseline), bevor ihr den Sprint als abgeschlossen betrachtet.

## Sprint 2: Tools

**Verknüpft mit:** [Übung 02](02-tool-use.md) → [Meilenstein M1](assignment-milestones.md#m1-tools)

**Sprint-Ziel:** ein Tool, das euer Anwendungsfall wirklich braucht, verkabelt und durchdacht — nicht hinzugefügt, um ein Kästchen abzuhaken.

**Sprint Planning:**
- Wählt aus der [Tool-Tabelle des READMEs](../../README.md#adding-more-tools-or-rag-for-students) (oder schreibt ein eigenes gemäß Übung 02) das Tool, das euer Anwendungsfall wirklich braucht.
- Schreibt 1–2 User-Story-Issues, gelabelt `epic:tools`, mit Akzeptanzkriterien, die sowohl den Erfolgsfall als auch den Fehlerfall (Rate-Limit / leeres Ergebnis / API down) abdecken.

**Definition of Done:**
- `agents.yaml` (Tools-Liste) und der API-Key des Tools in `.env`
- Die Tools-Tabelle in `DESIGN.md` ausgefüllt, M1-Zeilen in Risiken/Grenzen ergänzt

**Sprint Review:** zeigt, dass der Agent das Tool tatsächlich aufruft (nicht nur konfiguriert hat); prüft, dass die Fehlerfall-Risikofrage aus [M1](assignment-milestones.md#m1-tools) eine echte Antwort hat, keinen Platzhalter.

## Sprint 3: RAG (Zwischenabgabe)

**Verknüpft mit:** [Übung 03](03-agentic-rag.md) → [Meilenstein M2](assignment-milestones.md#m2-rag-zwischenabgabe)

**Sprint-Ziel:** Antworten, die in einer echten Knowledge Source verankert sind, statt dass das Modell rät.

**Sprint Planning:**
- Entscheidet, welches Dokument/welche Quelle für euren Anwendungsfall wirklich relevant ist (Ideen in der Spalte "Naheliegende M2-RAG-Quelle" der Tabelle).
- Schreibt ein User-Story-Issue, gelabelt `epic:rag`; falls die Zeit knapp ist, ist `knowledge_source_example.py` ein funktionierender Ausgangspunkt (siehe Übung 03).

**Definition of Done:**
- `knowledge_sources=[...]` in `crew.py` verkabelt, eine neue Datei unter `knowledge/`
- Die Tabelle Knowledge Sources/RAG in `DESIGN.md` ausgefüllt, M2-Zeilen in Risiken/Grenzen ergänzt

**Sprint Review:** das ist zugleich eure **Zwischenabgabe** — siehe [M2 in der Meilenstein-Leiter](assignment-milestones.md#m2-rag-zwischenabgabe) für die genaue Abgabe. Prüft vor der Deadline noch einmal, dass `DESIGN.md`-Abschnitte 1–4 vollständig sind, nicht nur der Abschnitt dieses Sprints.

## Sprint 4: Multi-Agent

**Verknüpft mit:** [Übung 04](04-multi-agent-pattern.md) → [Meilenstein M3](assignment-milestones.md#m3-multi-agent)

**Sprint-Ziel:** ein dritter Agent und eine bewusste, begründete Prozessentscheidung — nicht Multi-Agent um des Multi-Agent-Seins willen.

**Sprint Planning:**
- Bevor ihr Code schreibt: Argumentiert als Team beide Seiten — sequentiell vs. hierarchisch — für genau euren Anwendungsfall. Schreibt auch das unterlegene Argument auf — gutes Material für den Abschnitt "Betrachtete Alternativen" in `DESIGN.md`.
- Schreibt ein User-Story-Issue, gelabelt `epic:multi-agent`, für die Rolle des dritten Agenten.

**Definition of Done:**
- Dritter Agent hinzugefügt; `process`-Entscheidung getroffen und umgesetzt
- Architektur in `DESIGN.md` aktualisiert, M3-Zeilen in Risiken/Grenzen ergänzt

**Sprint Review:** prüft die Risikofrage zum dritten Agenten aus [M3](assignment-milestones.md#m3-multi-agent) — könntet ihr diesen Agenten weglassen und seine Arbeit einem der anderen beiden geben? Falls ja, schreibt das ehrlich in `DESIGN.md`, statt einen Entwurf zu verteidigen, der nicht trägt.

## Sprint 5: Produktion und Sicherheit (Abschlussabgabe)

**Verknüpft mit:** [Übung 05](05-production.md) + [Übung 06](06-securing-agents.md) → [Meilenstein Abschluss](assignment-milestones.md#abschluss-produktion-und-sicherheit)

**Sprint-Ziel:** eine glaubwürdige Antwort auf "was geht als Erstes kaputt, und wie würdet ihr es merken" — kein zu bauendes Feature.

**Sprint Planning:**
- Keine neuen User-Story-Issues für neue Features nötig — das "Backlog" dieses Sprints ist die schriftliche Ausarbeitung selbst. Falls ihr trotzdem eines wollt, schreibt ein Issue, gelabelt `epic:hardening`, für die Lücke, die euer Team am bedenklichsten findet.
- Lest eure eigenen Retrospektiven aus Sprint 1–4 noch einmal, bevor ihr den letzten Design-Historie-Eintrag schreibt — das ist buchstäblich das Ausgangsmaterial für "was hat sich geändert und warum".

**Definition of Done:**
- Die Abschnitte Sicherheit & Threat Model und Produktions-Aspekte in `DESIGN.md` vollständig
- Ein konkretes, hypothetisches Prompt-Injection-Szenario, spezifisch zu *euren* Tools/Knowledge Sources (nicht das generische aus Übung 06)
- Letzter Design-Historie-Eintrag mit der Antwort, was sich seit der Zwischenabgabe verändert hat, und warum

**Sprint Review:** das ist eure **Abschlussabgabe** — siehe [den Meilenstein Abschluss](assignment-milestones.md#abschluss-produktion-und-sicherheit) für die genaue Liste der Abgabeartefakte.

## Die 3 Retrospektive-Fragen (jeden Sprint)

Beantwortet am Ende jedes Sprints diese drei Fragen als Team:
1. Was lief diesen Sprint gut?
2. Was lief nicht gut, und warum?
3. Was ist die eine Sache, die ihr im nächsten Sprint ändert?

Schreibt die Antworten direkt in den Abschnitt **Design-Historie** von `DESIGN.md` als Eintrag für diesen Meilenstein — eure Retrospektive und euer benoteter Nachweis der Entwurfs-Entwicklung sind dasselbe Artefakt, nicht zwei getrennt zu pflegende Dinge. Das ist auch der Grund, warum die Design-Historie append-only ist: eine echte Retrospektive-Spur, kein nachträglich aufgeräumter Rückblick.
