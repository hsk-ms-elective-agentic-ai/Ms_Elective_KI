# Step 5 — RAG + Tools

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/05-rag-and-tools.md)

Add two forms of external grounding to the step 4 crew. **Tools** (`SerperDevTool`) let the agent retrieve live information from the web at runtime. **RAG** (a `TextFileKnowledgeSource`) lets the crew retrieve from a specific document you provide. Both address the same root limitation in steps 1–4: the LLM's knowledge is frozen at training time and doesn't know about your specific documents.

## Background

### Tools

The demonstration that a language model can learn *when* to call a tool, *which* tool, and *what arguments* to pass — rather than a human hardcoding every call — was:

> Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

![Toolformer: model inserting API calls into its own generated text for QA, calculator, translation, Wikipedia search](../assets/toolformer-schick2023-fig1.png)
*Figure 1 from Schick et al. (2023): Toolformer autonomously inserting tool calls. Reproduced for educational use in this course.*

### RAG

Retrieval-Augmented Generation: chunk a document, embed each chunk into a vector, store the vectors, and retrieve the most similar chunks for a query to feed into the LLM's context. The original paper:

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020, 9459–9474. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG architecture: query encoder + retriever feed top-k documents into a generator](../assets/rag-lewis2020-fig1.png)
*Figure 1 from Lewis et al. (2020): RAG architecture. Reproduced for educational use in this course.*

**One practical trap**: embeddings use a separate model from the chat LLM. This crew uses Groq for chat (free) and Gemini for embeddings (also free) — two different API keys, two different rate limits. This is why `GEMINI_API_KEY` exists in `.env.example`.

## The code

Open [src/exercises/step_05_rag_and_tools.py](../../src/exercises/step_05_rag_and_tools.py). Additions from step 4:

| Added | What it does |
| --- | --- |
| `SerperDevTool()` | Live web search — agent decides when to call it |
| `tools=[web_search]` on researcher | Registers the tool with the agent |
| `TextFileKnowledgeSource(...)` | Embeds `knowledge/user_preference.txt` into a vector store |
| `knowledge_sources=[...]` on Crew | Passes the knowledge to all agents at retrieval time |
| `embedder={...}` on Crew | Routes embedding calls to Gemini instead of the default OpenAI |

## Your task

1. Set `TOPIC` to the same topic as the previous steps.

2. Run it:
   ```bash
   uv run python src/exercises/step_05_rag_and_tools.py
   ```

3. Compare the output to step 4:
   - Does the researcher's output contain information that's clearly more current or more specific than in step 4?
   - Did the knowledge from `user_preference.txt` appear anywhere in the output?
   - Check the verbose log: can you see the moment the agent calls the search tool, and what query it used?

4. **Add your own knowledge source**: create a relevant document in `knowledge/` (a `.txt` summary of something related to your topic) and add it as a second `TextFileKnowledgeSource`. Ask a question in the task description that can only be answered from that document. Confirm retrieval worked — run without the document and check whether the agent still answers correctly or now admits it doesn't know.

5. Fill in the **Step 5** section of `EVALUATION.md` and your final recommendation.

## Stretch goal

Add a PDF instead of a text file: `from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource`. Use a real document relevant to your topic (a policy paper, a research summary, a product brief). Then test the retrieval by asking a question whose answer appears on a specific page of the PDF — does the agent retrieve it?

---

**This is your final submission.** See [Assignment Overview](assignment-overview.md) for the full grading rubric and exactly what to submit.
