from langchain_core.prompts import ChatPromptTemplate

def grammar_checker_prompt():
    """
    Generates a prompt template for grammar checking.
    """
    system_msg = """
        You are an advanced grammar checker assistant. Your task is to correct grammatical errors and improve clarity while maintaining the original intent.
        
        Provide the corrected text in a simple format:
        
        Original: I has a apple.
        Corrected: I have an apple.
    """

    user_msg = "Check and correct the following text in {style} style:\n{text}"

    return ChatPromptTemplate.from_messages([("system", system_msg), ("user", user_msg)])
