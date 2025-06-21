from flask import Flask, request, jsonify
import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# ✅ Initialize Chroma DB Client (persistent)
chroma_client = PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="faq_docs")

# ✅ Load Sentence Transformer Model (efficient small model)
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.route("/query", methods=["POST"])
def query_faq():
    # ✅ Extract and validate JSON data
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' in request body."}), 400

    query = data["question"]
    
    # ✅ Generate embedding for query
    query_embedding = model.encode(query).tolist()

    # ✅ Perform semantic search in Chroma DB
    results = collection.query(
        query_embeddings=[query_embedding],  # <- IMPORTANT: semantic search uses 'query_embeddings' not 'query_texts'
        n_results=3,
        include=['documents', 'metadatas', 'distances']
    )

    # ✅ Format the output cleanly
    formatted = []
    for i in range(len(results['documents'][0])):
        formatted.append({
            "document": results['metadatas'][0][i]['source'],
            "content": results['documents'][0][i],
            "similarity": results['distances'][0][i]
        })

    return jsonify({"results": formatted})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
