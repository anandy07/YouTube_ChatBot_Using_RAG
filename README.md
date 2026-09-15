# 🎥 YouTube AI Chatbot

An AI-powered YouTube chatbot that allows users to ask questions
about a YouTube video using its transcript.

The application uses Retrieval-Augmented Generation (RAG) to
retrieve relevant parts of the video transcript before generating
an answer with an LLM.

---

## 🚀 Features

- 🔗 Enter a YouTube video URL
- 📜 Extract YouTube transcripts
- ✂️ Split transcripts into smaller chunks
- 🧠 Generate text embeddings
- 🔎 Semantic similarity search
- 🗂️ FAISS vector database
- 🤖 Groq LLM
- 💬 Ask questions about the video
- ▶️ Preview the YouTube video
- 📚 Conversation history
- 🌐 Deployable on Render

---

## 🧠 Architecture

```text
YouTube URL
     │
     ▼
YouTube Transcript API
     │
     ▼
Transcript
     │
     ▼
Text Chunking
     │
     ▼
Hugging Face Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Similarity Search
     │
     ▼
Relevant Transcript
     │
     ▼
Groq LLM
     │
     ▼
Answer# YouTube-ChatBot-Using-RAG
# YouTube_ChatBot_Using_RAG
