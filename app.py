# from dotenv import load_dotenv
# import streamlit as st
# import chain
# load_dotenv()
# def grammar_checker_app():
#     """
#     Grammar Checker App with Streamlit, allowing users to input text and select a writing style.
#     Includes a button to check grammar and display corrected output.
#     """
#     # Sidebar configuration
#     st.sidebar.title("Menu")
#     section = st.sidebar.radio(
#         "Choose a section:",
#         ("Grammar Checker",)
#     )
    
#     # Grammar Checker UI
#     if section == "Grammar Checker":
#         st.title("Grammar Checker ✍️")

#         with st.form("grammar_checker"):
#             style = st.selectbox(
#                 "Choose a writing style:",
#                 ["Formal", "Casual", "Academic", "Creative", "Technical"]
#             )
#             text = st.text_area("Enter text to check:")
#             submitted = st.form_submit_button("Check Grammar")
            
#             if submitted:
#                 corrected_text = chain.check_grammar(text, style)
#                 st.info(corrected_text)

# # Run the app
# grammar_checker_app()

import streamlit as st
import chain
import vectordb
import agents

def grammar_checker_app():
    """
    Grammar Checker App with Streamlit, featuring RAG and Agent-based corrections.
    Includes a sidebar with sections for grammar checking and RAG file ingestion.
    """

    # Sidebar configuration
    st.sidebar.title("Menu")
    section = st.sidebar.radio(
        "Choose a section:",
        ("Grammar Checker RAG", "RAG File Ingestion")
    )

    # Initialize vector database
    vectorstore = vectordb.initialize_chroma()

    # Grammar Checker Section
    if section == "Grammar Checker RAG":
        st.title("Grammar Checker 📝")

        with st.form("grammar_checker"):
            input_text = st.text_area("Enter your text:", height=250)
            submitted = st.form_submit_button("Check Grammar")

            is_rag_enabled = st.checkbox("Enable RAG Contextual Corrections")
            is_agent_enabled = st.checkbox("Enable Agent-Based Correction")

            if submitted:
                if is_rag_enabled and is_agent_enabled:
                    response = agents.generate_correction_with_rag_agent(input_text, vectorstore)
                elif is_agent_enabled:
                    response = agents.generate_correction_with_agent(input_text)
                elif is_rag_enabled:
                    response = chain.generate_correction_rag_chain(input_text, vectorstore)
                else:
                    response = chain.check_grammar(input_text)
                
                st.subheader("Corrected Text ✨")
                st.text_area("Here is your corrected text:", response, height=200)

    # RAG File Ingestion Section
    elif section == "RAG File Ingestion":
        st.title("RAG File Ingestion 📂")

        uploaded_file = st.file_uploader("Upload a file:", type=["txt", "csv", "docx", "pdf"])

        if uploaded_file is not None:
            vectordb.store_text_in_chroma(uploaded_file, vectorstore)
            st.success(f"File '{uploaded_file.name}' uploaded and stored in the vector database successfully!")

# Run the app
grammar_checker_app()