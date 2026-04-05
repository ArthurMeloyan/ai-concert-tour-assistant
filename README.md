# Concert Tour Assistant

A RAG-based Q&A chatbot for concert tour information, powered by Google Gemini.

---

## How It Works

1. You paste text documents about concert tours (announcements, schedules, news).
2. Documents are chunked, embedded, and stored in a local ChromaDB vector database.
3. When you ask a question, the system retrieves relevant chunks and generates an answer using Gemini.

---

## Architecture

```
ingestion/
  filter.py        — keyword relevance filter
  chunking.py      — text splitting via RecursiveCharacterTextSplitter
  pipeline.py      — stores chunks in ChromaDB

rag/
  retriever.py     — similarity search over stored documents
  generator.py     — answer generation via Gemini API
  qa.py            — orchestrates retrieval + generation

ui/
  app.py           — Streamlit interface

config.py          — centralized settings, lazy vectordb singleton
main.py            — entry point
```

### Technologies

- Python 3.11+
- Google Gemini (`gemini-2.5-flash` for generation, `gemini-embedding-001` for embeddings)
- LangChain (Google GenAI + Chroma integrations)
- ChromaDB for local vector storage
- Streamlit for UI

---

## Setup

### 1. Clone

```bash
git clone https://github.com/ArthurMeloyan/ai-concert-tour-assistant.git
cd ai-concert-tour-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure `.env`

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your key from [Google AI Studio](https://aistudio.google.com/apikey).

### 4. Run

```bash
streamlit run main.py
```

Open http://localhost:8501 in your browser.

---

## Usage

**Adding documents** — Paste concert-related text and click "Add document". The text is chunked and indexed automatically.

**Asking questions** — Type a question about concert tours and click "Get answer". The assistant retrieves relevant context from your documents and generates an answer via Gemini.

---

## Design Choices

- **ChromaDB** — fast local vector search, no external DB required.
- **Gemini API** — handles both embeddings and generation, single provider simplifies auth and billing.
- **Lazy initialization** — models and DB connections load on first use, not at import time.
- **Shared vectordb singleton** — one Chroma instance used by both ingestion and retrieval, avoiding duplicate model loading.
- **Environment variables** — API keys stay out of source code.

---

## Docker

### Build and run

```bash
docker-compose up --build -d
```

### Stop

```bash
docker-compose down
```

The `docker-compose.yml` mounts `./chroma_db` as a volume so vector data persists across container restarts. The `.env` file is injected via `env_file` — it is never baked into the image.
