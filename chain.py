from model import create_chat_qroq
import prompts

def check_grammar(text, style):
    """
    Function to check and correct grammar.
    """
    prompt_template = prompts.grammar_checker_prompt()
    llm = create_chat_qroq()

    chain = prompt_template | llm

    response = chain.invoke({
        "text": text,
        "style": style
    })

    print("Raw LLM Response:", response.content)

    return extract_text_content(response.content)  # Extract corrected text output

def extract_text_content(response_text):
    """
    Extracts the corrected text from the LLM response and returns it as a string.
    """
    print("Raw response:", response_text)  # Debugging print

    try:
        return response_text.strip()
    except Exception as e:
        print("Error while extracting text content:", e)
        return "Error: Failed to extract text content."