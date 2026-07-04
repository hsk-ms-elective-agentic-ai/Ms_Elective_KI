# Schritt 4 — Multi-Agent

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/04-multi-agent.md)

Fügt einen zweiten Agenten mit einer anderen, ergänzenden Rolle hinzu. Der Researcher sammelt und strukturiert; der Analyst empfängt dessen Ausgabe und hinterfragt sie, extrahiert strategische Implikationen, die ein reiner Researcher nicht herausgearbeitet hätte. Sequentielle Pipeline: `researcher → analyst`. Das ist Multi-Agent im einfachsten Sinne — keine dynamische Delegation, nur Rollenspezialisierung mit Task-Verkettung.

## Hintergrund

Ein einzelner Agent kann mehrere Dinge tun, aber er kann nicht gleichzeitig wirklich unterschiedliche epistemische Rollen einnehmen — er kann nicht gleichzeitig gutgläubig (alles sammeln, was er finden kann) und skeptisch (das gerade Gefundene hinterfragen) sein. Mehrere Agenten erlauben euch, diese Spannung in die Architektur einzubauen. Die grundlegende Demonstration, dass Agenten durch Konversation anstatt über eine gemeinsame Datenbank zusammenarbeiten können, war:

> Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

![AutoGen: konversierbare, anpassbare Agenten, die Aufgaben in gemeinsamen oder hierarchischen Mustern lösen](../assets/autogen-wu2023-fig1.png)
*Abbildung 1 aus Wu et al. (2023): AutoGen-Agenten lösen Aufgaben durch mehrstufige Konversation. Reproduziert für Bildungszwecke in diesem Kurs.*

Die CrewAI-Version hier ist einfacher: keine Konversationsschleife, nur eine einseitige Übergabe der Researcher-Ausgabe an den Analysten über `context=[research_task]`.

## Der Code

Öffnet [src/exercises/step_04_multi_agent.py](../../src/exercises/step_04_multi_agent.py). Die Ergänzungen gegenüber Schritt 3:

| Hinzugefügt | Was es bewirkt |
| --- | --- |
| `analyst = Agent(...)` | Zweiter Agent, explizit skeptische Rolle |
| `analysis_task` | Task für den Analysten, mit `context=[research_task]` |
| `context=[research_task]` | Gibt die Researcher-Ausgabe an den Analysten weiter |
| Zwei Agenten in `Crew(agents=[...])` | Beide laufen, nacheinander |

## Aufgabe

1. Setzt `TOPIC` auf dasselbe Thema wie in den vorherigen Schritten.

2. Führt es aus:
   ```bash
   uv run python src/exercises/step_04_multi_agent.py
   ```

3. Lest beide verbose-Logs — den des Researchers und den des Analysten. Notiert:
   - Hinterfragt der Analyst tatsächlich irgendetwas, was der Researcher gefunden hat, oder verpackt er es hauptsächlich neu?
   - Was aus der Backstory des Analysten ("skeptisch", "sucht nach Fehlendem") taucht in der Ausgabe auf — und was nicht?
   - Fühlt sich die finale Analyse qualitativ anders an als das, was ein einzelner Agent in Schritt 3 produziert hat, oder ist es hauptsächlich derselbe Inhalt in zwei Durchgängen?

4. **Experimentiert**: Entfernt `context=[research_task]` aus `analysis_task` und führt erneut aus. Was passiert mit der Ausgabe des Analysten, wenn er die Arbeit des Researchers nicht mehr sehen kann?

5. Füllt den **Schritt 4**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Fügt eine dritte Rolle hinzu — nicht um drei Agenten zu haben, sondern eine, deren Fehlen ihr tatsächlich bemerken würdet. Kandidaten: ein Kritiker, der Gegenargumente formuliert, ein Übersetzer, der die Ausgabe für ein Laienpublikum umschreibt, oder ein Prüfer, der jede Behauptung gegen eine bekannte Einschränkung überprüft. Führt es aus und prüft, ob sich die Ausgabe bedeutsam verändert. Falls nicht — warum nicht?
