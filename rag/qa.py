from .retriever import retrieve_similar
from .generator import generate_answer

def answer_query(query: str) -> str:
    documents = retrieve_similar(query=query, k=3)
    context = "\n\n".join([doc.page_content for doc in documents])

    prompt = f"""
        You are a helpful assistant. Answer the user's question based on the context below.

        Context:
        {context}

        Question: {query}

        Answer:
    """

    return generate_answer(prompt)