# Vorlagen für die Aufgabe

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-templates.md)

**`DESIGN.md` und `TEAM.md` liegen bereits im Wurzelverzeichnis eures Repos** — jede "Use this template"-Kopie eines Teams startet bereits mit diesen Dateien, genau wie mit `knowledge/user_preference.txt` oder `.env.example`. Füllt sie direkt aus, statt sie neu anzulegen; sie sind unten zur Referenz noch einmal abgedruckt. Das User-Story-Format weiter unten ist für GitHub Issues, die ihr selbst anlegt — dafür gibt es keine Datei. Siehe [Überblick zur Aufgabe](assignment-overview.md) dafür, wie sie genutzt werden — die jeweilige Sprint-Seite (beginnend bei [Sprint 0](00-vision-architecture.md)) sagt euch, was in welcher Phase hineingehört.

## `DESIGN.md`

Das ist der Hauptbericht: ein strukturiertes Design-Dokument für die Architektur eurer Crew, das festhält, was ihr gebaut habt, warum, und was schiefgehen könnte. Füllt jeden Abschnitt aus, sobald der jeweilige Sprint ihn freischaltet — markiert spätere Abschnitte mit "noch nicht" statt sie zu löschen. Speziell für die Tabellen **Risiken**, **Grenzen** und **Design-Historie**: Das ist append-only — fügt pro Sprint neue Zeilen hinzu, bearbeitet oder löscht nie eine vorherige Zeile. Falls ein späterer Sprint eure Einschätzung ändert, fügt stattdessen eine neue Zeile hinzu, die das Update vermerkt.

```markdown
# Crew-Design-Dokument

**Team:** [Teamname] · **Thema:** [Thema eurer Crew] · **Zuletzt aktualisiert:** [Sprint, JJJJ-MM-TT]

## 1. Überblick
- **Problem / Ziel:** Wofür ist diese Crew, in ein bis zwei Sätzen?
- **Stakeholder:** Wer liest das Ergebnis, und was braucht diese Person davon?

## 2. Architektur

**Prozess:** `Process.sequential` oder `Process.hierarchical` — und warum dieser, nicht der andere.

### Agenten
| Agent | Rolle | Ziel | Verantwortlich für welche(n) Task(s) |
| --- | --- | --- | --- |
| | | | |

### Tasks
| Task | Beschreibung (kurz) | Erwartete Ausgabe | Agent | Abhängig von (`context`) |
| --- | --- | --- | --- | --- |
| | | | | |

### Tools
| Tool | Zweck | Warum dieses Tool für dieses Thema | Braucht API-Key / Embeddings? | Was passiert bei einem Ausfall |
| --- | --- | --- | --- | --- |
| | | | | |

### Knowledge Sources / RAG
*(bis Sprint 3 als "noch nicht hinzugefügt" stehen lassen)*

| Quelle | Typ | Warum dieser Inhalt | Embedder | Bekannte Lücken (was NICHT abgedeckt ist) |
| --- | --- | --- | --- | --- |
| | | | | |

### Guardrails / Vertrauensmechanismen
*(bis Sprint 5 als "noch keine" stehen lassen)*
-

## 3. Risiken
*(append-only — pro Sprint neue Zeilen hinzufügen, alte nie bearbeiten)*

| # | Sprint | Risiko | Wo es auftritt (Agent/Task/Tool/RAG) | Mitigation oder akzeptierter Kompromiss |
| --- | --- | --- | --- | --- |
| | | | | |

## 4. Grenzen (Constraints)
*(append-only — pro Sprint neue Zeilen hinzufügen, alte nie bearbeiten)*

| # | Sprint | Grenze | Typ (Rate-Limit / Kosten / Latenz / Daten / Zeit / Team) | Wie der Entwurf sie berücksichtigt |
| --- | --- | --- | --- | --- |
| | | | | |

## 5. Sicherheit & Threat Model
*(bis Sprint 5 — Abschlussabgabe — vollständig ausfüllen)*
- Konkretes, zu diesem Entwurf passendes Prompt-Injection-Szenario:
- Umgang mit Secrets:
- Umfang der Tool-Berechtigungen:

## 6. Produktions-Aspekte
*(bis Sprint 5 — Abschlussabgabe — ausfüllen)*
- Was ihr überwachen würdet:
- Was euch auf einen Ausfall hinweisen würde:
- Was für echten Produktionseinsatz noch fehlt:

## 7. Betrachtete Alternativen
- Welchen anderen Entwurf habt ihr erwogen (anderer Prozess, anderes Tool, kein RAG, anderer Rollensplit), und warum habt ihr ihn verworfen?

## 8. Design-Historie
*(append-only — ein Eintrag pro Sprint, nie einen vorherigen Eintrag bearbeiten)*

### Sprint 0 — Baseline (JJJJ-MM-TT)
**Geändert:**
**Warum:**

### Sprint 2 — Tools (JJJJ-MM-TT)
**Geändert:**
**Warum:**
```

Bei der Abschlussabgabe sollte der letzte Design-Historie-Eintrag konkret beantworten: *Was hat sich zwischen eurer Zwischen- und Abschlussabgabe verändert, und was habt ihr gelernt, das euch zur Änderung bewogen hat?*

## User Story (pro Epic, als GitHub Issue)

```markdown
**Story:** Als [Stakeholder des Crew-Ergebnisses] möchte ich [Fähigkeit], damit [Nutzen].

**Akzeptanzkriterien:**
- [ ] [testbare Bedingung 1]
- [ ] [testbare Bedingung 2]

**Definition of Done:**
- [ ] Umgesetzt in `agents.yaml`/`tasks.yaml`/`crew.py`
- [ ] Risiko identifiziert und in der Risiken-Tabelle von `DESIGN.md` dokumentiert
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub-Handle | Hauptbeitrag |
| --- | --- | --- |
| ... | ... | ... |

Thema: [Thema eurer Crew]
```

## Peer Evaluation (vertraulich — nicht ins Repo committen)

Schickt das direkt an eure Lehrperson (per E-Mail, nicht über GitHub), bei jeder Abgabe-Deadline. Es aus dem gemeinsamen Repo herauszuhalten — wo Teammitglieder es sehen würden — ist genau das, was ehrliches Feedback erst möglich macht; das fließt in die individuelle Anpassung ein, die im [Überblick zur Aufgabe](assignment-overview.md#bewertung) beschrieben ist.

```markdown
# Peer Evaluation — [euer Name] — [Zwischenabgabe / Abschluss]

## Eure Teammitglieder
Ein Abschnitt pro Teammitglied, nicht für euch selbst:

### [Name des Teammitglieds]
- Beitrag (1–5, 5 = hat den vollen eigenen Anteil oder mehr geleistet):
- Was hat diese Person in dieser Phase konkret gemacht?
- Sonst noch etwas, das eure Lehrperson wissen sollte? (optional, vertraulich)

## Ihr selbst
- Was habt ihr in dieser Phase konkret beigetragen?
```
