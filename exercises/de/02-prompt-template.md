# Schritt 2 — Prompt-Vorlage

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/02-prompt-template.md)

Dasselbe Modell, derselbe einzelne API-Aufruf, dasselbe Thema — aber jetzt mit einem **System-Prompt**, der eine Rolle zuweist und ein Ausgabeformat vorschreibt. Kein Framework, nur zwei Nachrichten. Die Frage, um die dieser Schritt kreist: Wie viel des Qualitätsunterschieds zwischen einer mittelmäßigen und einer nützlichen LLM-Antwort kommt vom Modell, und wie viel davon, wie ihr ihm sagt, was es sein soll?

## Hintergrund

"System", "user" und "assistant" sind eine Konvention — ein Beschriftungsschema, das dem Modell mitteilt, welche Teile des Kontextfensters Anweisungen, Fragen oder frühere Antworten sind. Das Modell verarbeitet sie alle als Tokens, aber sein Training enthielt genug Beispiele von so beschrifteten Gesprächen, dass die Beschriftungen verschieben, aus welchem Teil seiner Trainingsverteilung die Antwort schöpft.

Die Kernerkenntnis, die dieser Schritt demonstriert:

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

Der Kerngedanke: Ein Prompt ist ein Programm. Die Rolle, die Formatanweisungen und die Einschränkungen, die ihr schreibt, sind der Code; das Modell ist die Laufzeitumgebung. Ihr könnt verändern, was das Programm produziert, ohne die Laufzeitumgebung zu verändern.

## Der Code

Öffnet [src/exercises/step_02_prompt_template.py](../../src/exercises/step_02_prompt_template.py). Vergleicht es mit Schritt 1 — die einzigen Ergänzungen sind:

| Hinzugefügt | Was es bewirkt |
| --- | --- |
| `SYSTEM_PROMPT` | Weist eine Rolle zu ("senior research analyst") und schreibt vier Ausgabeabschnitte vor |
| `USER_PROMPT` | Formatierter String mit eingesetztem Thema |
| Zwei Nachrichten statt einer | System-Nachricht setzt Kontext; Nutzer-Nachricht stellt die Frage |

Keine neuen Abhängigkeiten, kein Framework.

## Aufgabe

1. Setzt `TOPIC` auf dasselbe Thema wie in Schritt 1.

2. Führt es aus:
   ```bash
   uv run python src/exercises/step_02_prompt_template.py
   ```

3. Vergleicht die Ausgabe mit Schritt 1:
   - Sind die vier Abschnitte aus `SYSTEM_PROMPT` tatsächlich erschienen?
   - Ist die Ausgabe für euer spezifisches Thema nützlicher — oder nur anders formatiert?
   - Was macht das Modell mit dem "Open Questions"-Abschnitt — erzeugt es echte offene Fragen oder Fülltext?

4. **Experimentiert**: versucht mindestens eins davon und beobachtet, was sich verändert:
   - Entfernt die Abschnittsüberschriften aus `SYSTEM_PROMPT` — verschwindet das Format, oder behält das Modell es trotzdem bei?
   - Ändert die Rolle von "senior research analyst" auf etwas anderes (z. B. "skeptischer Journalist", "Erstjahresstudent"). Verändert sich die Ausgabe so, wie ihr es erwartet habt?

5. Füllt den **Schritt 2**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Schreibt eine zweite Vorlage für dasselbe Thema, aber für eine andere Zielgruppe (z. B. Studierende vs. Vorstandsmitglieder). Führt beide aus. Verändert die Zielgruppenspezifikation tatsächlich, welche Informationen erscheinen — oder nur den Ton?
