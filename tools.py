from langchain.agents import Tool
from chain import generate_correction_chain, generate_correction_rag_chain
from vectordb import retrieve_from_chroma

def grammar_checker_tool():
    return Tool(
        name="Grammar Checker",
        func=generate_correction_chain,
        description="Checks and corrects grammar, spelling, and punctuation."
    )

def rag_retriever_tool(vectorstore):
    return Tool(
        name="RAG Retriever",
        func=lambda query: "\n\n".join(doc.page_content for doc in retrieve_from_chroma(query, vectorstore)),
        description="Retrieves relevant grammar rules and contextual examples."
    )