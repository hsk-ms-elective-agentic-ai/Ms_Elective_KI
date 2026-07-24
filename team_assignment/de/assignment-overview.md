# Team-Aufgabe — Bewertet die Progression

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-overview.md)

Dies ist die benotete Aufgabe — und sie ist dasselbe wie die Übungsreihe, kein separater Strang daneben. In Teams arbeitet ihr euch durch eine Abfolge von Versionen desselben KI-Systems mit demselben Thema, organisiert in fünf Sprints, fügt bei jedem Sprint eine Schicht hinzu, und bewertet, was jede Schicht tatsächlich verändert. Das primäre Abgabeprodukt ist `REPORT.md`: ein vollständiger Projektbericht — Architektur, Implementierungsentscheidungen, Evaluierung und ethische Überlegungen — für den Agenten, den euer Team entwirft und baut, informiert durch alles, was ihr beim Durchlaufen der Übungs-Sprints beobachtet.

**Teamgröße:** 3–5 Studierende.

Vorlagen für die Dokumente, die ihr ausfüllt (`REPORT.md`, `TEAM.md`, Peer Evaluation), sind im [Vorlagen-Dokument](assignment-templates.md) enthalten.

## So funktioniert es: ein Sprint, eine Schicht, ein Vergleich

| Sprint | Schritte | Fügt hinzu |
| --- | --- | --- |
| 1 | [Schritt 03 — Zero-Shot-Prompting](../../exercises/en/step_03_zero_shot_prompting.ipynb) | Der bloße API-Aufruf — eure Ausgangsbasis |
| 2 | [Schritte 04–08 — Prompting-Techniken](../../exercises/en/step_04_few_shot.ipynb) | Eine Rolle + Ausgabeformat, derselbe Aufruf |
| 3 | [Schritt 09 — Einzelner Agent](../../exercises/en/step_09_single_agent.ipynb) | Die CrewAI-Framework-Schleife *(Zwischenabgabe fällig)* |
| 4 | [Schritte 10–12 — Tools, MCP & RAG](../../exercises/en/step_10_tools.ipynb) | Externe Verankerung: Websuche, ein MCP-Server, Dokumenten-Retrieval |
| 5 | [Schritt 13 — Multi-Agent](../../exercises/en/step_13_multi_agent_seq.ipynb) | Rollenspezialisierung + Ausgaben-Verkettung *(Abschlussabgabe fällig)* |

Ihr entwerft zwischen den Sprints nichts neu — ihr fügt jedes Mal ein Teil hinzu und führt es mit demselben Thema aus. Zwei Abgaben: eine **Zwischenabgabe** nach Schritt 09 (Sprint 3), die eine kurze Zwischenpräsentation enthält, und eine **Abschlussabgabe** nach Schritt 13 (Sprint 5).

## Team-Setup: Repos und Accounts

Dieser Kurs läuft in einer GitHub-Organisation, mit **einem privaten Repository pro Team — nicht eines pro Studierenden.** Ihr legt dieses Repo nicht selbst an; eure Lehrperson erzeugt es aus der Kursvorlage, eines pro Team, und gibt eurem Team Zugang, sobald ihr eingeschrieben seid. Siehe den Abschnitt ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students) für die Einschreibe-Schritte.

**Jedes Teammitglied braucht trotzdem einen eigenen GitHub-Account**, der dem Team in der Organisation hinzugefügt wurde. Eure einzelnen Commits sind die Grundlage, anhand der der individuelle Beitrag im Team bewertet wird.

### Zusammenarbeiten ohne Git-Erfahrung

Ein Branch pro Sprint, ein Pull Request, um ihn abzuschließen — darüber hinaus ist die tägliche Arbeit derselbe einfache Ablauf wie direktes Committen auf `main`:

1. **Zu Beginn jedes Sprints** erstellt ihr einen Branch namens `sprint-<N>` (z. B. `sprint-2`): klickt auf den Branch-Namen unten links in VS Code → **Create new branch...**. Das ganze Team arbeitet für den Rest des Sprints auf diesem einen Branch.
2. Bearbeitet eine Datei wie gewohnt (in VS Code/Cursor).
3. Öffnet das **Source-Control-Panel** (das Verzweigungs-Icon in der Seitenleiste).
4. Schreibt eine kurze Commit-Nachricht, klickt auf **✓ Commit**.
5. Klickt auf **Sync Changes** — das holt in einem Schritt die Änderungen eurer Teammitglieder und schiebt eure eigenen hoch.
6. **Am Ende des Sprints** öffnet ihr einen Pull Request von `sprint-<N>` nach `main` — GitHub zeigt auf github.com direkt nach dem Pushen eines neuen Branches ein "Compare & pull request"-Banner an, oder ihr nutzt das **GitHub Pull Requests**-Panel in VS Code. Skim den Diff als Team, und mergt ihn selbst — keine Freigabe nötig. Den nächsten Sprint startet ihr, indem ihr `sprint-<N+1>` vom dann aktualisierten `main` abzweigt.

Kein Terminal, keine `git add`/`commit`/`push`/`merge`-Befehle.

**Teilt Dateien zwischen Teammitgliedern auf**, wo es geht — z. B. führt eine Person Schritt 09 aus und entwirft den Architektur-Abschnitt von `REPORT.md`, eine andere Schritt 10 und den Tools-Unterabschnitt. `REPORT.md` ist eine gemeinsame Datei, zu der alle beitragen — wechselt euch ab, oder committet und synct alle paar Minuten, statt lange parallel daran zu arbeiten.

Für schnelle Änderungen, ohne eure lokale Umgebung zu öffnen: Öffnet die Datei auf github.com, wechselt im Branch-Dropdown auf euren aktuellen `sprint-<N>`-Branch, klickt auf das Stift-Icon und bearbeitet sie im Browser.

## Agil arbeiten als Team: Sprints, User Stories & Issues

*(Falls eure separate Agile-Vorlesung Scrum/Kanban-Theorie schon behandelt hat, springt direkt zu "Einmaliges Setup" unten — dieser Abschnitt ist nur das "Wie" in GitHub.)*

Über die Git-Mechanik oben hinaus muss euer Team auch planen und nachverfolgen, *was* ihr in jedem Sprint baut — nicht nur Code pushen. Ihr führt diesen Kurs bereits als fünf Sprints durch (Tabelle oben) — dieser Abschnitt zeigt, wie ihr jeden davon so durchführt, wie es ein agiles Team tun würde, mit GitHubs eigenem Issue-Tracker statt einem separaten Tool.

Ein kurzer Begriffs-Brückenschlag, falls die Vorlesung das noch nicht behandelt hat:

- **User Story** — ein konkretes, abschließbares Stück Arbeit, idealerweise formuliert als *"Als ___ möchte ich ___, damit ___."* Ein Sprint zerfällt in ungefähr 3–6 davon.
- **Backlog** — alles, was noch nicht erledigt ist: offene Issues, die noch nicht in Arbeit sind.
- **Board** — eine visuelle Ansicht, wie Stories durch Zustände wandern (To do → In progress → Done).

Das ist schon das gesamte Vokabular — die Begründung hinter Sprints, dem Aufteilen von Stories oder Schätzungen behandelt die separate Agile-Vorlesung. Hier geht es nur darum, das auf GitHub-Features zu verdrahten, die ihr schon habt:

| Agile-Konzept | GitHub-Feature | So nutzt ihr es |
| --- | --- | --- |
| Sprint | Milestone | Ein Milestone pro Sprint: `Sprint 1` … `Sprint 5` |
| User Story | Issue | Ein Issue pro konkreter Aufgabe; formuliert den Titel als Story, wo es passt |
| Sprint-Backlog & Board | Project (Board-Ansicht) | Spalten: Backlog → To do → In progress → In review → Done |
| "Dieser Code schließt diese Story ab" | PR-Beschreibung | `Closes #12` in eurem `sprint-<N>`-PR — Mergen schließt das Issue automatisch |

### Einmaliges Setup (macht das zu Beginn von Sprint 1)

1. **Milestones** — **Issues → Milestones → New milestone**, einmal pro Sprint: `Sprint 1` … `Sprint 5`. Fügt die "Fügt hinzu"-Zelle des jeweiligen Sprints aus der Tabelle oben als Beschreibung ein.
2. **Project-Board** — **Projects → New project → Board**. Fügt die Spalten `Backlog`, `To do`, `In progress`, `In review`, `Done` hinzu.
3. **Issue-Vorlage** — dieses Repo bringt bereits eine *User story*-Issue-Vorlage mit (**New issue → User story**): [`.github/ISSUE_TEMPLATE/user-story.yml`](../../.github/ISSUE_TEMPLATE/user-story.yml). Sie füllt die Als/möchte ich/damit-Form plus Akzeptanzkriterien vor.

### Einen Sprint durchführen

1. **Sprint Planning** (Sprint-Beginn, ~15 Min., ganzes Team): lest die "Fügt hinzu"-Zelle des Sprints aus der Tabelle oben noch einmal, und teilt sie in 3–6 Issues mit der *User story*-Vorlage auf. Setzt bei jedem den Milestone auf den aktuellen Sprint, weist eine verantwortliche Person zu und legt es in "To do".
2. **Während des Sprints**: bewegt eure eigenen Issues beim Arbeiten über das Board (`To do` → `In progress` → `In review` → `Done`) und referenziert die Issue-Nummer in Commits (`#12`), damit die Historie nachvollziehbar bleibt.
3. **Sprint Review** (Sprint-Ende, direkt vor dem Öffnen des PRs): geht das Board gemeinsam als Team durch — alles in `Done` sollte im Diff sichtbar sein, den ihr gleich mergt; alles Unfertige wandert ins Backlog des nächsten Sprints, statt den PR zu blockieren.
4. **Kreis schließen**: schreibt `Closes #12` (und weitere) in die Beschreibung eures `sprint-<N>` → `main`-PRs — das Mergen schließt diese Issues automatisch und komplettiert den Milestone.

## Abgabepaket

Bei jeder Abgabe-Deadline (Zwischenabgabe: nach Schritt 09, Abschluss: nach Schritt 13) ist eure Abgabe der Zustand des `main`-Branchs eures Team-Repos:

| Artefakt | Wo | Was es zeigt |
| --- | --- | --- |
| Berichtsdokument | `REPORT.md` — Sprint-Fortschritt, Architektur, Implementierung, Evaluierung und Ethik eures eigenen Agenten | Euer tatsächlicher Projektbericht, spezifisch auf euer Thema bezogen |
| Code-Änderungen | Änderungen an den Übungsskripten (z. B. TOPIC, eigene Knowledge-Sources) | Was ihr tatsächlich ausgeführt habt |
| Sprint-Historie | ein gemergter Pull Request pro Sprint (`sprint-<N>` → `main`) | Ein prüfbarer Diff, was sich in jedem Sprint verändert hat |
| Team-Notizen | `TEAM.md` | Mitglieder und wer was beigetragen hat |

Die Kette der gemergten Sprint-PRs ist das, was eure Lehrperson liest, um den Fortschritt zu verfolgen. Nutzt die PR-Beschreibung, um zu notieren, was ihr ausgeführt und was ihr festgestellt habt.

Die Zwischen- und Abschlusspräsentation (siehe Bewertung unten) sind keine Repo-Artefakte — sie sind Live-Vorträge, dafür wird nichts committed.

## Bewertung

Die Abschlussnote setzt sich aus drei Komponenten zusammen:

| Komponente | Gewicht | Was bewertet wird |
| --- | --- | --- |
| Zwischenpräsentation | 10% | Ein kurzer Live-Rundgang durch den bisherigen Fortschritt, gehalten bei der Zwischenabgabe (nach Schritt 09, Sprint 3) — was ihr gebaut habt, was ihr gelernt habt, und was für die verbleibenden Sprints geplant ist. Jedes Teammitglied sollte mindestens einen Teil vortragen. |
| Bericht (`REPORT.md`) | 70% | Siehe Aufschlüsselung unten. Wird einmalig bei der Abschlussabgabe bewertet. |
| Abschlusspräsentation | 20% | Ein Live-Rundgang durch euren Agenten im Kurs — was er macht, warum ihr ihn so gebaut habt, und eine Live-Demo, die tatsächlich läuft. Jedes Teammitglied sollte mindestens einen Teil vortragen. Plant etwa 10 Minuten + Fragerunde ein (eure Lehrperson kann das an die Kursgröße anpassen); eine funktionierende Live-Demo ist klar bevorzugt, bereitet aber eine kurze aufgezeichnete Rückfalllösung vor, falls während des Vortrags API-Probleme auftreten. Kein separates File zum Einreichen — das passiert live in der letzten Kurssitzung, nach der Abschlussabgabe-Deadline. |

Die 70% des Berichts schlüsseln sich weiter in vier Unterkriterien auf:

| Unterkriterium | Gewicht (der Gesamtnote) | Was bewertet wird |
| --- | --- | --- |
| Berichtsqualität | 28% | `REPORT.md` — ist die Analyse spezifisch und ehrlich, verankert im tatsächlichen Verhalten eures eigenen Agenten und den durchgeführten Übungsschritten, nicht generisch? |
| Kritische Reflexion | 21% | Versteht das Team *warum* jede Design-Entscheidung wichtig ist? Wird es auf das spezifische Thema und den eigenen Agenten bezogen statt generisch beantwortet? |
| Design & Fazit | 14% | Ist die Architektur des Agenten (Abschnitt 3) begründet und spezifisch für den eigenen Anwendungsfall — nicht "RAG + Tools ist immer das Beste" — und bewertet das Fazit (Abschnitt 8) ehrlich, ob die Ziele erreicht wurden? |
| Prozess (PRs, Team) | 7% | Ein sauberer PR pro Sprint, alle Teammitglieder tragen bei, PR-Beschreibungen geben an, was ausgeführt wurde, die Sprint-Fortschritt-Tabelle in `REPORT.md` wird sprintweise aktuell gehalten |

**Optionaler Bonus:** eine funktionierende Implementierung, die durchgängig läuft (`crew.kickoff()` schließt ohne Fehler ab, der Code ist einigermaßen sauber strukturiert und stimmt mit dem überein, was `REPORT.md` beschreibt), und/oder ein funktionierendes eigenes Setup (angepasste Agenten, eigene Knowledge-Source, verschiedene Themen-Varianten getestet) — zusammen bis zu **+10%** Zusatzpunkte. Nie Pflicht, nie Ersatz für eine dünne Evaluierung.

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

Jedes Team mergt einen Pull Request pro Sprint (`sprint-<N>` → `main`) — bewertet den Diff dieses PRs direkt auf GitHub (**Pull requests → Closed**). Bewertet zum Deadline-Zeitpunkt gegen den Zustand von `main`, mit der Kette gemergter Sprint-PRs als schrittweiser Nachweis. Musterlösungen sind bewusst nicht enthalten.
