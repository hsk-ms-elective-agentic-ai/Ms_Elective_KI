# Ethik-Report — [euer Name] ([GitHub-Benutzername])

**Kurs:** Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI
**Team:** [euer Teamname] — **Thema:** [euer Thema]

Das ist eure **individuelle** Abgabe — 20% eurer Note — über OpenOlat, separat von eurem Team-Repo eingereicht (siehe [Überblick zur Aufgabe](assignment-overview.md#abgabepaket) für wo und wie). Auch wenn ihr und eure Teammitglieder über denselben Agenten schreiben, ist das kein gemeinsames Dokument: schreibt eure eigene Analyse, in euren eigenen Worten, verankert im tatsächlichen `REPORT.md` eures Teams (Architektur, Implementierung, Evaluierung) und in dem, was ihr persönlich beim Bauen und Testen beobachtet habt. Zwei Studierende desselben Teams sollten sich nicht gleich lesen.

Generische Antworten ("unser Agent könnte Bias haben, also sollten wir vorsichtig sein") erzielen wenig Punkte. Konkrete, verankerte Antworten erzielen viele — verknüpft jede Aussage mit etwas Konkretem an *diesem* Agenten: einer `role`/`goal`/`backstory`, die ihr zitieren könnt, einem Tool, das er tatsächlich aufruft, einer Memory-/Knowledge-Source, die er tatsächlich speichert oder abruft, einem echten Testlauf, bei dem etwas gut oder schlecht gelaufen ist.

---

## 1. Euer Agent, kurz

_(2–4 Sätze, in euren eigenen Worten: was macht der Agent eures Teams, und womit hat er tatsächlich Kontakt — Tools, Memory, Knowledge-Sources, externe Systeme? Das ist die Grundlage für alles Weitere; gebt nicht einfach die Executive Summary aus `REPORT.md` wieder.)_

---

## 2. Bias & Fairness

Hat euer Agent das Potenzial, Bias zu zeigen? Wie könnte er unterschiedliche Nutzer:innen oder Gruppen unterschiedlich behandeln? Welche Schritte habt ihr unternommen (oder solltet ihr unternehmen), um Bias zu mindern?

- _(z. B.: "Unser Agent nutzt ein Sprachmodell, das möglicherweise auf verzerrten Daten trainiert wurde. Ich habe ihn mit Anfragen aus drei verschiedenen Nutzer-Personas getestet und auf diskriminierende Ausgaben geachtet. Wir haben explizite Anweisungen in die `backstory` der Agenten aufgenommen, alle Nutzer:innen fair zu behandeln.")_

## 3. Privacy & Data Security

Welche Daten sammelt, speichert oder verarbeitet euer Agent? Wie wird mit Nutzerdaten umgegangen? Welche Datenschutzbedenken ergeben sich aus Memory- oder Tool-Nutzung eures Agenten?

- _(z. B.: "CrewAIs `memory=True` speichert Interaktionsdaten lokal unter `CREWAI_STORAGE_DIR`. Ich habe geprüft, was dort geschrieben wird, und sichergestellt, dass keine sensiblen Informationen enthalten sind. Nutzer:innen können es über `crew.reset_memories('all')` löschen.")_

## 4. Transparency & Explainability

Können Nutzer:innen nachvollziehen, wie euer Agent Entscheidungen trifft? Ist der Denkprozess des Agenten transparent? Was passiert, wenn der Agent einen Fehler macht?

- _(z. B.: "Der Lauf mit `verbose=True` legt die vollständige ReAct-Reasoning-Spur des Agenten offen, die wir zum Debuggen genutzt haben. Endnutzer:innen unserer finalen Ausgabe sehen jedoch nur den finalen Bericht, nicht diese Spur — das halte ich für eine Lücke, die es wert ist, benannt zu werden, weil...")_

## 5. Autonomy & Control

Welches Autonomieniveau hat euer Agent, und welche Sicherheitsmechanismen sind vorhanden? Kann der Agent Handlungen mit realen Konsequenzen ausführen? Wie können Nutzer:innen den Agenten übersteuern oder stoppen?

- _(z. B.: "Unser Agent kann Daten nur über Tools/`knowledge_sources` lesen — er hat kein Tool, das ein externes System schreibt oder verändert, daher ist der Schaden im Fehlerfall auf eine schlechte Antwort begrenzt, nicht auf eine schlechte Handlung.")_

## 6. Misuse & Safety

Wie könnte euer Agent missbraucht werden? Welche schädlichen Verhaltensweisen könnte er ermöglichen? Welche Sicherheitsmaßnahmen habt ihr implementiert?

- _(z. B.: "Ein Agent mit Websuche könnte missbraucht werden, um Informationen für schädliche Zwecke zu sammeln. Wir haben `goal`/`backstory` des Researchers eng auf unser Thema begrenzt und ihm keinen uneingeschränkten Suchzugriff gegeben.")_

## 7. Accountability

Wer ist verantwortlich, wenn der Agent einen Fehler macht oder Schaden verursacht? Wie geht ihr mit Fehlern und Edge Cases um?

- _(z. B.: "Wir haben `expected_output` unserer Agenten so gestaltet, dass ein expliziter 'Ich weiß es nicht'-Pfad möglich ist, statt zu raten, und wir loggen die `tracing=True`-Trace-URL jedes `kickoff()`-Laufs zur nachträglichen Überprüfung.")_

---

## 8. Eure persönliche Einschätzung

_(1–2 Absätze, wirklich eure eigenen: welche der fünf Dimensionen oben beunruhigt euch am meisten für *genau diesen Agenten* — nicht für Agenten im Allgemeinen — und warum? Würdet ihr diesen Agenten so einsetzen, wie er ist? Was müsste sich zuerst ändern?)_
