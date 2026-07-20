# Step 5 — RAG + Tools

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../../de/agents/05-rag-and-tools.md)

Add two forms of external grounding to your step 4 crew. **Tools** let an agent retrieve live information at runtime; the agent decides when and with what query to call the tool. **RAG** lets the crew retrieve from a document you provide; chunks are embedded and the most relevant ones are injected into context automatically. Both address the same root limitation in steps 1–4: the LLM's knowledge is frozen at training time.

## Background

### Tools

> Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

![Toolformer inserting API calls into its own generated text](../../assets/toolformer-schick2023-fig1.png)
*Figure 1 from Schick et al. (2023). Reproduced for educational use in this course.*

### RAG

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG: query encoder and retriever feed top-k documents into a generator](../../assets/rag-lewis2020-fig1.png)
*Figure 1 from Lewis et al. (2020). Reproduced for educational use in this course.*

**One practical detail**: embeddings use a separate model from the chat LLM. This crew uses Groq for chat and Gemini for embeddings — two different services, two different API keys, two different rate limits. The `embedder` block in `crew.py` is already configured; you just need `GEMINI_API_KEY` set.

## In this repo

| File | What to change |
| --- | --- |
| [src/research_crew/crew.py](../../../src/research_crew/crew.py) | Add `tools=[SerperDevTool()]` to the relevant agent; add `knowledge_sources=[...]` to the `Crew` |
| [src/research_crew/knowledge_source_example.py](../../../src/research_crew/knowledge_source_example.py) | Template for `build_knowledge_sources()` — import and call it in `crew.py` |
| [step_05_rag_and_tools.ipynb](step_05_rag_and_tools.ipynb) | Run the crew and view the result — nothing to edit here |
| `knowledge/` | Add your own document here (`.txt` or `.pdf`) |

The `embedder` block is already in `crew.py` — it's what makes RAG work without an OpenAI key.

## Your task

1. Add a knowledge document to `knowledge/` that's relevant to your topic — a `.txt` file with background information works fine to start.

2. In `crew.py`, import `build_knowledge_sources` from `knowledge_source_example.py` (or write the source inline), point it at your file, and pass it to the `Crew` constructor:
   ```python
   knowledge_sources=build_knowledge_sources()
   ```

3. Add `SerperDevTool()` to the agent that searches for information, in `crew.py`:
   ```python
   tools=[SerperDevTool()]
   ```

4. Update that agent's task description in `tasks.yaml` to include a question only answerable from your knowledge document. Run it — either open [step_05_rag_and_tools.ipynb](step_05_rag_and_tools.ipynb) and run its cell, or from the terminal:
   ```bash
   uv run research_crew
   ```

5. Now run again **without** the knowledge source (comment it out). Does the agent still answer the document-specific question correctly, or does it admit it doesn't know? That comparison is the point of RAG.

6. Check the verbose log: can you see when the agent calls the search tool, and what query it used?

7. Fill in the **Step 5** section of `EVALUATION.md` and your final recommendation.

## Stretch goal

Add a PDF instead of a plain text file:
```python
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
PDFKnowledgeSource(file_paths=["your_document.pdf"])
```
Ask a question whose answer appears on a specific page. Does the agent retrieve it?

---

**This is your final submission.** See [Assignment Overview](../assignment-overview.md) for the full grading rubric and exactly what to submit.
