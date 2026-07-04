# Schritt 2 — Prompting-Techniken

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/02-prompt-template.md)

Drei Skripte, dasselbe Thema, dasselbe Modell. Jedes ist eine andere Strategie, um die Ausgabe des Modells zu formen — ohne Framework, ohne Agenten. Führt alle drei aus und vergleicht die Ausgaben.

## Hintergrund

Ein Prompt ist ein Programm. Die Strategien, die ihr anwendet — Eingaben in benannte Komponenten strukturieren, explizites Reasoning anfordern, eine Aufgabe in sequentielle Aufrufe aufteilen — sind der Code. Das Modell ist die Laufzeitumgebung.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

Chain-of-Thought-Prompting speziell — die Demonstration, dass das Bitten des Modells, vor der Antwort zu denken, die Leistung bei komplexen Aufgaben verbessert — wurde gezeigt in:

> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

## Die drei Skripte

### 2a — Prompt-Vorlage
[src/exercises/step_02a_prompt_template.py](../../src/exercises/step_02a_prompt_template.py)

Der Prompt ist in benannte Komponenten aufgeteilt (`persona`, `instruction`, `context`, `data_format`, `audience`, `tone`, `data`), die zu einer einzigen Query zusammengefügt werden. Ein API-Aufruf.

### 2b — Chain of Thought
[src/exercises/step_02b_chain_of_thought.py](../../src/exercises/step_02b_chain_of_thought.py)

Dieselbe Komponentenstruktur wie 2a, mit einer Ergänzung: eine `reasoning`-Komponente, die das Modell bittet, das Problem durchzudenken, bevor es antwortet. Ein API-Aufruf.

### 2c — Chain Prompting
[src/exercises/step_02c_chain_prompting.py](../../src/exercises/step_02c_chain_prompting.py)

Zwei sequentielle API-Aufrufe: Der erste extrahiert oder bereitet etwas aus dem Thema vor; der zweite erhält diese Ausgabe und produziert die finale Antwort. Die Aufgabe wird bewusst aufgeteilt.

## Aufgabe

1. Setzt euer Thema in allen drei Skripten — dasselbe Thema wie in Schritt 1, dasselbe Thema für 2a/2b/2c.

2. Füllt die `TODO`-Felder aus und führt jedes Skript aus:
   ```bash
   uv run python src/exercises/step_02a_prompt_template.py
   uv run python src/exercises/step_02b_chain_of_thought.py
   uv run python src/exercises/step_02c_chain_prompting.py
   ```

3. Vergleicht die drei Ausgaben:
   - Welche Komponenten in 2a hatten den sichtbarsten Einfluss? Versucht, eine nach der anderen zu entfernen.
   - Produziert die `reasoning`-Komponente in 2b erkennbar andere Schlussfolgerungen — oder nur mehr Text?
   - Verbessert die Zwei-Schritt-Aufteilung in 2c die finale Ausgabe, oder produziert das Modell in einem Schritt etwas Ähnliches?

4. Füllt den **Schritt 2**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Tauscht in Schritt 2c die Reihenfolge der beiden Prompts — macht zuerst den "finalen" Schritt, dann verfeinert mit der Ausgabe des "Vorbereitungs"-Schritts. Spielt die Reihenfolge eine Rolle?
