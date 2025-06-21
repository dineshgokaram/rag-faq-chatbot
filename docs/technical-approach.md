# Technical Approach and Rationale

## ✅ Problem Statement

Develop a **Retrieval-Augmented Generation (RAG)** powered FAQ chatbot for **Altibbe Health Pvt Ltd**, capable of retrieving contextually relevant answers to user questions from a provided set of FAQ documents.

---

## ⚙️ Architecture Overview

```plaintext
User Query (POST /faq-query)
        ↓
n8n Webhook → HTTP Request → Flask API → Semantic Search (Chroma)
        ↓
Semantic Results → n8n → Response Formatting → JSON Output to User
```

---

## 📌 Technology Stack

| Component       | Choice                                   | Why?                                           |
| --------------- | ---------------------------------------- | ---------------------------------------------- |
| Embeddings      | SentenceTransformer (`all-MiniLM-L6-v2`) | Lightweight, free, local                       |
| Vector Database | **Chroma** (PersistentClient)            | Free, local storage, fast semantic search      |
| Orchestration   | **n8n**                                  | Visual workflows, error handling, transparency |
| Web Framework   | **Flask**                                | Lightweight REST API, quick integration        |

---

## 🏗️ Implementation Rationale

### ➤ **Document Ingestion**

* Documents (markdown/text) are read → Tokenized → Split into 500-token chunks
* Each chunk converted to an **embedding vector** and stored in **Chroma DB** along with source metadata

### ➤ **Retrieval**

* User query → Converted to embedding → Semantic search in Chroma
* Top 3 results returned with:

  * 📄 **Document Name (source)**
  * 💬 **Content Chunk**
  * 🔢 **Similarity Score (for transparency)**

### ➤ **n8n Orchestration**

* HTTP Webhook (→ POST /faq-query)
* HTTP Request node → Calls Flask API with the question
* Respond to Webhook → Clean JSON response

---

## 🚧 Challenges Faced

| Challenge                            | Resolution                                        |
| ------------------------------------ | ------------------------------------------------- |
| OpenAI API Key Limits (quota)        | Switched to local SentenceTransformer embeddings  |
| Pinecone deprecated usage            | Replaced with local **Chroma** for cost savings   |
| Chroma configuration update required | Migrated to **PersistentClient** API              |
| Webhook 404 during testing           | Solved by using active workflows & production URL |

---

## ⚡ Performance Considerations

* Works **fast** for small to medium FAQ sets
* Purely **local** processing → No external costs
* Easily extensible for multi-modal (PDF, images)

---

## 📈 Future Scalability Ideas

* Integrate **OpenAI GPT** for contextual augmentation
* Implement **response caching** for common queries
* Add **real-time document ingestion** support
* Develop a **dashboard** for analytics on queries and usage
* Extend to **multi-modal** inputs (PDF parsing, OCR for images)

---

**Virtuous Technology Principles followed:**

* ✅ **Integrity:** Transparent responses with similarity scores
* ✅ **Diligence:** Error handling, tested thoroughly
* ✅ **Empathy:** User-friendly, JSON formatted output
* ✅ **Wisdom:** Focused on responsible, cost-effective AI development

