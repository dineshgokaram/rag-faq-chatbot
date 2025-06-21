# RAG-powered FAQ Chatbot

## 📚 Overview

This project is a Retrieval-Augmented Generation (RAG) FAQ chatbot designed to provide accurate, sourced answers to user questions by combining semantic search with large language models (LLMs). The system retrieves relevant information from a knowledge base of embedded documents and generates natural responses, ensuring transparency and source attribution.


---

## ⚙️ Features

* ✅ **Semantic Search** with **Chroma Vector DB**
* ✅ **Embeddings** via **SentenceTransformers** (local, no API costs)
* ✅ **Workflow Orchestration** using **n8n**
* ✅ **Web API Integration** with **Flask**
* ✅ **Ethical Design:** Transparent retrieval, source attribution

---

## 🏗️ Project Structure

```
rag-chatbot-project/
├── workflows/                  # n8n workflow JSON
├── scripts/                    # Vector DB setup and search scripts
├── data/sample-documents/      # Input FAQ files (txt/md)
├── chroma_db/                  # Local Chroma DB files
├── tests/                      # Example test queries
├── docs/                       # README and technical approach
└── .env.example                # Example environment variables
```

---

## 🚀 Setup Instructions

1️⃣ **Clone the repository**

```bash
git clone <your-repo-url>
cd rag-chatbot-project
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Environment Setup**

* Create `.env` based on `.env.example`
* Example:

```ini
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHROMA_DB_DIR=./chroma_db
```

4️⃣ **Run the Flask API (retrieval service)**

```bash
python scripts/search_and_generate.py
```

5️⃣ **Start n8n**

```bash
n8n start
```

→ Import the provided workflow file (`workflows/rag-chatbot-workflow.json`) in the n8n UI.

6️⃣ **Test via Postman**

```http
POST https://<your-n8n-instance>/webhook/faq-query
Body (JSON): { "question": "Do you offer online consultations?" }
```

---

## 🧪 Testing

Example test queries are available in:

```
tests/sample-queries.json
```

---

## 💡 Future Improvements

* ✅ Multi-modal support (PDF, images)
* ✅ LLM integration (OpenAI, Anthropic, or OSS models)
* ✅ Real-time indexing of new documents
* ✅ Caching for repeated queries
* ✅ Analytics Dashboard

---

##Screenshots
![image](https://github.com/user-attachments/assets/c4f6bcaf-311f-49b6-8bfa-7b40bba7cd64)


