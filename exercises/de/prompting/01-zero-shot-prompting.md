# Schritt 1 — Zero-Shot-Prompting

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../../en/prompting/step_01_zero_shot_prompting.ipynb)

**Hinweis:** Dieser Schritt ist jetzt ein Jupyter-Notebook (auf Englisch) statt eines Python-Skripts — siehe [step_01_zero_shot_prompting.ipynb](../../en/prompting/step_01_zero_shot_prompting.ipynb). Diese Seite beschreibt weiterhin Hintergrund und Aufgabe auf Deutsch; die deutsche Notebook-Version folgt noch.

Der direkteste Weg von Frage zu Antwort: ein API-Aufruf, eine Nachricht, eine Antwort. Keine Rollendefinition, kein Ausgabeformat, keine Beispiele, kein Agent — nur das Modell und euer Text, direkt über CrewAIs `LLM`-Klasse aufgerufen (dieselbe Klasse, die auch die Agenten in Schritt 3 intern nutzen, nur ohne die Agent/Task/Crew-Schicht darüber). Das ist die Ausgangsbasis, auf der alle weiteren Schritte aufbauen. Ihr könnt erst dann beurteilen, was eine Technik hinzufügt, wenn ihr gesehen habt, was ihr ohne sie bekommt.

## Hintergrund

„Zero-Shot" bedeutet, dass das Modell keine Beispiele für die erwartete Ausgabe erhält — es muss ausschließlich aus dem antworten, was es während des Trainings gelernt hat. Das ist der Standardmodus für die meisten Menschen, die LLMs nutzen: eine Frage tippen, eine Antwort bekommen.

Ein Large Language Model ist auf der untersten Ebene eine Funktion, die das wahrscheinlichste nächste Token vorhersagt, gegeben einem Kontextfenster mit vorherigen Tokens. Wenn ihr eine einfache Nutzernachricht sendet, bekommt ihr zurück, was das Modell auf Basis seiner Trainingsdaten für am wahrscheinlichsten hält — das ist mächtig, aber vollständig davon abhängig, wie das Thema in den Trainingsdaten vertreten ist.

Kein Zitat nötig. Der Punkt ist empirisch: beobachtet, was ihr bekommt, bevor irgendeine Technik angewendet wird.

## Der Code

Öffnet [step_01_zero_shot_prompting.ipynb](../../en/prompting/step_01_zero_shot_prompting.ipynb) in VS Code/Cursor und wählt den Kernel **"research_crew"** (siehe Haupt-README, Abschnitt "Register the Jupyter kernel"). Die Code-Zelle:

1. Lädt `.env` (für den API-Key und `MODEL`)
2. Ruft `crewai.LLM.call()` mit einer einzigen Nutzernachricht auf
3. Gibt die Antwort aus und speichert sie in `output/step_01.md`

`crewai` ist bereits eine Abhängigkeit dieses Projekts — keine neue Installation nötig. `LLM` ist dieselbe Klasse, die auch die Agenten in Schritt 3–5 intern verwenden — auch Schritt 1 nutzt also schon CrewAI, nur direkt statt über einen Agenten.

## Aufgabe

1. **Wählt euer Thema** — verwendet eines aus der [Anwendungsfall-Tabelle im Haupt-README](../../../README.md#use-cases-to-pick-from), oder schlagt eures vor. Seid spezifisch: "KI im Gesundheitswesen" ist ein Themenbereich; "KI-gestützte Früherkennung von Krebs in der Radiologie" ist ein Thema, für das eine bestimmte Person einen bestimmten Bedarf hätte. **Dieses Thema bleibt für alle 5 Schritte gleich** — der gesamte Sinn ist, den Unterschied zwischen den Schritten zu beobachten, bei gleich gehaltenem Input.

2. Setzt `TOPIC` in der Code-Zelle auf euer Thema.

3. Führt die Zelle aus.

4. Lest die Ausgabe sorgfältig. Notiert:
   - Welche Struktur hat das Modell von sich aus erzeugt, ohne danach gefragt worden zu sein?
   - Wie spezifisch vs. generisch fühlt sich die Ausgabe für euer Thema an?
   - Wie selbstsicher klingt der Ton — wirkt diese Sicherheit verdient, oder ist es Formulierungsroutine ohne echtes Wissen dahinter?

5. Füllt den **Schritt 1**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Führt dieselbe Zelle zweimal mit demselben Thema aus, ohne etwas zu ändern. Wie verschieden sind die zwei Ausgaben? Was bedeutet diese Varianz für jemanden, der einen Workflow baut, der von einer konsistenten Ausgabe abhängt?
