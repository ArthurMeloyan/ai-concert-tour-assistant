from config import get_vectordb
from .chunking import chunk_text


def add_document(text: str, doc_id: str):
    chunks = chunk_text(text)
    ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
    get_vectordb().add_texts(chunks, ids=ids)
