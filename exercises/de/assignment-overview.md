# Team-Aufgabe — Entwerft eure eigene Crew

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-overview.md)

Dies ist die benotete Aufgabe — und sie ist dasselbe wie die Übungsreihe, kein separater Strang daneben. In Teams entwerft ihr eine CrewAI-Crew zu einem Anwendungsfall eurer Wahl, und jeder Sprint vermittelt sowohl ein Konzept als auch baut eure eigene Crew damit aus. Das primäre Abgabeprodukt ist in jeder Phase **euer Entwurf plus eure kritische Einschätzung seiner Risiken und Grenzen** — funktionierender Code ist ein optionaler Bonus, nie eine Pflicht.

**Teamgröße:** 3–5 Studierende. Klein genug, dass alle einen echten Anteil am Ergebnis haben, groß genug, um bis Sprint 4 plausibel drei unterschiedliche Agentenrollen zu besetzen, ohne dass eine Person heimlich alles macht.

Siehe [Vorlagen für die Aufgabe](assignment-templates.md) für die Dokumente, die ihr ausfüllt (`DESIGN.md`, `TEAM.md`, User Stories, Peer Evaluation). Sprint Planning, Definition of Done und was abzugeben ist, sind direkt in die jeweilige Sprint-Seite eingebaut — es gibt keine separate Meilenstein-Leiter oder Sprint-Plan-Datei, auf die ihr verweisen müsstet.

## So funktioniert es: ein Sprint, ein Konzept, ein Teil eurer Crew

| Sprint | Schaltet frei |
| --- | --- |
| [0 — Vision & Architektur](00-vision-architecture.md) | Anwendungsfall wählen, Agenten und Tasks entwerfen |
| [1 — Erster lauffähiger MVP](01-first-mvp.md) | Eine funktionierende sequentielle (oder parallele) Crew |
| [2 — Tools](02-tools.md) | Ein Tool, das euer Anwendungsfall wirklich braucht |
| [3 — RAG](03-rag.md) | Verankerte Antworten aus einer echten Knowledge Source *(Zwischenabgabe fällig)* |
| [4 — Dynamische Orchestrierung (Hierarchisch)](04-dynamic-orchestration.md) | Ein dritter Agent + manager-delegierter Prozess |
| [5 — Produktionssicherheit & Stabilität](05-production-safety.md) | Threat Model, Monitoring-Plan *(Abschlussabgabe fällig)* |

Ihr entwerft nicht jeden Sprint neu — ihr erweitert, was schon da ist. Zwei Abgaben: eine **Zwischenabgabe** am Ende von Sprint 3 (formativ, geringeres Gewicht — fängt schwache Grundlagen früh ab) und eine **Abschlussabgabe** am Ende von Sprint 5 (der vollständige Entwurf plus eine Retrospektive darüber, wie sich euer Denken verändert hat).

## Team-Setup: Repos und Accounts

Dieser Kurs läuft in einer GitHub-Organisation, mit **einem privaten Repository pro Team — nicht eines pro Studierendem.** Ihr legt dieses Repo nicht selbst an; eure Lehrperson hat es bereits aus der Kursvorlage erzeugt, eines pro Team, und gibt eurem Team Zugang dazu, sobald ihr eingeschrieben seid. Siehe den Abschnitt ["Zugang erhalten" im Haupt-README](../../README.md#getting-access-students) für die Einschreibe-Schritte (GitHub-Account → Team-Anmelde-Issue → Einladung annehmen).

**Jedes Teammitglied braucht trotzdem einen eigenen GitHub-Account**, dem Team in der Organisation hinzugefügt (nicht nur direkt einem Repo). Zwei Gründe: Eure einzelnen Commits sind die Grundlage, anhand der der individuelle Beitrag im Team bewertet wird, und eine echte Commit-Historie unter eurem eigenen Account ist über diesen Kurs hinaus etwas wert.

### Zusammenarbeiten ohne Git-Erfahrung

Für die tägliche Teamarbeit braucht ihr keine Branches oder Pull Requests — ein einfacher Ablauf reicht:

1. Bearbeitet eine Datei wie gewohnt (in eurem Codespace).
2. Öffnet das **Source-Control-Panel** (das Verzweigungs-Icon in der Seitenleiste).
3. Schreibt eine kurze Commit-Nachricht, klickt auf **✓ Commit**.
4. Klickt auf **Sync Changes** — das holt in einem Schritt die Änderungen eurer Teammitglieder und schiebt eure eigenen hoch.

Kein Terminal, keine `git add`/`commit`/`push`-Befehle. Alle committen direkt auf `main`.

Um zu vermeiden, dass zwei Personen dieselbe Datei gleichzeitig bearbeiten, **teilt Dateien zwischen Teammitgliedern auf**, wo es geht — z. B. verwaltet eine Person `agents.yaml`, eine andere `tasks.yaml`. `DESIGN.md` ist eine gemeinsame Datei, zu der alle beitragen — wechselt euch dabei ab, oder committet und synct alle paar Minuten, statt lange parallel in derselben Datei zu arbeiten. Falls trotzdem ein Konflikt auftritt, zeigt VS Code eine Merge-Ansicht mit anklickbaren Buttons ("Accept Current / Incoming / Both") — bittet eure Lehrperson einmal um eine kurze Live-Demo davon, damit es niemanden mitten in einer Deadline überrascht.

Für schnelle Änderungen (z. B. einen `DESIGN.md`-Eintrag) könnt ihr Codespaces ganz überspringen: Öffnet die Datei auf github.com, klickt auf das Stift-Icon, bearbeitet sie im Browser und klickt unten auf **"Commit changes"**.

## Abgabepaket

Bei jeder Abgabe-Deadline (Zwischenabgabe: Ende von Sprint 3, Abschluss: Ende von Sprint 5) ist eure Abgabe der Zustand des `main`-Branchs eures Team-Repos:

| Artefakt | Wo | Was es zeigt |
| --- | --- | --- |
| Lauffähige Crew-Konfiguration | `src/research_crew/config/agents.yaml` + `tasks.yaml` (+ `crew.py`, sobald Tools/RAG/Prozess sich ändern) | Die buchstäbliche, lauffähige Version eures Entwurfs |
| Design-Dokument | `DESIGN.md` — Architektur (Agenten/Tasks/Tools/RAG), Risiken, Grenzen, Sicherheit, Produktions-Aspekte, Design-Historie | Eure vollständige, kritisch geprüfte Entwurfsbegründung, in einem sich entwickelnden Bericht |
| Backlog | GitHub Issues (nach Epic gelabelt) + ein Projects-Board | Eure User Stories und euer Fortschritt — lebt auf GitHub, nichts zu exportieren |
| Team-Notizen | `TEAM.md` | Mitglieder und wer was beigetragen hat |
| Optionaler Bonus | ein funktionierendes `crew.py` + ein erfolgreiches `uv run research_crew` | Nur Zusatzpunkte — nie Pflicht |

Die Abgabe ist einfach **der Zustand des `main`-Branchs eures Team-Repos zur Deadline** — es gibt keinen Pull Request zu öffnen. Teilt eure Repo-URL einmal, am Anfang; eure Lehrperson prüft eure Commit-Historie zu jeder Deadline in genau diesem Repo (und kann dafür einen bestimmten Commit taggen).

## Bewertung

Dieselben Gewichtungen gelten für Zwischen- und Abschlussabgabe, bewertet anhand dessen, was bis zur jeweiligen Deadline tatsächlich fertig ist:

| Komponente | Gewicht | Was bewertet wird |
| --- | --- | --- |
| Architektur & Entwurf | 25 % | `agents.yaml`/`tasks.yaml` + `DESIGN.md` §1–2 — passt der Rollensplit wirklich zu eurem Anwendungsfall, statt ein umbenannter Standard zu sein? |
| Risiko- und Grenzenanalyse | 30 % | `DESIGN.md` §3–4 — spezifisch zu eurem Entwurf, wächst über die Sprints, nicht generisch |
| Sicherheit & Produktions-Aspekte | 15 % | `DESIGN.md` §5–6 — ein konkretes Threat Model und ein Monitoring-Plan für *euren* Entwurf, nicht das generische Beispiel aus Sprint 5 |
| Prozess: Backlog & Epics | 15 % | GitHub Issues/Projects-Board — echte User Stories mit Akzeptanzkriterien, Definition of Done tatsächlich genutzt, nicht nur abgehakt |
| Design-Historie & Retrospektive | 15 % | Ehrliche Entwicklung des Denkens über die Sprints hinweg, nicht eine einzige, am Ende glattgeschriebene Antwort |

**Optionaler Bonus:** ein funktionierendes `crew.py` + ein erfolgreiches `uv run research_crew` — bis zu **+10 %** Zusatzpunkte oben auf das Obige. Nie Pflicht, nie ein Ersatz für eine dünne Risikoanalyse.

**Individuelle Anpassung innerhalb der Teamnote:** Der Anteil jedes Studierenden an der Teamnote kann anhand der vertraulichen [Peer Evaluation](assignment-templates.md#peer-evaluation-vertraulich--nicht-ins-repo-committen) um bis zu **±15 %** verschoben werden — direkt an eure Lehrperson geschickt, nie ins Repo committed, damit Feedback ehrlich sein kann.

Jede Sprint-Seite selbst enthält die konkreten Fragen, die in dieser Phase bewertet werden — beantwortet direkt in `DESIGN.md`, nicht als separate "kritisches Denken"-Übung.

## Agile Praxis: Backlog und User Stories

Führt euren Entwurfsprozess wie ein echtes Produkt-Backlog:
- Die neue Fähigkeit jedes Sprints ist ein **Epic**. Brecht es in 2–4 **User Stories** herunter: *"Als [Stakeholder des Crew-Ergebnisses] möchte ich [Fähigkeit], damit [Nutzen]."*
- Schreibt **Akzeptanzkriterien** für jede Story als testbare Bedingungen — diese sind zugleich ein Entwurf für das `expected_output`-Feld des Tasks, sobald ihr beim YAML angelangt seid, was an sich schon eine nützliche Beobachtung ist.
- Fügt jedem Epic "Risiko identifiziert und dokumentiert" zur Definition of Done hinzu, damit Risikoanalyse eine Gewohnheit wird, kein einmaliger Aufsatz.
- Ist euer Team größer als zwei, rotiert die Facilitator-Rolle jeden Sprint.

Vorlagen dafür findet ihr unter [Vorlagen für die Aufgabe](assignment-templates.md). Sprint Planning, Definition of Done und Review sind direkt im "Aufgabe"-Abschnitt jeder Sprint-Seite eingebaut — öffnet die jeweilige Sprint-Seite, wenn ihr sie planen wollt, statt eine separate Sprint-Plan-Datei.

## Für Lehrende

Das ist die einmalige Einrichtung hinter allem oben. GitHub Classroom nimmt seit Mai 2026 keine neuen Anmeldungen mehr an — das hier ersetzt es durch reine GitHub-Organisation-Funktionen, der Free-Plan deckt alles ab (unbegrenzte Mitglieder, unbegrenzte private Repos).

### 1. Organisation und Teams anlegen

Legt eine kostenlose Organisation an, dann **Settings → Teams → New team** einmal pro Projektgruppe (z. B. `team-a`, `team-b`, ...). Optional könnt ihr alle unter einem Parent-Team verschachteln (z. B. `students`), falls ihr ein gemeinsames Ressourcen-Repo wollt, das automatisch für alle sichtbar ist — Child-Teams erben alles, was das Parent-Team sehen kann.

### 2. Dieses Repo als Vorlage markieren, dann ein Repo pro Team erzeugen

Dieses Repo: **Settings → "Template repository" anhaken**. Dann pro Team:
```bash
gh repo create <org>/<team-slug>-crew --template <org>/<dieses-repo> --private
gh api repos/<org>/<team-slug>-crew/teams/<team-slug> -X PUT -f permission=admin
```
**Admin** (nicht nur Write) ist hier wichtig — das Verwalten der Secrets eines Repos braucht Admin, und ihr wollt, dass jedes Team seine API-Schlüssel selbst einrichten kann, ohne dass ihr dazwischen müsst.

### 3. Codespaces für die Organisation aktivieren

**Org Settings → Codespaces → General** → für alle Repositories aktivieren (oder gezielt die Team-Repos auswählen). Im Free-Plan rechnet Codespaces-Nutzung gegen das persönliche kostenlose Kontingent jedes Studierenden, nicht gegen die Organisation — kein Spending-Limit einzurichten.

### 4. Team-Einschreibung einrichten: Studierende reichen ein, ihr entscheidet, ein Workflow führt aus

Studierende reichen ihre **E-Mail und ihren GitHub-Benutzernamen** über ein [Team-Anmelde-Issue](../../.github/ISSUE_TEMPLATE/team-signup.yml) auf diesem Repo ein. Das allein bewirkt nichts außer einer Benachrichtigung an euch — **ihr entscheidet die Team-Zuweisung selbst**, indem ihr ein Label vergebt, und ein [Workflow](../../.github/workflows/add-to-team.yml) übernimmt den mechanischen Teil (zum Team hinzufügen, antworten, Issue schließen).

1. **Erstellt ein Label pro Team**, exakt benannt `team:<team-slug>` (z. B. `team:team-a`) — **Issues → Labels → New label**, einmal pro Team.
2. **Erstellt das Token für die Automatisierung**: ein Personal Access Token mit **Organization → Members: Read and write** und **Repository → Issues: Read and write** (fine-grained), oder `admin:org` + `repo` (classic) — nötig, weil Team-Mitgliedschaft eine Organisations-Berechtigung ist, die der Standard-`GITHUB_TOKEN` nicht vergeben kann.
3. Fügt es als Secret namens `ORG_ADMIN_TOKEN` hinzu — entweder auf diesem Repo selbst (**Settings → Secrets and variables → Actions**) oder auf Organisationsebene, beschränkt auf dieses Repo (**Org Settings → Secrets and variables → Actions**).
4. **Bei jeder neuen Anmeldung**: Das Issue bekommt automatisch einen Kommentar, der euch erinnert, das passende Team-Label zu vergeben. Öffnet das Issue, findet anhand der E-Mail heraus, wer das in eurer eigenen Team-Liste ist, und vergebt `team:<deren-Team-Slug>` — dieses Label *ist* der Auslöser; der Workflow liest es, fügt den Benutzernamen hinzu, antwortet und schließt das Issue. Falscher Benutzername oder Label-Tippfehler? Korrigieren und das Label erneut vergeben, um es noch einmal zu versuchen.

### 5. Laufend: Abgaben prüfen

Prüft die Commit-Historie jedes Teams auf `main` zu jeder Deadline — taggt selbst einen bestimmten Commit (Releases → "Create a new release"), wenn ihr einen unveränderlichen Stand für die Bewertung wollt. Musterlösungen sind bewusst nicht enthalten, wie im Rest dieser Reihe.
