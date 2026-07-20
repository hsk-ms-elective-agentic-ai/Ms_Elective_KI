# Schritt 2 — Prompting-Techniken

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../../en/prompting/02-prompt-template.md)

**Hinweis:** Dieser Schritt besteht jetzt aus fünf Jupyter-Notebooks (auf Englisch) statt einzelner Python-Skripte — siehe [step_02a_few_shot.ipynb](../../en/prompting/step_02a_few_shot.ipynb) bis [step_02e_tree_of_thought.ipynb](../../en/prompting/step_02e_tree_of_thought.ipynb). Diese Seite beschreibt Hintergrund und Aufgabe weiterhin auf Deutsch; die deutschen Notebook-Versionen folgen noch.

Fünf Notebooks, dasselbe Thema, dasselbe Modell. Jedes ist eine andere Strategie, um die Ausgabe des Modells zu formen — noch keine Agenten, nur CrewAIs `LLM`-Klasse direkt aufgerufen. Führt alle fünf aus und vergleicht die Ausgaben.

## Hintergrund

Ein Prompt ist ein Programm. Die Strategien, die ihr anwendet — Beispiele bereitstellen, Eingaben in benannte Komponenten strukturieren, eine Aufgabe in sequentielle Aufrufe aufteilen, explizites Reasoning anfordern — sind der Code. Das Modell ist die Laufzeitumgebung.

> Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). *Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing*. ACM Computing Surveys, 55(9), 1–35. [arXiv:2107.13586](https://arxiv.org/abs/2107.13586)

**Few-Shot-Prompting** — das Bereitstellen von Eingabe-/Ausgabe-Beispielen im Prompt, damit das Modell das erwartete Format und den Stil aus dem Kontext lernt, ohne Gewichtsaktualisierungen — war der zentrale Befund von:

> Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., … Amodei, D. (2020). *Language Models are Few-Shot Learners*. NeurIPS 2020. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

**Zero-Shot-Chain-of-Thought** — das Hinzufügen einer kurzen Anweisung, das Problem Schritt für Schritt zu durchdenken, bevor geantwortet wird, ohne ausgearbeitete Beispiele — wurde gezeigt in:

> Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). *Large Language Models are Zero-Shot Reasoners*. NeurIPS 2022. [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)

Wei et al. (2022) haben separat gezeigt, dass das Einbinden vollständig ausgearbeiteter Reasoning-Ketten als Few-Shot-Beispiele die Leistung ebenfalls verbessert — beide Ergebnisse ergänzen sich:

> Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

**Tree of Thought** — das Erkunden mehrerer Reasoning-Pfade statt einer einzelnen Kette, mit der Möglichkeit, Pfade zu vergleichen, zurückzuverfolgen oder unterwegs zu verwerfen — wurde eingeführt in:

> Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. NeurIPS 2023. [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)

## Die fünf Notebooks

### 2a — Few-Shot-Prompting
[step_02a_few_shot.ipynb](../../en/prompting/step_02a_few_shot.ipynb)

Zwei oder drei Eingabe-/Ausgabe-Beispielpaare erscheinen im Prompt vor der eigentlichen Frage. Das Modell lernt das erwartete Format und den Stil aus diesen Beispielen — das ist In-Context-Learning (Brown et al., 2020). Keine Struktur, keine Reasoning-Anweisung, nur Muster.

### 2b — Prompt-Vorlage
[step_02b_prompt_template.ipynb](../../en/prompting/step_02b_prompt_template.ipynb)

Ein API-Aufruf, keine Beispiele, keine Reasoning-Anweisung — aber die Nachricht ist jetzt auf zwei *Rollen* aufgeteilt:

- **`system`**: Hintergrundanweisungen, die der Endnutzer nie sieht — `persona`, `instruction`, `context`, `data_format`, `audience`, `tone`. Das sagt dem Modell, wer es ist und wie es sich bei jeder Antwort verhalten soll.
- **`user`**: die eigentliche Frage — nur das Thema, das beantwortet werden soll.

Dies ist die Standardstruktur der OpenAI Chat Completions API (und jedes Modells, das ihr folgt). Die `system`-Rolle ist ein erstklassiges Konzept im Protokoll, keine bloße Formatierungskonvention. Versucht, einzelne System-Komponenten zu entfernen, um zu sehen, was jede tatsächlich steuert.

Die Persona-Komponente allein kann die gesamte Antwort verändern: „Du bist ein geduldiger Gymnasiallehrer" versus „Du bist ein leitender Machine-Learning-Engineer, der einen Pull Request reviewt" führt bei derselben Frage und demselben Thema zu sehr unterschiedlichem Ton, Vokabular und Tiefe. Das Notebook enthält dazu keine leeren `TODO`-Felder — alle sechs Komponenten (`persona`, `instruction`, `context`, `data_format`, `audience`, `tone`) sind zweimal mit derselben Frage vorausgefüllt: einmal als Lehrer-Persona, einmal als Engineer-Persona. Vergleicht die beiden Ausgaben, entfernt einzelne Komponenten oder tauscht Werte aus, um ihren jeweiligen Effekt zu sehen.

### 2c — Chain Prompting
[step_02c_chain_prompting.ipynb](../../en/prompting/step_02c_chain_prompting.ipynb)

Zwei sequentielle API-Aufrufe: Der erste extrahiert oder bereitet etwas aus dem Thema vor; der zweite erhält diese Ausgabe und produziert die finale Antwort. Die Aufgabe wird bewusst aufgeteilt.

### 2d — Chain of Thought
[step_02d_chain_of_thought.ipynb](../../en/prompting/step_02d_chain_of_thought.ipynb)

Dieselbe Komponentenstruktur wie 2b, mit einer Ergänzung: eine `reasoning`-Komponente, die das Modell bittet, das Problem durchzudenken, bevor es antwortet. Dies ist das Zero-Shot-CoT-Muster von Kojima et al. (2022) — keine Beispiele nötig, nur die Anweisung.

### 2e — Tree of Thought
[step_02e_tree_of_thought.ipynb](../../en/prompting/step_02e_tree_of_thought.ipynb)

Statt sich auf eine einzelne Reasoning-Kette festzulegen, bittet ihr mehrere "Experten", parallel zu denken: jeder schreibt einen Schritt auf, teilt ihn mit der Gruppe, dann geht es gemeinsam zum nächsten Schritt. Jeder Experte, dessen Reasoning sich als falsch herausstellt, scheidet unterwegs aus.

## Aufgabe

1. Setzt euer Thema in jedem Notebook — dasselbe Thema wie in Schritt 1, dasselbe Thema für 2a–2e.

2. Öffnet jedes Notebook einzeln in VS Code/Cursor, wählt den Kernel **"research_crew"** und führt die Zellen der Reihe nach aus (zuerst die "Setup"-Zelle) — 2b führt direkt zwei ausformulierte Beispiele aus (Lehrer- vs. Engineer-Persona); 2a, 2c, 2d und 2e haben `TODO`-Felder zum Ausfüllen.

3. Vergleicht die Ausgaben:
   - Lenken die Beispiele in 2a das Modell auf ein bestimmtes Format oder eine bestimmte Schlussfolgerung? Was passiert, wenn ihr nur ein Beispiel ändert?
   - Welche Komponenten in 2b hatten den sichtbarsten Einfluss? Versucht, eine nach der anderen zu entfernen.
   - Verbessert die Zwei-Schritt-Aufteilung in 2c die finale Ausgabe, oder produziert das Modell in einem Schritt etwas Ähnliches?
   - Produziert die `reasoning`-Anweisung in 2d erkennbar andere Schlussfolgerungen — oder nur mehr Text?
   - Widersprechen sich die "Experten" in 2e tatsächlich und scheiden aus, oder konvergieren sie sofort auf dieselbe Antwort? Probiert `num_experts` zu ändern.

4. Füllt den **Schritt 2**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Probiert in 2a eine „Zero-Shot"-Variante, indem ihr die Beispiele entfernt und nur die Frage stellt — vergleicht das dann mit der Few-Shot-Version. Ist die Verbesserung durch die Beispiele groß, klein oder unerwartet?
