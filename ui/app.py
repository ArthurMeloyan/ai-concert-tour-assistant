import streamlit as st
from ingestion import is_revelant, add_document, summarize_text
import uuid
from rag.qa import answer_query

def run_app():

    st.set_page_config(page_title='Concert Tour Assistant')

    st.title("🎤 Concert Tour Assistant")
    st.header("📄 Add a New Document")

    user_input = st.text_area("Enter a text related to a concert tour:")

    if st.button("Add document"):
        if not user_input.strip():
            st.warning("Please, entet a document")
        else:
            if not is_revelant(user_input):
                st.error("❌ Sorry, I cannot ingest documents unrelated to concert tours.")
            else:
                summary = summarize_text(user_input)
                doc_id = str(uuid.uuid4())
                add_document(user_input, doc_id)
                st.success("✅ Thank you for sharing! Your document has been successfully added to the database!")
                st.info(f"📌 Here is a brief summary of the data from the document: {summary}")
    st.markdown('---')
    st.header('❓ Ask a Question')

    user_question = st.text_input('Ask me anything about concert tours:')
    artist_name = st.text_input('Or enter a musician/band name for online concert search:')


    if st.button("Get answer"):
        if user_question.strip():
            with st.spinner("Searching and generating answer..."):
                answer = answer_query(user_question)
                st.markdown(f"**Answer:** {answer}")
        else:
            st.warning("Please, enter a question")

                