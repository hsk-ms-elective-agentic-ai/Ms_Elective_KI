# Ethik- & Trustworthy-AI-Report — [euer Name] ([GitHub-Benutzername])

**Kurs:** Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI
**Team:** [euer Teamname] — **Thema:** [euer Thema]

Das ist eure **individuelle** Abgabe — 20% eurer Note — über OpenOlat, separat von eurem Team-Repo eingereicht (siehe [Überblick zur Aufgabe](assignment-overview.md#abgabepaket) für wo und wie). Auch wenn ihr und eure Teammitglieder über denselben Agenten schreiben, ist das kein gemeinsames Dokument: schreibt eure eigene Analyse, in euren eigenen Worten, verankert im tatsächlichen `REPORT.md` eures Teams (Architektur, Implementierung, Evaluierung) und in dem, was ihr persönlich beim Bauen und Testen beobachtet habt. Zwei Studierende desselben Teams sollten sich nicht gleich lesen.

Die Linse für diesen Report ist **vertrauenswürdige KI (Trustworthy AI)**: zählt nicht einfach auf, was bei Agenten im Allgemeinen theoretisch schiefgehen könnte — beurteilt, wie vertrauenswürdig *euer konkreter Agent* tatsächlich ist, und schlagt konkrete Änderungen vor, die ihn vertrauenswürdiger machen würden.

> Europäische Kommission, High-Level Expert Group on AI (2019). *Ethics Guidelines for Trustworthy AI*. https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai — der Rahmen hinter den Dimensionen unten.

Generische Antworten ("unser Agent könnte Bias haben, also sollten wir vorsichtig sein") erzielen wenig Punkte. Konkrete, verankerte Antworten erzielen viele — verknüpft jede Aussage mit etwas Konkretem an *diesem* Agenten: einer `role`/`goal`/`backstory`, die ihr zitieren könnt, einem Tool, das er tatsächlich aufruft, einer Memory-/Knowledge-Source, die er tatsächlich speichert oder abruft, einem echten Testlauf, bei dem etwas gut oder schlecht gelaufen ist. Jede Dimension unten fragt nach zwei Dingen, nicht nach einem: einer verankerten Einschätzung, wo euer Agent tatsächlich steht, **und** einer konkreten vorgeschlagenen Änderung, die ihn vertrauenswürdiger machen würde — nicht nur ein Risiko benennen, sondern genau sagen, was ihr anders bauen würdet.

---

## 1. Euer Agent, kurz

_(2–4 Sätze, in euren eigenen Worten: was macht der Agent eures Teams, und womit hat er tatsächlich Kontakt — Tools, Memory, Knowledge-Sources, externe Systeme? Das ist die Grundlage für alles Weitere; gebt nicht einfach die Executive Summary aus `REPORT.md` wieder.)_

---

## 2. Bias & Fairness

Hat euer Agent das Potenzial, Bias zu zeigen? Wie könnte er unterschiedliche Nutzer:innen oder Gruppen unterschiedlich behandeln? Welche Schritte habt ihr unternommen (oder solltet ihr unternehmen), um Bias zu mindern?

- _(z. B.: "Unser Agent nutzt ein Sprachmodell, das möglicherweise auf verzerrten Daten trainiert wurde. Ich habe ihn mit Anfragen aus drei verschiedenen Nutzer-Personas getestet und auf diskriminierende Ausgaben geachtet. Wir haben explizite Anweisungen in die `backstory` der Agenten aufgenommen, alle Nutzer:innen fair zu behandeln.")_
- **Vorgeschlagene Änderung:** _(Eine konkrete, spezifische Änderung am Design eures Agenten, die dieses Risiko verringern würde — nicht "vorsichtiger sein", sondern etwas, das ihr tatsächlich umsetzen könntet: eine Ergänzung der `backstory`, ein Testfall für euer Evaluations-Set, ein Guardrail. So konkret, dass ein Teammitglied es allein aus eurem Satz umsetzen könnte.)_

## 3. Privacy & Data Security

Welche Daten sammelt, speichert oder verarbeitet euer Agent? Wie wird mit Nutzerdaten umgegangen? Welche Datenschutzbedenken ergeben sich aus Memory- oder Tool-Nutzung eures Agenten?

- _(z. B.: "CrewAIs `memory=True` speichert Interaktionsdaten lokal unter `CREWAI_STORAGE_DIR`. Ich habe geprüft, was dort geschrieben wird, und sichergestellt, dass keine sensiblen Informationen enthalten sind. Nutzer:innen können es über `crew.reset_memories('all')` löschen.")_
- **Vorgeschlagene Änderung:** _(Eine konkrete Änderung — z. B. eingrenzen, was ins Memory geschrieben wird, eine Aufbewahrungsfrist einführen, den Zugriff eines Tools auf bestimmte Felder beschränken.)_

## 4. Transparency & Explainability

Können Nutzer:innen nachvollziehen, wie euer Agent Entscheidungen trifft? Ist der Denkprozess des Agenten transparent? Was passiert, wenn der Agent einen Fehler macht?

- _(z. B.: "Der Lauf mit `verbose=True` legt die vollständige ReAct-Reasoning-Spur des Agenten offen, die wir zum Debuggen genutzt haben. Endnutzer:innen unserer finalen Ausgabe sehen jedoch nur den finalen Bericht, nicht diese Spur — das halte ich für eine Lücke, die es wert ist, benannt zu werden, weil...")_
- **Vorgeschlagene Änderung:** _(Eine konkrete Änderung — z. B. eine Zusammenfassung der Reasoning-Spur für Endnutzer:innen sichtbar machen, einen Konfidenz-Hinweis ergänzen, protokollieren, aus welcher Knowledge-Source eine Aussage stammt.)_

## 5. Autonomy & Control

Welches Autonomieniveau hat euer Agent, und welche Sicherheitsmechanismen sind vorhanden? Kann der Agent Handlungen mit realen Konsequenzen ausführen? Wie können Nutzer:innen den Agenten übersteuern oder stoppen?

- _(z. B.: "Unser Agent kann Daten nur über Tools/`knowledge_sources` lesen — er hat kein Tool, das ein externes System schreibt oder verändert, daher ist der Schaden im Fehlerfall auf eine schlechte Antwort begrenzt, nicht auf eine schlechte Handlung.")_
- **Vorgeschlagene Änderung:** _(Eine konkrete Änderung — z. B. `Task(human_input=True)` vor einem folgenreichen Schritt ergänzen, eine harte Grenze über `max_iter`, eine explizite "erst fragen, dann handeln"-Anweisung in der `backstory`.)_

## 6. Misuse & Safety

Wie könnte euer Agent missbraucht werden? Welche schädlichen Verhaltensweisen könnte er ermöglichen? Welche Sicherheitsmaßnahmen habt ihr implementiert?

- _(z. B.: "Ein Agent mit Websuche könnte missbraucht werden, um Informationen für schädliche Zwecke zu sammeln. Wir haben `goal`/`backstory` des Researchers eng auf unser Thema begrenzt und ihm keinen uneingeschränkten Suchzugriff gegeben.")_
- **Vorgeschlagene Änderung:** _(Eine konkrete Änderung — z. B. den Umfang eines Tools weiter eingrenzen, ein Output-Guardrail ergänzen, das bestimmte Anfragearten ablehnt, eine sensible Aktion rate-limiten.)_

## 7. Accountability

Wer ist verantwortlich, wenn der Agent einen Fehler macht oder Schaden verursacht? Wie geht ihr mit Fehlern und Edge Cases um?

- _(z. B.: "Wir haben `expected_output` unserer Agenten so gestaltet, dass ein expliziter 'Ich weiß es nicht'-Pfad möglich ist, statt zu raten, und wir loggen die `tracing=True`-Trace-URL jedes `kickoff()`-Laufs zur nachträglichen Überprüfung.")_
- **Vorgeschlagene Änderung:** _(Eine konkrete Änderung — z. B. ein expliziter Eskalationspfad bei Unsicherheit des Agenten, eine verpflichtende menschliche Freigabe vor Auslieferung der Ausgabe, besseres Logging, welcher Agent/Task eine bestimmte Aussage erzeugt hat.)_

---

## 8. Trustworthiness-Fazit & priorisierte Änderungen

_(1–2 Absätze, wirklich eure eigenen: wie vertrauenswürdig ist dieser Agent insgesamt, so wie er heute dasteht — nicht Agenten im Allgemeinen, *dieser* konkrete? Welche der sechs vorgeschlagenen Änderungen oben würde den größten Unterschied machen, und warum genau diese zuerst? Würdet ihr diesen Agenten so einsetzen, wie er ist? Falls nicht: was ist die minimale Menge an Änderungen, die vorher passieren müsste?)_
