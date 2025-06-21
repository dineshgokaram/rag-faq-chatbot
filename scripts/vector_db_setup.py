import os
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ New PersistentClient for Chroma
chroma_client = PersistentClient(path="./chroma_db")

collection_name = "faq_docs"
collection = chroma_client.get_or_create_collection(name=collection_name)

def read_documents(folder):
    docs = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if filename.endswith(('.txt', '.md')):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                docs.append((filename, content))
    return docs

def upload_embeddings():
    documents = read_documents("data/sample-documents")
    for doc_name, content in documents:
        embedding = model.encode(content).tolist()
        collection.add(
            documents=[content],
            metadatas=[{"source": doc_name}],
            ids=[doc_name]
        )
        print(f"✅ Uploaded '{doc_name}' to local Chroma vector store.")

    print("✅ All documents processed and stored in local Chroma DB.")

if __name__ == "__main__":
    upload_embeddings()
