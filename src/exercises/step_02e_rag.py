"""
Step 2e — Retrieval-Augmented Generation (RAG)
------------------------------------------------
Same idea as step 5's RAG, but done by hand with plain completion() calls and
a local vector store (chromadb) instead of a CrewAI agent and its
knowledge_sources.

Two phases (handled by the helper functions below, you don't need to read or
edit them):
1. Read your document, split it into chunks, and index them in chromadb —
   this runs fully locally, no API key needed for this part.
2. Retrieve the chunks most similar to your question — this is the "R" in RAG.
   Stuff them into the system message as grounding context, then ask the
   question — this is the "AG" (augmented generation).

Compare to step 1 (zero-shot): does grounding the model in retrieved text
change or correct its answer?

Setup:
    Add a .txt or .pdf file with background on your topic to knowledge/, then
    point KNOWLEDGE_FILE at it below.

Run:
    uv run python src/exercises/step_02e_rag.py
"""
import os

import chromadb
import fitz  # PyMuPDF
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
os.makedirs("output", exist_ok=True)


# ── Everything below this line is provided — you don't need to read or edit it ──
def read_document(path: str) -> str:
    """Extract the text of a .txt or .pdf file."""
    if path.lower().endswith(".pdf"):
        with fitz.open(path) as pdf:
            return "\n\n".join(page.get_text() for page in pdf)
    with open(path, encoding="utf-8") as f:
        return f.read()


def retrieve_relevant_context(document_text: str, question: str, top_k: int = 3) -> str:
    """Split the document into paragraphs, index them in a local vector store,
    and return the paragraphs most similar to the question. Retrieving more than
    one guards against a short, topic-y paragraph (e.g. a title) outscoring the
    paragraph that actually contains the answer."""
    chunks = [chunk.strip() for chunk in document_text.split("\n\n") if chunk.strip()]
    collection = chromadb.Client().create_collection("knowledge")
    collection.add(documents=chunks, ids=[str(i) for i in range(len(chunks))])
    result = collection.query(query_texts=[question], n_results=min(top_k, len(chunks)))
    return "\n\n".join(result["documents"][0])
# ── End of provided code ──────────────────────────────────────────────────────


# ── Your part — upload a .txt or .pdf file to knowledge/, then fill these in ──
KNOWLEDGE_FILE = "knowledge/TODO-your-document.txt"
question = "TODO: a question only answerable from your document"

document_text = read_document(KNOWLEDGE_FILE)
relevant_context = retrieve_relevant_context(document_text, question)

system_message = (
    "Answer only using the context below. "
    "If the answer isn't in the context, say you don't know.\n\n"
    f"Context:\n{relevant_context}"
)

response = completion(
    model=os.getenv("MODEL", "gemini/gemini-2.5-flash"),
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": question},
    ],
)

output = response.choices[0].message.content
print(output)

with open("output/step_02e.md", "w", encoding="utf-8") as f:
    f.write(
        f"# Step 2e — Retrieval-Augmented Generation\n\n"
        f"**Question:** {question}\n\n"
        f"## Retrieved context\n\n```\n{relevant_context}\n```\n\n"
        f"## System message\n\n```\n{system_message}\n```\n\n"
        f"## Output\n\n{output}\n"
    )
