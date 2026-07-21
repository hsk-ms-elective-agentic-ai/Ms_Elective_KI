# Team-Aufgabe — Bewertet die Progression

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-overview.md)

Dies ist die benotete Aufgabe — und sie ist dasselbe wie die Übungsreihe, kein separater Strang daneben. In Teams arbeitet ihr euch durch fünf Versionen desselben KI-Systems mit demselben Thema, fügt bei jedem Schritt eine Schicht hinzu, und bewertet, was jede Schicht tatsächlich verändert. Das primäre Abgabeprodukt ist `EVALUATION.md`: eine vergleichende Analyse dessen, was ihr beobachtet habt und was das für euren Anwendungsfall bedeutet.

**Teamgröße:** 3–5 Studierende.

Vorlagen für die Dokumente, die ihr ausfüllt (`EVALUATION.md`, `TEAM.md`, Peer Evaluation), sind im [Vorlagen-Dokument](assignment-templates.md) enthalten.

## So funktioniert es: ein Schritt, eine Schicht, ein Vergleich

| Schritt | Fügt hinzu |
| --- | --- |
| [1 — Zero-Shot-Prompting](../../exercises/en/step_01_zero_shot_prompting.ipynb) | Der bloße API-Aufruf — eure Ausgangsbasis |
| [2 — Prompt-Vorlage](../../exercises/en/step_02a_few_shot.ipynb) | Eine Rolle + Ausgabeformat, derselbe Aufruf |
| [3 — Einzelner Agent](../../exercises/en/step_03_single_agent.ipynb) | Die CrewAI-Framework-Schleife *(Zwischenabgabe fällig)* |
| [4 — Multi-Agent](../../exercises/en/step_04_multi_agent.ipynb) | Rollenspezialisierung + Ausgaben-Verkettung |
| [5 — Tools, MCP & RAG](../../exercises/en/step_05a_tools.ipynb) | Externe Verankerung: Websuche, ein MCP-Server, Dokumenten-Retrieval *(Abschlussabgabe fällig)* |

Ihr entwerft zwischen den Schritten nichts neu — ihr fügt jedes Mal ein Teil hinzu und führt es mit demselben Thema aus. Zwei Abgaben: eine **Zwischenabgabe** nach Schritt 3 und eine **Abschlussabgabe** nach Schritt 5.

## Team-Setup: Repos und Accounts

Dieser Kurs läuft in einer GitHub-Organisation, mit **einem privaten Repository pro Team — nicht eines pro Studierenden.** Ihr legt dieses Repo nicht selbst an; eure Lehrperson erzeugt es aus der Kursvorlage, eines pro Team, und gibt eurem Team Zugang, sobald ihr eingeschrieben seid. Siehe den Abschnitt ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students) für die Einschreibe-Schritte.

**Jedes Teammitglied braucht trotzdem einen eigenen GitHub-Account**, der dem Team in der Organisation hinzugefügt wurde. Eure einzelnen Commits sind die Grundlage, anhand der der individuelle Beitrag im Team bewertet wird.

### Zusammenarbeiten ohne Git-Erfahrung

Ein Branch pro Schritt, ein Pull Request, um ihn abzuschließen — darüber hinaus ist die tägliche Arbeit derselbe einfache Ablauf wie direktes Committen auf `main`:

1. **Zu Beginn jedes Schritts** erstellt ihr einen Branch namens `sprint-<N>` (z. B. `sprint-2`): klickt auf den Branch-Namen unten links in VS Code → **Create new branch...**. Das ganze Team arbeitet für den Rest des Schritts auf diesem einen Branch.
2. Bearbeitet eine Datei wie gewohnt (in VS Code/Cursor).
3. Öffnet das **Source-Control-Panel** (das Verzweigungs-Icon in der Seitenleiste).
4. Schreibt eine kurze Commit-Nachricht, klickt auf **✓ Commit**.
5. Klickt auf **Sync Changes** — das holt in einem Schritt die Änderungen eurer Teammitglieder und schiebt eure eigenen hoch.
6. **Am Ende des Schritts** öffnet ihr einen Pull Request von `sprint-<N>` nach `main` — GitHub zeigt auf github.com direkt nach dem Pushen eines neuen Branches ein "Compare & pull request"-Banner an, oder ihr nutzt das **GitHub Pull Requests**-Panel in VS Code. Skim den Diff als Team, und mergt ihn selbst — keine Freigabe nötig. Den nächsten Schritt startet ihr, indem ihr `sprint-<N+1>` vom dann aktualisierten `main` abzweigt.

Kein Terminal, keine `git add`/`commit`/`push`/`merge`-Befehle.

**Teilt Dateien zwischen Teammitgliedern auf**, wo es geht — z. B. führt eine Person Schritt 3 aus und schreibt diesen Abschnitt in `EVALUATION.md`, eine andere Schritt 4. `EVALUATION.md` ist eine gemeinsame Datei, zu der alle beitragen — wechselt euch ab, oder committet und synct alle paar Minuten, statt lange parallel daran zu arbeiten.

Für schnelle Änderungen, ohne eure lokale Umgebung zu öffnen: Öffnet die Datei auf github.com, wechselt im Branch-Dropdown auf euren aktuellen `sprint-<N>`-Branch, klickt auf das Stift-Icon und bearbeitet sie im Browser.

## Abgabepaket

Bei jeder Abgabe-Deadline (Zwischenabgabe: nach Schritt 3, Abschluss: nach Schritt 5) ist eure Abgabe der Zustand des `main`-Branchs eures Team-Repos:

| Artefakt | Wo | Was es zeigt |
| --- | --- | --- |
| Evaluierungsdokument | `EVALUATION.md` — schrittweise Beobachtungen, Vergleiche, abschließende Empfehlung | Eure tatsächliche vergleichende Analyse, spezifisch auf euer Thema bezogen |
| Code-Änderungen | Änderungen an den Übungsskripten (z. B. TOPIC, eigene Knowledge-Sources) | Was ihr tatsächlich ausgeführt habt |
| Schritt-Historie | ein gemergter Pull Request pro Schritt (`sprint-<N>` → `main`) | Ein prüfbarer Diff, was sich in jedem Schritt verändert hat |
| Team-Notizen | `TEAM.md` | Mitglieder und wer was beigetragen hat |

Die Kette der gemergten Sprint-PRs ist das, was eure Lehrperson liest, um den Fortschritt zu verfolgen. Nutzt die PR-Beschreibung, um zu notieren, was ihr ausgeführt und was ihr festgestellt habt.

## Bewertung

Dieselben Gewichtungen gelten bei Zwischen- und Abschlussabgabe, bewertet gegen das, was bis zu dieser Deadline abgeschlossen ist:

| Komponente | Gewicht | Was bewertet wird |
| --- | --- | --- |
| Evaluierungsqualität | 40% | `EVALUATION.md` — sind die Schrittvergleiche spezifisch und ehrlich? Werden echte Unterschiede identifiziert, nicht nur "es ist besser"? |
| Kritische Reflexion | 30% | Versteht das Team *warum* sich jeder Schritt unterscheidet? Wird es auf das spezifische Thema bezogen statt generisch beantwortet? |
| Abschließende Empfehlung | 20% | Ist die Empfehlung für den eigenen Anwendungsfall begründet und spezifisch — nicht "RAG + Tools ist immer das Beste"? |
| Prozess (PRs, Team) | 10% | Ein sauberer PR pro Schritt, alle Teammitglieder tragen bei, PR-Beschreibungen geben an, was ausgeführt wurde |

**Optionaler Bonus:** ein funktionierendes eigenes Setup (angepasste Agenten, eigene Knowledge-Source, verschiedene Themen-Varianten getestet) — bis zu **+10%** Zusatzpunkte. Nie Pflicht, nie Ersatz für eine dünne Evaluierung.

**Individuelle Anpassung innerhalb der Teamnote:** der Anteil jedes Studierenden an der Teamnote kann sich um bis zu **±15%** verschieben, basierend auf der privaten [Peer Evaluation](assignment-templates.md#peer-evaluation-privat--nicht-in-das-repo-committen) — direkt an eure Lehrperson eingereicht, nie ins Repo committed.

## Für Lehrende

Das ist das einmalige Setup hinter allem oben. GitHub Classroom hat im Mai 2026 keine neuen Anmeldungen mehr aufgenommen, daher ersetzt dies es durch einfache GitHub-Organisations-Features — Free-Plan deckt alles ab.

### 1. Organisation und Teams anlegen

Free-Organisation anlegen, dann **Settings → Teams → New team** einmal pro Projektgruppe (z. B. `team-a`, `team-b`, ...). Optional alle unter einem übergeordneten Team verschachteln (z. B. `students`), damit ein gemeinsames Ressourcen-Repo automatisch für alle sichtbar ist.

### 2. Repo als Template markieren, dann eines pro Team erzeugen

**Settings → "Template repository" ankreuzen**. Dann pro Team:
```bash
gh repo create <org>/<team-slug>-crew --template <org>/<this-repo> --private
gh api repos/<org>/<team-slug>-crew/teams/<team-slug> -X PUT -f permission=admin
```
**Admin** (nicht nur Write) ist wichtig — Repo-Secrets zu verwalten erfordert Admin, und ihr wollt, dass jedes Team seine eigenen API-Keys ohne eure Beteiligung einrichten kann.

### 3. Team-Einschreibung einrichten: Studierende reichen ein, ihr entscheidet, ein Workflow führt aus

Studierende reichen ihre **E-Mail und ihren GitHub-Benutzernamen** über ein [Team-Anmelde-Issue](../../.github/ISSUE_TEMPLATE/team-signup.yml) ein. Das allein tut nichts außer euch zu benachrichtigen — **ihr entscheidet die Team-Zuweisung selbst**, indem ihr ein Label anwendet, und ein [Workflow](../../.github/workflows/add-to-team.yml) erledigt den mechanischen Teil.

1. **Erstellt ein Label pro Team**, genau benannt `team:<team-slug>` — **Issues → Labels → New label**, einmal pro Team.
2. **Erstellt das Token der Automatisierung**: ein Personal Access Token mit **organization → Members: Read and write** und **repository → Issues: Read and write** Scopes (fine-grained), oder `admin:org` + `repo` (classic).
3. Als Secret namens `ORG_ADMIN_TOKEN` hinzufügen.
4. **Issues triagieren**: Issue öffnen, `team:<team-slug>` anwenden — der Workflow fügt den Benutzernamen hinzu, antwortet und schließt das Issue.

### 4. Laufend: Abgaben bewerten

Jedes Team mergt einen Pull Request pro Schritt (`sprint-<N>` → `main`) — bewertet den Diff dieses PRs direkt auf GitHub (**Pull requests → Closed**). Bewertet zum Deadline-Zeitpunkt gegen den Zustand von `main`, mit der Kette gemergter Sprint-PRs als schrittweiser Nachweis. Musterlösungen sind bewusst nicht enthalten.
