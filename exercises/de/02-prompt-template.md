# Schritt 2 — Prompting-Techniken

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/02-prompt-template.md)

Vier Skripte, dasselbe Thema, dasselbe Modell. Jedes ist eine andere Strategie, um die Ausgabe des Modells zu formen — ohne Framework, ohne Agenten. Führt alle vier aus und vergleicht die Ausgaben.

## Hintergrund

Ein Prompt ist ein Programm. Die Strategien, die ihr anwendet — Beispiele bereitstellen, Eingaben in benannte Komponenten strukturieren, eine Aufgabe in sequentielle Aufrufe aufteilen, explizites Reasoning anfordern — sind der Code. Das Modell ist die Laufzeitumgebung.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

**Few-Shot-Prompting** — das Bereitstellen von Eingabe-/Ausgabe-Beispielen im Prompt, damit das Modell das erwartete Format und den Stil aus dem Kontext lernt, ohne Gewichtsaktualisierungen — war der zentrale Befund von:

> Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., … Amodei, D. (2020). *Language Models are Few-Shot Learners*. NeurIPS 2020. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

**Zero-Shot-Chain-of-Thought** — das Hinzufügen einer kurzen Anweisung, das Problem Schritt für Schritt zu durchdenken, bevor geantwortet wird, ohne ausgearbeitete Beispiele — wurde gezeigt in:

> Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). *Large Language Models are Zero-Shot Reasoners*. NeurIPS 2022. [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)

Wei et al. (2022) haben separat gezeigt, dass das Einbinden vollständig ausgearbeiteter Reasoning-Ketten als Few-Shot-Beispiele die Leistung ebenfalls verbessert — beide Ergebnisse ergänzen sich:

> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

## Die vier Skripte

### 2a — Few-Shot-Prompting
[src/exercises/step_02a_few_shot.py](../../src/exercises/step_02a_few_shot.py)

Zwei oder drei Eingabe-/Ausgabe-Beispielpaare erscheinen im Prompt vor der eigentlichen Frage. Das Modell lernt das erwartete Format und den Stil aus diesen Beispielen — das ist In-Context-Learning (Brown et al., 2020). Keine Struktur, keine Reasoning-Anweisung, nur Muster.

### 2b — Prompt-Vorlage
[src/exercises/step_02b_prompt_template.py](../../src/exercises/step_02b_prompt_template.py)

Der Prompt ist in benannte Komponenten aufgeteilt (`persona`, `instruction`, `context`, `data_format`, `audience`, `tone`, `data`), die zu einer einzigen Query zusammengefügt werden. Ein API-Aufruf, keine Beispiele, keine Reasoning-Anweisung.

### 2c — Chain Prompting
[src/exercises/step_02c_chain_prompting.py](../../src/exercises/step_02c_chain_prompting.py)

Zwei sequentielle API-Aufrufe: Der erste extrahiert oder bereitet etwas aus dem Thema vor; der zweite erhält diese Ausgabe und produziert die finale Antwort. Die Aufgabe wird bewusst aufgeteilt.

### 2d — Chain of Thought
[src/exercises/step_02d_chain_of_thought.py](../../src/exercises/step_02d_chain_of_thought.py)

Dieselbe Komponentenstruktur wie 2b, mit einer Ergänzung: eine `reasoning`-Komponente, die das Modell bittet, das Problem durchzudenken, bevor es antwortet. Dies ist das Zero-Shot-CoT-Muster von Kojima et al. (2022) — keine Beispiele nötig, nur die Anweisung.

## Aufgabe

1. Setzt euer Thema in allen vier Skripten — dasselbe Thema wie in Schritt 1, dasselbe Thema für 2a/2b/2c/2d.

2. Füllt die `TODO`-Felder aus und führt jedes Skript aus:
   ```bash
   uv run python src/exercises/step_02a_few_shot.py
   uv run python src/exercises/step_02b_prompt_template.py
   uv run python src/exercises/step_02c_chain_prompting.py
   uv run python src/exercises/step_02d_chain_of_thought.py
   ```

3. Vergleicht die vier Ausgaben (jede wird in `output/step_02*.md` gespeichert):
   - Lenken die Beispiele in 2a das Modell auf ein bestimmtes Format oder eine bestimmte Schlussfolgerung? Was passiert, wenn ihr nur ein Beispiel ändert?
   - Welche Komponenten in 2b hatten den sichtbarsten Einfluss? Versucht, eine nach der anderen zu entfernen.
   - Verbessert die Zwei-Schritt-Aufteilung in 2c die finale Ausgabe, oder produziert das Modell in einem Schritt etwas Ähnliches?
   - Produziert die `reasoning`-Anweisung in 2d erkennbar andere Schlussfolgerungen — oder nur mehr Text?

4. Füllt den **Schritt 2**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Probiert in 2a eine „Zero-Shot"-Variante, indem ihr die Beispiele entfernt und nur die Frage stellt — vergleicht das dann mit der Few-Shot-Version. Ist die Verbesserung durch die Beispiele groß, klein oder unerwartet?
