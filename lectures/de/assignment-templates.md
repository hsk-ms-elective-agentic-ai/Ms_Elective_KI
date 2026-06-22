# Vorlagen für die Aufgabe

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-templates.md)

Kopiert diese in euer Team-Repo und füllt sie aus. Siehe [Überblick zur Aufgabe](assignment-overview.md) dafür, wie sie genutzt werden, und [Meilensteine der Aufgabe](assignment-milestones.md) dafür, was in welcher Phase hineingehört.

## `RISK_LOG.md`

Fügt pro Meilenstein einen neuen Abschnitt an — bearbeitet nie einen vorherigen, auch wenn ihr ihn heute anders beantworten würdet. Die Geschichte eures Denkens ist der Punkt.

```markdown
# Risk Log

## M0 — Baseline (JJJJ-MM-TT)
**Entscheidung:** [was ihr gewählt habt und warum, ein bis zwei Sätze]
**Risiko:** [was schiefgehen könnte]
**Mitigation / akzeptierter Kompromiss:** [was ihr dagegen tun würdet, oder warum ihr es so akzeptiert]

## M1 — Tools (JJJJ-MM-TT)
...
```

## User Story (pro Epic, als GitHub Issue)

```markdown
**Story:** Als [Stakeholder des Crew-Ergebnisses] möchte ich [Fähigkeit], damit [Nutzen].

**Akzeptanzkriterien:**
- [ ] [testbare Bedingung 1]
- [ ] [testbare Bedingung 2]

**Definition of Done:**
- [ ] Umgesetzt in `agents.yaml`/`tasks.yaml`/`crew.py`
- [ ] Risiko identifiziert und in `RISK_LOG.md` dokumentiert
```

## `RETROSPECTIVE.md` (nur Abschlussabgabe)

```markdown
# Retrospektive

## Was hat sich seit der Zwischenabgabe verändert?
[Konkrete Entwurfsentscheidungen, die ihr revidiert oder umgeworfen habt]

## Warum?
[Was ihr gelernt habt — ein Vorlesungskonzept, ein gescheiterter Test, der Einwand eines Teammitglieds — das die Änderung ausgelöst hat]

## Was würdet ihr mit vier weiteren Wochen anders machen?
[Ehrliche Antwort, keine Wunschliste]
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub-Handle | Hauptbeitrag |
| --- | --- | --- |
| ... | ... | ... |

Thema: [Thema eurer Crew]
```
