import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

# ✅ New PersistentClient usage
chroma_client = PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="faq_docs")

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=['documents', 'metadatas', 'distances']
    )
    return results

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scripts/search_and_generate.py 'your question here'")
        sys.exit(1)

    query = sys.argv[1]
    search_results = semantic_search(query)

    print("\nTop Results:\n")
    for i in range(len(search_results['documents'][0])):
        print(f"📄 Document: {search_results['metadatas'][0][i]['source']}")
        print(f"💬 Content: {search_results['documents'][0][i]}")
        print(f"🔢 Similarity Score: {search_results['distances'][0][i]:.4f}")
        print("-" * 80)
