from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# build_knowledge_sources() is wired into crew.py's Crew(knowledge_sources=...).
# See Step 11 (Tools) and Step 13 (RAG) in exercises/en/ for the concepts this
# applies. Add more entries to the returned list for the stretch goal (e.g.
# StringKnowledgeSource).


def build_knowledge_sources() -> list:
    return [
        TextFileKnowledgeSource(file_paths=["user_preference.txt"]),
        # crewai extracts each PDF page's text via pdfplumber (already a
        # direct crewai dependency, no separate install needed) before chunking.
        PDFKnowledgeSource(file_paths=["rag-data.pdf"]),
    ]