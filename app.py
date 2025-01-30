from dotenv import load_dotenv
import streamlit as st
import chain
load_dotenv()
def grammar_checker_app():
    """
    Grammar Checker App with Streamlit, allowing users to input text and select a writing style.
    Includes a button to check grammar and display corrected output.
    """
    # Sidebar configuration
    st.sidebar.title("Menu")
    section = st.sidebar.radio(
        "Choose a section:",
        ("Grammar Checker",)
    )
    
    # Grammar Checker UI
    if section == "Grammar Checker":
        st.title("Grammar Checker ✍️")

        with st.form("grammar_checker"):
            style = st.selectbox(
                "Choose a writing style:",
                ["Formal", "Casual", "Academic", "Creative", "Technical"]
            )
            text = st.text_area("Enter text to check:")
            submitted = st.form_submit_button("Check Grammar")
            
            if submitted:
                corrected_text = chain.check_grammar(text, style)
                st.info(corrected_text)

# Run the app
grammar_checker_app()
