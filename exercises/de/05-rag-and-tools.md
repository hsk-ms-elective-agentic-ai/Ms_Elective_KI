# Schritt 5 — RAG + Tools

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/05-rag-and-tools.md)

Fügt der Crew aus Schritt 4 zwei Formen externer Verankerung hinzu. **Tools** (`SerperDevTool`) ermöglichen dem Agenten, zur Laufzeit aktuelle Informationen aus dem Web abzurufen. **RAG** (eine `TextFileKnowledgeSource`) ermöglicht der Crew, aus einem von euch bereitgestellten Dokument zur Abfragezeit zu retrieven. Beide adressieren dieselbe grundlegende Einschränkung in Schritten 1–4: Das Wissen des LLMs ist zum Trainingszeitpunkt eingefroren und kennt eure spezifischen Dokumente nicht.

## Hintergrund

### Tools

Die Demonstration, dass ein Sprachmodell lernen kann, *wann* es ein Tool aufrufen soll, *welches* Tool, und *mit welchen Argumenten* — anstatt dass ein Mensch jeden Aufruf fest codiert — war:

> Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

![Toolformer: das Modell fügt API-Aufrufe in seinen eigenen generierten Text ein](../assets/toolformer-schick2023-fig1.png)
*Abbildung 1 aus Schick et al. (2023): Toolformer fügt eigenständig Tool-Aufrufe ein. Reproduziert für Bildungszwecke in diesem Kurs.*

### RAG

Retrieval-Augmented Generation: ein Dokument in Abschnitte aufteilen, jeden Abschnitt in einen Vektor einbetten, die Vektoren speichern und die ähnlichsten Abschnitte für eine Abfrage abrufen, um sie in den LLM-Kontext einzuspeisen. Das Originalpaper:

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020, 9459–9474. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG-Architektur: Query Encoder + Retriever speisen Top-k-Dokumente in einen Generator](../assets/rag-lewis2020-fig1.png)
*Abbildung 1 aus Lewis et al. (2020): RAG-Architektur. Reproduziert für Bildungszwecke in diesem Kurs.*

**Eine praktische Falle**: Embeddings nutzen ein separates Modell vom Chat-LLM. Diese Crew verwendet Groq für Chat (kostenlos) und Gemini für Embeddings (ebenfalls kostenlos) — zwei verschiedene API-Keys, zwei verschiedene Rate-Limits. Deshalb gibt es `GEMINI_API_KEY` in `.env.example`.

## Der Code

Öffnet [src/exercises/step_05_rag_and_tools.py](../../src/exercises/step_05_rag_and_tools.py). Ergänzungen gegenüber Schritt 4:

| Hinzugefügt | Was es bewirkt |
| --- | --- |
| `SerperDevTool()` | Live-Websuche — der Agent entscheidet, wann er sie aufruft |
| `tools=[web_search]` am Researcher | Registriert das Tool beim Agenten |
| `TextFileKnowledgeSource(...)` | Bettet `knowledge/user_preference.txt` in einen Vektorspeicher ein |
| `knowledge_sources=[...]` an Crew | Stellt die Knowledge-Sources allen Agenten zur Abfragezeit zur Verfügung |
| `embedder={...}` an Crew | Leitet Embedding-Aufrufe an Gemini statt an das Standard-OpenAI weiter |

## Aufgabe

1. Setzt `TOPIC` auf dasselbe Thema wie in den vorherigen Schritten.

2. Führt es aus:
   ```bash
   uv run python src/exercises/step_05_rag_and_tools.py
   ```

3. Vergleicht die Ausgabe mit Schritt 4:
   - Enthält die Ausgabe des Researchers Informationen, die erkennbar aktueller oder spezifischer sind als in Schritt 4?
   - Taucht das Wissen aus `user_preference.txt` irgendwo in der Ausgabe auf?
   - Prüft das verbose-Log: Könnt ihr den Moment sehen, in dem der Agent das Such-Tool aufruft, und welche Abfrage er dabei verwendet?

4. **Fügt eure eigene Knowledge-Source hinzu**: Erstellt ein relevantes Dokument in `knowledge/` (eine `.txt`-Zusammenfassung von etwas zu eurem Thema) und fügt es als zweite `TextFileKnowledgeSource` hinzu. Stellt im Task-Description eine Frage, die nur aus diesem Dokument beantwortet werden kann. Bestätigt, dass das Retrieval funktioniert hat — führt ohne das Dokument aus und prüft, ob der Agent die Frage trotzdem beantwortet oder jetzt eingesteht, es nicht zu wissen.

5. Füllt den **Schritt 5**-Abschnitt in `EVALUATION.md` aus und eure abschließende Empfehlung.

## Zusatzaufgabe

Fügt eine PDF-Datei statt einer Textdatei hinzu: `from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource`. Nutzt ein echtes, themenbezogenes Dokument (ein Policy-Paper, eine Forschungszusammenfassung, ein Produktbriefing). Testet dann das Retrieval, indem ihr eine Frage stellt, deren Antwort auf einer bestimmten Seite der PDF steht — retrievet der Agent sie?

---

**Das ist eure Abschlussabgabe.** Siehe [Überblick zur Aufgabe](assignment-overview.md) für das vollständige Bewertungsschema und genaue Abgabeanforderungen.
