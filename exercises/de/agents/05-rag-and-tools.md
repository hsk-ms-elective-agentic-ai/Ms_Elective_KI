# Schritt 5 — RAG + Tools

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../../en/agents/05-rag-and-tools.md)

Fügt der Crew aus Schritt 4 zwei Formen externer Verankerung hinzu. **Tools** ermöglichen einem Agenten, zur Laufzeit aktuelle Informationen abzurufen; der Agent entscheidet selbst, wann und mit welcher Abfrage er das Tool aufruft. **RAG** ermöglicht der Crew, aus einem von euch bereitgestellten Dokument zu retrieven; Abschnitte werden eingebettet und die relevantesten automatisch in den Kontext injiziert. Beide adressieren dieselbe Grundeinschränkung aus Schritten 1–4: das Wissen des LLMs ist zum Trainingszeitpunkt eingefroren.

## Hintergrund

### Tools

> Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

![Toolformer fügt eigenständig API-Aufrufe in den eigenen Text ein](../../assets/toolformer-schick2023-fig1.png)
*Abbildung 1 aus Schick et al. (2023). Reproduziert für Bildungszwecke in diesem Kurs.*

### RAG

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG: Query Encoder + Retriever speisen Top-k-Dokumente in einen Generator](../../assets/rag-lewis2020-fig1.png)
*Abbildung 1 aus Lewis et al. (2020). Reproduziert für Bildungszwecke in diesem Kurs.*

**Ein praktischer Hinweis**: Embeddings nutzen ein separates Modell vom Chat-LLM. Diese Crew verwendet Groq für Chat und Gemini für Embeddings — zwei verschiedene Dienste, zwei verschiedene API-Keys, zwei verschiedene Rate-Limits. Der `embedder`-Block in `crew.py` ist bereits konfiguriert; ihr braucht nur `GEMINI_API_KEY` gesetzt.

## In diesem Repo

| Datei | Was ihr ändert |
| --- | --- |
| [src/research_crew/crew.py](../../../src/research_crew/crew.py) | `tools=[SerperDevTool()]` zum relevanten Agenten hinzufügen; `knowledge_sources=[...]` zur `Crew` |
| [src/research_crew/knowledge_source_example.py](../../../src/research_crew/knowledge_source_example.py) | Vorlage für `build_knowledge_sources()` — importieren und in `crew.py` aufrufen |
| `knowledge/` | Euer eigenes Dokument hier ablegen (`.txt` oder `.pdf`) |

Der `embedder`-Block ist bereits in `crew.py` — er ist das, was RAG ohne OpenAI-Key funktionieren lässt.

## Aufgabe

1. Legt ein Wissensdokument in `knowledge/` ab, das für euer Thema relevant ist — eine `.txt`-Datei mit Hintergrundinformationen reicht für den Anfang.

2. Importiert in `crew.py` `build_knowledge_sources` aus `knowledge_source_example.py` (oder schreibt die Source direkt), zeigt sie auf eure Datei und übergebt sie an den `Crew`-Konstruktor:
   ```python
   knowledge_sources=build_knowledge_sources()
   ```

3. Fügt `SerperDevTool()` dem Agenten hinzu, der nach Informationen sucht, in `crew.py`:
   ```python
   tools=[SerperDevTool()]
   ```

4. Aktualisiert die Task-Beschreibung dieses Agenten in `tasks.yaml` so, dass sie eine Frage enthält, die nur aus eurem Wissensdokument beantwortet werden kann. Führt es aus — entweder öffnet [step_05_rag_and_tools.ipynb](../../en/agents/step_05_rag_and_tools.ipynb) (auf Englisch) und führt die Zelle aus, oder im Terminal:
   ```bash
   uv run research_crew
   ```

5. Führt erneut aus **ohne** die Knowledge-Source (kommentiert sie aus). Beantwortet der Agent die dokumentspezifische Frage trotzdem richtig, oder gibt er zu, es nicht zu wissen? Dieser Vergleich ist der Sinn von RAG.

6. Prüft das verbose-Log: Könnt ihr sehen, wann der Agent das Such-Tool aufruft und welche Abfrage er dabei verwendet?

7. Füllt den **Schritt 5**-Abschnitt in `EVALUATION.md` aus und eure abschließende Empfehlung.

## Zusatzaufgabe

Fügt eine PDF-Datei statt einer Textdatei hinzu:
```python
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
PDFKnowledgeSource(file_paths=["your_document.pdf"])
```
Stellt eine Frage, deren Antwort auf einer bestimmten Seite steht. Retrievet der Agent sie?

---

**Das ist eure Abschlussabgabe.** Siehe [Überblick zur Aufgabe](../assignment-overview.md) für das vollständige Bewertungsschema.
