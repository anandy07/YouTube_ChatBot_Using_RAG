# 🎥 YouTube AI Chatbot

An AI-powered chatbot that answers questions about any YouTube video
using its transcript.

The app uses **Retrieval-Augmented Generation (RAG)**: it fetches the
video transcript, indexes it in a FAISS vector store, retrieves the
chunks most relevant to your question, and passes them to a Groq-hosted
LLM to generate a grounded answer.

---

## 🚀 Features

- 🔗 Paste a YouTube URL (`watch`, `youtu.be`, `shorts`, and `embed` links are supported)
- 📜 Fetch the video's English transcript automatically
- ✂️ Split the transcript into overlapping chunks
- 🧠 Embed chunks with Hugging Face `all-MiniLM-L6-v2`
- 🗂️ Store and search embeddings with FAISS
- 🤖 Generate answers with Groq (`openai/gpt-oss-120b`)
- 🛡️ Answers stay grounded in the transcript; if the answer isn't in the video, the bot says so
- ▶️ Preview the video in the app
- 💬 Chat history for the current video (newest first)

---

## 🧠 Architecture

```text
YouTube URL
     │
     ▼
Video ID extraction            (src/youtube.py)
     │
     ▼
YouTube Transcript API         (src/youtube.py)
     │
     ▼
Text chunking                  (src/rag.py)
  chunk_size=1000, overlap=200
     │
     ▼
Hugging Face embeddings        (src/rag.py)
     │
     ▼
FAISS vector store             (src/rag.py)
     │
     ▼
Similarity search (top 4)      (src/llm.py)
     │
     ▼
Prompt + Groq LLM              (src/llm.py)
     │
     ▼
Answer                         (app.py)
```

---

## 📁 Project Structure

```text
.
├── app.py              # Streamlit UI and session state
├── requirements.txt    # Python dependencies
└── src/
    ├── youtube.py      # Video ID parsing and transcript fetching
    ├── rag.py          # Chunking, embeddings, FAISS vector store
    └── llm.py          # Retrieval, prompt template, Groq LLM call
```

---

## 🛠️ Tech Stack

| Component     | Tool                                         |
| ------------- | -------------------------------------------- |
| UI            | Streamlit                                    |
| Transcripts   | `youtube-transcript-api`                     |
| Orchestration | LangChain                                    |
| Embeddings    | `sentence-transformers/all-MiniLM-L6-v2`     |
| Vector store  | FAISS (`faiss-cpu`)                          |
| LLM           | Groq — `openai/gpt-oss-120b`                 |

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/anandy07/YouTube_ChatBot_Using_RAG.git
cd YouTube_ChatBot_Using_RAG
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free key from the [Groq Console](https://console.groq.com/keys).

### 5. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 💡 Usage

1. Paste a YouTube video URL and click **Process Video**.
2. Wait for the transcript to be fetched and indexed.
3. Type a question about the video and click **Ask AI**.
4. Ask as many follow-up questions as you like. Processing a new video
   clears the chat history.

---

## ⚠️ Limitations

- Only videos with an **English** transcript (manual or auto-generated) are supported.
- The vector store is kept in memory and rebuilt each time a video is processed.
- The first run downloads the embedding model from Hugging Face, so it may take a little longer.
- Each question is answered independently; previous chat turns are not sent to the LLM.
