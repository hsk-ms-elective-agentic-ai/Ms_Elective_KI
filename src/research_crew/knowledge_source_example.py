from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# Template for wiring up RAG knowledge sources — not imported by crew.py yet.
# See Step 10 (Tools) and Step 12 (RAG) in exercises/en/ for the concepts this
# applies. To actually use this, import build_knowledge_sources() in crew.py
# and pass its result as Crew(..., knowledge_sources=build_knowledge_sources()).
# Add more entries to the returned list for the stretch goal (e.g.
# StringKnowledgeSource, PDFKnowledgeSource).


def build_knowledge_sources() -> list:
    return [
        TextFileKnowledgeSource(file_paths=["user_preference.txt"]),
    ]