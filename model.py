from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

def create_chat_qroq():
    '''
    Function to initialize chat groq for grammar checking
    
    Returns :
        chatgroq
    '''
    return ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=1,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
def create_hugging_face_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates and returns a configured instance of the HuggingFace embeddings model.
    """
    return HuggingFaceEmbeddings(model_name=model_name)