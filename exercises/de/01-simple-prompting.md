# Schritt 1 — Einfaches Prompting

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/01-simple-prompting.md)

Der direkteste Weg von Frage zu Antwort: ein API-Aufruf, eine Nachricht, eine Antwort. Keine Rollendefinition, kein Ausgabeformat, kein Framework — nur das Modell und euer Text. Das ist die Ausgangsbasis, auf der alle weiteren Schritte aufbauen. Ihr könnt erst dann beurteilen, was ein Framework hinzufügt, wenn ihr gesehen habt, was ihr ohne es bekommt.

## Hintergrund

Ein Large Language Model ist auf der untersten Ebene eine Funktion, die das wahrscheinlichste nächste Token vorhersagt, gegeben einem Kontextfenster mit vorherigen Tokens. Wenn ihr eine einfache Nutzernachricht sendet, bekommt ihr zurück, was das Modell auf Basis seiner Trainingsdaten für am wahrscheinlichsten hält — das ist mächtig, aber vollständig davon abhängig, wie das Thema in den Trainingsdaten vertreten ist.

Kein Zitat nötig. Der Punkt ist empirisch: beobachtet, was ihr bekommt, bevor ihr irgendeine Struktur hinzufügt.

## Der Code

Öffnet [src/exercises/step_01_simple_prompting.py](../../src/exercises/step_01_simple_prompting.py). Die Datei hat ca. 15 Zeilen:

1. Lädt `.env` (für `GROQ_API_KEY` und `MODEL`)
2. Ruft `litellm.completion()` mit einer einzigen Nutzernachricht auf
3. Gibt die Antwort aus

`litellm` ist bereits eine Abhängigkeit dieses Projekts (es ist die Routing-Schicht, die denselben Code mit Groq, DeepSeek, OpenAI und anderen arbeiten lässt) — keine neue Installation nötig.

## Aufgabe

1. **Wählt euer Thema** — verwendet eines aus der [Anwendungsfall-Tabelle im Haupt-README](../../README.md#use-cases-to-pick-from), oder schlagt eures vor. Seid spezifisch: "KI im Gesundheitswesen" ist ein Themenbereich; "KI-gestützte Früherkennung von Krebs in der Radiologie" ist ein Thema, für das eine bestimmte Person einen bestimmten Bedarf hätte. **Dieses Thema bleibt für alle 5 Schritte gleich** — der gesamte Sinn ist, den Unterschied zwischen den Schritten zu beobachten, bei gleich gehaltenem Input.

2. Setzt `TOPIC` in der Datei auf euer Thema.

3. Führt es aus:
   ```bash
   uv run python src/exercises/step_01_simple_prompting.py
   ```

4. Lest die Ausgabe sorgfältig. Notiert:
   - Welche Struktur hat das Modell von sich aus erzeugt, ohne danach gefragt worden zu sein?
   - Wie spezifisch vs. generisch fühlt sich die Ausgabe für euer Thema an?
   - Wie selbstsicher klingt der Ton — wirkt diese Sicherheit verdient, oder ist es Formulierungsroutine ohne echtes Wissen dahinter?

5. Füllt den **Schritt 1**-Abschnitt in `EVALUATION.md` aus.

## Zusatzaufgabe

Führt dasselbe Skript zweimal mit demselben Thema aus. Wie verschieden sind die zwei Ausgaben? Was bedeutet diese Varianz für jemanden, der einen Workflow baut, der von einer konsistenten Ausgabe abhängt?
