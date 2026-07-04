# Schritt 2 — Prompt-Vorlage

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/02-prompt-template.md)

Dasselbe Modell, derselbe einzelne API-Aufruf, dasselbe Thema — aber jetzt mit einem **System-Prompt**, der eine Rolle zuweist und ein Ausgabeformat vorschreibt. Kein Framework, nur zwei Nachrichten. Die Frage, um die dieser Schritt kreist: Wie viel des Qualitätsunterschieds zwischen einer mittelmäßigen und einer nützlichen LLM-Antwort kommt vom Modell, und wie viel davon, wie ihr ihm sagt, was es sein soll?

## Hintergrund

"System", "user" und "assistant" sind eine Konvention — ein Beschriftungsschema, das dem Modell mitteilt, welche Teile des Kontextfensters Anweisungen, Fragen oder frühere Antworten sind. Das Modell verarbeitet sie alle als Tokens, aber sein Training enthielt genug Beispiele von so beschrifteten Gesprächen, dass die Beschriftungen verschieben, aus welchem Teil seiner Trainingsverteilung die Antwort schöpft.

Die Kernerkenntnis, die dieser Schritt demonstriert:

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

Der Kerngedanke: Ein Prompt ist ein Programm. Die Rolle, die Formatanweisungen und die Einschränkungen, die ihr schreibt, sind der Code; das Modell ist die Laufzeitumgebung. Ihr könnt verändern, was das Programm produziert, ohne die Laufzeitumgebung zu verändern.

## Der Code

Öffnet [src/exercises/step_02_prompt_template.py](../../src/exercises/step_02_prompt_template.py). Der Prompt ist in benannte Komponenten aufgeteilt, die zu einer einzigen Query zusammengefügt werden:

| Komponente | Steuert |
| --- | --- |
| `persona` | Wer das Modell ist |
| `instruction` | Was es tun soll |
| `context` | Hintergrundwissen, das es braucht, um es gut zu tun |
| `data_format` | Wie die Ausgabe aussehen soll |
| `audience` | Wer die Ausgabe liest |
| `tone` | Wie sie klingen soll |
| `data` | Das eigentliche Thema oder den Text |

Keine neuen Abhängigkeiten, kein Framework — nur String-Verkettung.

## Aufgabe

1. Setzt `TOPIC` auf dasselbe Thema wie in Schritt 1.

2. Führt es aus:
   ```bash
   uv run python src/exercises/step_02_prompt_template.py
   ```

3. Vergleicht die Ausgabe mit Schritt 1:
   - Welche Komponenten hatten den sichtbarsten Einfluss auf die Ausgabe?
   - Ist die Ausgabe für euer spezifisches Thema nützlicher — oder nur anders formatiert?

4. **Experimentiert**: Entfernt nacheinander eine Komponente aus `query` und beobachtet, was sich verändert. Versucht mindestens:
   - Entfernt `data_format` — verschwindet die Struktur vollständig?
   - Entfernt `persona` — verändert sich Ton oder Expertenniveau?
   - Entfernt `audience` — ändert sich etwas merklich?

5. Füllt den **Schritt 2**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Schreibt eine zweite Vorlage für dasselbe Thema, aber für eine andere Zielgruppe (z. B. Studierende vs. Vorstandsmitglieder). Führt beide aus. Verändert die Zielgruppenspezifikation tatsächlich, welche Informationen erscheinen — oder nur den Ton?
