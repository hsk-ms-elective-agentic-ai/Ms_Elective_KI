# Markdown-Kurzanleitung

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/markdown-guide.md)

`REPORT.md` und `TEAM.md` sind reine Textdateien, geschrieben in **Markdown** — eine leichtgewichtige Methode, um Formatierung (Überschriften, Fett, Listen, Tabellen, Links) mit einfachen Zeichen hinzuzufügen, ohne Menüs oder Werkzeugleisten. GitHub rendert das automatisch überall, wo die Datei angezeigt wird — was ihr schreibt, ist also das, was euer Team und eure Lehrperson sehen.

Diese Seite deckt alles ab, was ihr für `REPORT.md` tatsächlich braucht. Für die vollständige Spezifikation siehe [GitHubs eigenen Markdown-Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) — mehr als diese Seite solltet ihr aber kaum brauchen.

## Überschriften

```markdown
# Größte Überschrift (einmalig, für den Titel)
## Abschnittsüberschrift
### Unterabschnittsüberschrift
```

`REPORT.md` hat alle Überschriften bereits vorgegeben — ihr füllt den Text darunter aus, fügt normalerweise keine neuen hinzu.

## Fett, kursiv, Inline-Code

```markdown
**fetter Text**
*kursiver Text*
`Inline-Code`, wie ein Variablenname: `crew.kickoff()`
```

## Listen

```markdown
- Aufzählungspunkt eins
- Aufzählungspunkt zwei
  - Eingerückter Unterpunkt (zwei Leerzeichen)

1. Erster Schritt
1. Zweiter Schritt (Markdown nummeriert automatisch — ihr müsst nicht 2., 3., ... schreiben)
```

## Links

```markdown
[Linktext](https://example.com)
[eine Datei in diesem Repo](src/research_crew/crew.py)
```

## Tabellen

Wird durchgehend in `REPORT.md` verwendet, am wichtigsten die **Sprint-Progression**-Tabelle:

```markdown
| Sprint | Ergänzt | Was sich geändert hat |
| --- | --- | --- |
| 0 | Setup | Erster LLM-Aufruf |
| 1 | Prompting | Zero-Shot-Basisprompt |
```

Ergibt gerendert:

| Sprint | Ergänzt | Was sich geändert hat |
| --- | --- | --- |
| 0 | Setup | Erster LLM-Aufruf |
| 1 | Prompting | Zero-Shot-Basisprompt |

Tipp: Ihr müsst die `|`-Spalten nicht manuell ausrichten — GitHub rendert es so oder so korrekt, und die meisten Editoren (siehe unten) formatieren die Abstände automatisch.

## Code-Blöcke

Für mehr als eine Zeile Code, oder um einen ganzen Ausschnitt zu zeigen:

````markdown
```python
agent = Agent(role="Researcher", goal="...", backstory="...")
```
````

Der Sprachname nach den ersten drei ` ``` ` (`python`, `bash`, `yaml`, ...) aktiviert Syntax-Highlighting — optional, macht Code aber leichter lesbar.

## Blockquotes

In `REPORT.md` für Hinweise und Anleitungen verwendet (der kursive `_(...)_`-Hinweistext und die `>`-Kästen):

```markdown
> Ein Hinweis oder Kasten, wie die bereits in REPORT.md, die erklären, was in jedem Abschnitt geschrieben werden soll.
```

## Horizontale Linie

`REPORT.md` nutzt `---` auf einer eigenen Zeile, um Hauptabschnitte zu trennen — bereits vorhanden, das müsst ihr nicht selbst ergänzen.

## Vorschau eurer Änderungen

- **In VS Code:** öffnet die `.md`-Datei, klickt dann auf das Vorschau-Icon oben rechts im Editor (oder `Strg+Shift+V` / `Cmd+Shift+V`), um es beim Tippen live gerendert nebeneinander zu sehen.
- **Auf github.com:** öffnet die Datei und klickt auf den **"Preview"**-Tab, bevor ihr committet, falls ihr direkt im Browser bearbeitet.

Falls ihr euch mit der Syntax gar nicht erst beschäftigen wollt: Die VS-Code-Extension **"Markdown All in One"** ergänzt Tastenkürzel (`Strg+B` für Fett, etc.) und Auto-Formatierung zu allem oben. Für eine vollständig WYSIWYG-Erfahrung — Formatierung wird live beim Tippen gerendert, kein sichtbares `#`/`**`/`|` — probiert [Obsidian](https://obsidian.md) (kostenlos) oder [Typora](https://typora.io) (kostenpflichtig); beide bearbeiten dieselbe `.md`-Datei in eurem geklonten Repo, Committen und Pushen läuft also weiterhin wie gewohnt über VS Code.
