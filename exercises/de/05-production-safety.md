# Sprint 5 — Produktionssicherheit & Stabilität

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/05-production-safety.md)

Einen Agenten von "läuft auf meinem Rechner" in den Produktionsbetrieb zu bringen bedeutet: reproduzierbare Umgebungen, Observability darüber, was der Agent tatsächlich tut, und einen Weg für Nicht-Entwickler, ihn zu nutzen — nichts davon ändert die Agenten-Logik, es ist die operative Schicht darum herum. Agenten-spezifische Sicherheit bringt eigene Risiken über Standard-Appsec hinaus mit: Secrets, die in die Versionskontrolle durchsickern, Prompt Injection (nicht vertrauenswürdiger Inhalt von einem Tool, etwa ein Suchergebnis, das Anweisungen enthält, die den Agenten entführen), und zu weit gefasste Tool-Berechtigungen. Der gemeinsame Nenner: Agenten handeln basierend auf Inhalten, die sie abrufen, also ist alles, was diese Inhalte beeinflussen können, eine Angriffsfläche.

Für "Agenten-Betrieb" gibt es kein einzelnes bahnbrechendes Paper wie für RAG oder Tool-Nutzung:

> Lakshmanan, V. (2025). *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications*. O'Reilly Media. (Siehe die Kapitel zu Deployment/Observability.)

Indirekte Prompt Injection — bösartige Anweisungen, die nicht aus dem eigenen Prompt des Nutzers stammen, sondern aus Inhalten, die das Modell *abruft* — wurde erstmals systematisch gegen echte LLM-integrierte Anwendungen demonstriert in:

> Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security, 79–90. [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)

![Indirekte Prompt Injection: ein Angreifer injiziert Prompts in Inhalte (Webseiten, Dateien, E-Mails), die eine LLM-integrierte Anwendung abruft, und steuert so deren Ausgabe, ohne je direkt mit dem Modell zu sprechen](../assets/promptinjection-greshake2023-fig1.png)
*Abbildung 1 aus Greshake et al. (2023): ein Angreifer kann das LLM indirekt steuern, indem er Prompts in Quellen injiziert, die das Modell abruft. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

## In diesem Repo

Produktion, bereits in dieser Vorlage gezeigt: [.devcontainer/devcontainer.json](../../.devcontainer/devcontainer.json) + `uv.lock` geben allen eine identische Umgebung; [streamlit_app.py](../../streamlit_app.py) abonniert CrewAIs Event-Bus (`crewai_event_bus`) und streamt Ereignisse live, statt nur einen finalen Report zu zeigen — derselbe Mechanismus, den echtes Produktions-Monitoring nutzen würde, hier nur in einer Demo-UI dargestellt statt an ein Logging-Backend geschickt.

Sicherheit, ein echter Beinahe-Fehler beim Bauen dieses Projekts: eine `.env.example`-Datei (die *Vorlage*, von git verfolgt) wäre fast mit echten API-Schlüsseln committed worden statt der echten `.env`-Datei (von git ignoriert), weil die Namen ähnlich aussehen. Das Muster, das ein tatsächliches Leck verhindert hat: `.env` ist in [.gitignore](../../.gitignore) aufgeführt, `.env.example` wird nur mit leeren Platzhaltern ausgeliefert, und `git status`/`git diff` werden vor jedem Push geprüft.

## Aufgabe

1. **Sprint Planning**: Öffnet 1–2 GitHub-Issues als User Stories, gelabelt `epic:hardening`, für die Lücke, die euer Team am bedenklichsten findet.
2. Schreibt einen kurzen Produktionsplan: Was würdet ihr überwachen, und was würde euch tatsächlich auf einen Ausfall hinweisen, konkret für euren Anwendungsfall (keine generische Liste).
3. **Prompt-Injection-Übung**: Konstruiert ein konkretes, hypothetisches (nicht ausgeführtes) Prompt-Injection-Szenario, spezifisch zu *euren* Tools und Knowledge Sources — nicht das generische Suchergebnis-Beispiel von dieser Seite. Denkt durch, was anhand der `context`-Abhängigkeiten eurer Tasks tatsächlich passieren würde — behandelt der empfangende Agent die vorgelagerte Ausgabe als Daten oder als Anweisungen?
4. Optional: Fügt einem Task ein `guardrail` hinzu, das auf verdächtige Inhalte prüft und die Validierung scheitern lässt, falls gefunden — `Task(guardrail=fn)`, eine Funktion `(output) -> (bool, Any)`.
5. Vervollständigt die Abschnitte Sicherheit & Threat Model und Produktions-Aspekte in `DESIGN.md`.
6. Schreibt den letzten **Design-Historie**-Eintrag: Was hat sich zwischen eurer Zwischenabgabe (Sprint 3) und dem finalen Entwurf verändert, und was habt ihr gelernt, das euch zur Änderung bewogen hat? Das ist mehr wert, als es aussieht — es ist die einzige Stelle, an der ihr zeigen müsst, dass sich euer Denken weiterentwickelt hat, statt sich nur angesammelt zu haben.
7. Bevor ihr das als fertig betrachtet, beantwortet in `DESIGN.md`: Würde diese Crew ein Semester lang unbeaufsichtigt zu eurem echten Anwendungsfall laufen — was geht als Erstes kaputt, und wie würdet ihr es tatsächlich merken — nicht "irgendjemand würde es irgendwann merken", sondern ein konkretes Signal, das ihr sehen würdet.

## Zusatzaufgabe

Führt `git log --all --oneline -- .env` in eurem eigenen Team-Repo aus, um zu bestätigen, dass `.env` selbst nie in eurer Geschichte committed wurde. Falls doch, ist das ein echter Befund für euer Threat Model, kein hypothetischer.

---

**Das ist eure Abschlussabgabe.** Siehe [Überblick zur Aufgabe](assignment-overview.md) für die vollständige Bewertung und genau, was einzureichen ist.
