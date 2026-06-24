# Sprint 3 — RAG

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/03-rag.md)

RAG (Retrieval-Augmented Generation) gibt einem Agenten Zugriff auf bestimmte Dokumente/Daten, mit denen er nicht trainiert wurde: der Inhalt wird in Chunks zerlegt, jeder Chunk in einen Vektor eingebettet, die Vektoren gespeichert, und die relevantesten Chunks für eine gegebene Anfrage abgerufen, um sie in den Kontext des LLM einzuspeisen. Der Teil, über den Leute stolpern: **Embeddings sind ein separates Modell vom Chat-LLM** — man kann Groq für den Chat und einen völlig anderen Anbieter für Embeddings nutzen, oder versehentlich auf einen Anbieter zurückfallen, den man nie konfiguriert hat.

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020, 9459–9474. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG-Architektur: ein Query-Encoder und Retriever (nicht-parametrisch) speisen die Top-k-Dokumente in einen Generator (parametrisch), der über sie marginalisiert, um die finale Antwort zu erzeugen](../assets/rag-lewis2020-fig1.png)
*Abbildung 1 aus Lewis et al. (2020): ein Query Encoder + Retriever speist Dokumente in einen Generator, der seine Vorhersage über sie marginalisiert. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

## In diesem Repo

[crew.py:48-60](../../src/research_crew/crew.py#L48-L60) konfiguriert bereits den Embedder, nutzt ihn aber noch nicht:

```python
embedder={
    "provider": "google-generativeai",
    "config": {
        "api_key": os.getenv("GEMINI_API_KEY"),
        "model_name": "gemini-embedding-001",
    },
},
```

Warum das existiert: CrewAIs Knowledge-/RAG-Funktionen nutzen standardmäßig **OpenAI-Embeddings**, unabhängig davon, welches LLM für den Chat konfiguriert ist. Ohne diesen Block scheitert das Hinzufügen jeder Knowledge-Quelle mit einem fehlenden `OPENAI_API_KEY`-Fehler.

**Fertiger Code zur Wiederverwendung:** [src/research_crew/knowledge_source_example.py](../../src/research_crew/knowledge_source_example.py) ist eine funktionierende, noch nicht eingebundene `build_knowledge_sources()`-Hilfsfunktion, die eine `TextFileKnowledgeSource` zurückgibt. Übernehmt sie direkt, oder schreibt die gleichen Zeilen selbst:

```python
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

preference_knowledge = TextFileKnowledgeSource(file_paths=["your_file.txt"])
```

## Aufgabe

Das ist der zentrale praktische Sprint der Reihe — echtes RAG für euren Anwendungsfall verkabeln:

1. **Sprint Planning**: Öffnet 1–2 GitHub-Issues als User Stories, gelabelt `epic:rag`.
2. Wählt ein echtes Dokument/eine echte Quelle, die zu eurem Anwendungsfall passt (Ideen in der Tabelle des READMEs), und legt sie unter `knowledge/` ab.
3. Importiert eine Knowledge-Source-Klasse, zeigt sie auf eure Datei, und übergebt `knowledge_sources=[...]` an den `Crew`-Konstruktor.
4. Fügt einen Task hinzu (oder ändert einen bestehenden), der etwas fragt, das nur aus dieser Quelle beantwortbar ist. Prüft, dass der Agent korrekt mit abgerufenem Wissen antwortet.
5. Entfernt jetzt die Knowledge-Quelle und stellt dieselbe Frage erneut — halluziniert der Agent, verweigert er, oder gibt er zu, es nicht zu wissen? Genau dieser Vergleich *ist* der Sinn von RAG, kein Nebeneffekt.
6. Aktualisiert die Tabelle Knowledge Sources/RAG in `DESIGN.md`.
7. Bevor ihr das als fertig betrachtet, beantwortet in `DESIGN.md`: Was fehlt oder ist veraltet in eurer Quelle, und was macht der Agent tatsächlich, wenn das Retrieval nichts Relevantes liefert? Embeddings haben eigene Rate-Limits, getrennt vom Chat-LLM — würde euer Entwurf noch funktionieren, wenn jemand aus eurem Kurs ein 100-Seiten-Dokument statt eurer wenigen Seiten hochladen würde? Konkret: Wie ist die *Ausgabe* mit RAG besser als ohne, für euren spezifischen Anwendungsfall — nicht "genauer" im Abstrakten, sondern ein konkretes Beispiel, auf das ihr zeigen könnt?

## Zusatzaufgabe

Fügt eine zweite Knowledge-Quelle eines anderen Typs hinzu und prüft, dass beide abrufbar sind.

---

**→ Die Zwischenabgabe ist am Ende dieses Sprints fällig.** Einzureichen: `agents.yaml`, `tasks.yaml`, `DESIGN.md` (Überblick, Architektur, Risiken, Grenzen — alle entsprechend Sprints 0–3), und euer Backlog (Issues + Project-Board) im aktuellen Stand. Siehe [Überblick zur Aufgabe](assignment-overview.md) für die genaue Bewertung.
