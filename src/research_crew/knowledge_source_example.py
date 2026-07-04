from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# Template for wiring up RAG knowledge sources — not imported by crew.py yet.
# See Step 5 (RAG + Tools). For the stretch goal, add more entries to the
# returned list (e.g. StringKnowledgeSource, PDFKnowledgeSource).


def build_knowledge_sources() -> list:
    return [
        TextFileKnowledgeSource(file_paths=["user_preference.txt"]),
    ]