import streamlit as st
import uuid
from ingestion import is_relevant, add_document, chunk_text
from rag import answer_query


def run_app():
    st.set_page_config(page_title="Concert Tour Assistant")

    st.title("🎤 Concert Tour Assistant")
    st.header("📄 Add a New Document")

    user_input = st.text_area("Enter a text related to a concert tour:")

    if st.button("Add document"):
        if not user_input.strip():
            st.warning("Please, enter a document.")
        elif not is_relevant(user_input):
            st.error("❌ Sorry, I cannot ingest documents unrelated to concert tours.")
        else:
            doc_id = str(uuid.uuid4())
            add_document(user_input, doc_id)
            chunks = chunk_text(user_input)
            st.success("✅ Document added to the database!")
            st.info(f"📌 Split into {len(chunks)} chunk(s) for indexing.")

    st.markdown("---")
    st.header("❓ Ask a Question")

    user_question = st.text_input("Ask me anything about concert tours:")

    if st.button("Get answer"):
        if user_question.strip():
            with st.spinner("Searching and generating answer..."):
                answer = answer_query(user_question)
                st.markdown(f"**Answer:** {answer}")
        else:
            st.warning("Please, enter a question.")
