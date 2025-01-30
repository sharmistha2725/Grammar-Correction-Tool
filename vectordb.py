from langchain_chroma import Chroma
import model
import utils

def initialize_chroma(persist_directory="./chroma_db"):
    """Initializes and returns a Chroma vector store."""
    hf_embeddings = model.create_hugging_face_embedding_model()
    vectorstore = Chroma(embedding_function=hf_embeddings, persist_directory=persist_directory)
    return vectorstore

def store_pdf_in_chroma(uploaded_file, vectorstore):
    """Processes and stores the PDF content into ChromaDB."""
    splits = utils.process_pdf_for_rag(uploaded_file)
    vectorstore.add_documents(splits)

def retrieve_from_chroma(query, vectorstore):
    """Retrieves the most relevant documents from ChromaDB."""
    retriever = vectorstore.as_retriever()
    documents = retriever.get_relevant_documents(query)
    return documents
