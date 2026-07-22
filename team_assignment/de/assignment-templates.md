# Vorlagen für die Aufgabe

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-templates.md)

**`EVALUATION.md` und `TEAM.md` existieren bereits im Root eures Repos** — jede Team-Kopie startet damit schon als Vorlage. Füllt sie direkt aus; sie sind unten zur Referenz abgedruckt. Siehe [Überblick zur Aufgabe](assignment-overview.md) für die Verwendung, und die jeweilige Schrittseite für das, was bei jedem Schritt geschrieben werden soll.

## `EVALUATION.md`

Das ist das Hauptabgabeprodukt: eine vergleichende Analyse dessen, was jeder Schritt hinzugefügt hat, spezifisch für euer Thema verankert. Füllt den Abschnitt jedes Schritts aus, sobald ihr ihn durchführt — schreibt Beobachtungen direkt nach dem Ausführen, nicht am Ende. Der Vergleich *ist* die Aufgabe; generische Antworten ("es ist genauer") erzielen weniger Punkte als spezifische ("der Analyst in Schritt 13 hat X als übertrieben markiert, was der Researcher in Schritt 09 nicht hinterfragt hatte").

```markdown
# Schritt-Evaluierung

**Team:** [Teamname] · **Thema:** [euer Thema] · **Zuletzt aktualisiert:** [Schritt N, JJJJ-MM-TT]

## Euer Thema

[Ein oder zwei Sätze: Welches spezifische Problem adressiert euer Thema, und wer würde die Ausgabe nutzen?
"KI im Gesundheitswesen" ist zu breit. "Wie KI für die Früherkennung von Krebs in der Radiologie eingesetzt 
wird, gerichtet an Radiologen, die diagnostische Unterstützungstools evaluieren" ist der richtige Detailgrad.]

## Schrittweise Beobachtungen

Führt jeden Schritt mit demselben Thema aus. Füllt direkt nach dem Ausführen aus.

### Schritt 03 — Zero-Shot-Prompting
**Ausführungsdatum:**
**Wie die Ausgabe aussieht (2–3 Sätze):**
**Eine Sache, die euch überrascht hat:**

### Schritt 04 — Few-Shot-Prompting
**Ausführungsdatum:**
**Was sich gegenüber Schritt 03 verändert hat; haben die Beispiele die Ausgabe merklich gelenkt:**
**Eine Sache, die euch überrascht hat:**

### Schritt 05 — Prompt-Vorlage
**Ausführungsdatum:**
**Was sich gegenüber Schritt 04 verändert hat:**
**Eine Sache, die euch überrascht hat:**

### Schritt 06 — Chain Prompting
**Ausführungsdatum:**
**Was sich gegenüber Schritt 04/05 verändert hat:**
**Eine Sache, die euch überrascht hat:**

### Schritt 07 — Chain of Thought
**Ausführungsdatum:**
**Was sich gegenüber Schritt 05 verändert hat; hat explizites Schlussfolgern das Ergebnis verändert oder nur mehr Text erzeugt:**
**Eine Sache, die euch überrascht hat:**

### Schritt 08 — Tree of Thought
**Ausführungsdatum:**
**Was sich gegenüber Schritt 07 verändert hat; hat das parallele Erkunden mehrerer Gedankenpfade die Antwort verändert, oder nur die Diskussion drumherum:**
**Welche Prompting-Technik (Schritte 04–08) hat für euer Thema am besten funktioniert, und warum:**
**Eine Sache, die euch überrascht hat:**

### Schritt 09 — Einzelner Agent
**Ausführungsdatum:**
**Was sich gegenüber Schritt 08 verändert hat (konkret):**
**Was besser ist:**
**Was schwieriger oder fragiler ist:**
**Eine Sache, die euch überrascht hat:**

### Schritt 10 — Tools
**Ausführungsdatum:**
**Was sich gegenüber Schritt 09 verändert hat (konkret):**
**Was besser ist:**
**Was schwieriger oder fragiler ist:**
**Eine Sache, die euch überrascht hat:**

### Schritt 11 — MCP
**Ausführungsdatum:**
**Was sich gegenüber Schritt 10 verändert hat (konkret):**
**Was besser ist:**
**Was schwieriger oder fragiler ist:**
**Eine Sache, die euch überrascht hat:**

### Schritt 12 — RAG
**Ausführungsdatum:**
**Was sich gegenüber Schritt 10/11 verändert hat (konkret):**
**Was besser ist:**
**Was schwieriger oder fragiler ist:**
**Eine Sache, die euch überrascht hat:**

### Schritt 13 — Multi-Agent
**Ausführungsdatum:**
**Was sich gegenüber Schritt 09 verändert hat (konkret):**
**Was besser ist:**
**Was schwieriger oder fragiler ist:**
**Eine Sache, die euch überrascht hat:**

## Eure Empfehlung

Für euer spezifisches Thema und euren Anwendungsfall: Welchen Komplexitätsgrad würdet ihr 
tatsächlich einsetzen, und warum? Was würdet ihr verlieren, wenn ihr einen Schritt einfacher 
geht? Was würdet ihr gewinnen, wenn ihr einen Schritt komplexer geht — und ist dieser Gewinn 
die zusätzliche Fragilität wert?

[150–250 Wörter. Spezifisch auf euer Thema bezogen, nicht generisch.]

## Alternativen, die ihr ausprobiert habt

Was habt ihr sonst noch ausprobiert oder in Betracht gezogen? (Eine andere Themenformulierung, 
eine andere Rollendefinition in der Agent-Backstory, ein anderes Knowledge-Dokument, ein Tool, 
das nicht wie erwartet funktioniert hat?) Was habt ihr festgestellt?

## Was ihr als Nächstes hinzufügen würdet

Wenn ihr zwei weitere Wochen und einen weiteren API-Key hätten: Was genau würdet ihr ändern, 
hinzufügen oder testen? Warum das und nicht etwas anderes?
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub-Handle | Hauptbeitrag |
| --- | --- | --- |
| | | |

Thema: [euer Thema]
```

## Peer Evaluation (privat — nicht ins Repo committen)

Reicht das direkt an eure Lehrperson ein (per E-Mail, nicht über GitHub) bei jeder Abgabe-Deadline. Es aus dem gemeinsamen Repo herauszuhalten ist das, was ehrliches Feedback ermöglicht; das fließt in die individuelle Anpassung ein, die im [Überblick zur Aufgabe](assignment-overview.md#bewertung) beschrieben ist.

```markdown
# Peer Evaluation — [euer Name] — [Zwischen- / Abschlussabgabe]

## Eure Teammitglieder
Ein Abschnitt pro Teammitglied, nicht euch selbst:

### [Name des Teammitglieds]
- Beitrag (1–5, 5 = hat vollen Anteil oder mehr übernommen):
- Was hat die Person in dieser Phase konkret getan?
- Sonst noch etwas, das eure Lehrperson wissen sollte? (optional, vertraulich)

## Ihr selbst
- Was habt ihr in dieser Phase konkret beigetragen?
```
