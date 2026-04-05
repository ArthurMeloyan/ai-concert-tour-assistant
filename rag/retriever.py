from config import get_vectordb


def retrieve_similar(query: str, k: int = 3):
    return get_vectordb().similarity_search(query=query, k=k)
