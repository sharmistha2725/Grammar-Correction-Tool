from langchain.agents import initialize_agent
from langchain.agents import AgentType
from tools import grammar_checker_tool, rag_retriever_tool
import models

def generate_correction_with_agent(text):
    """
    Uses an agent to perform grammar correction.
    """
    agent_executor = initialize_agent(
        tools=[grammar_checker_tool()],
        llm=models.create_chat_groq_model(),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent_executor.run(text)

def generate_correction_with_rag_agent(text, vectorstore):
    """
    Uses an agent with RAG retrieval for grammar correction.
    """
    agent_executor = initialize_agent(
        tools=[grammar_checker_tool(), rag_retriever_tool(vectorstore)],
        llm=models.create_chat_groq_model(),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent_executor.run(text)