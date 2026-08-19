from threat_intel_core.threat_embeddings import calculate_text_vector
from threat_intel_core.threat_vector_db import get_vector_collection

def search_threat_knowledge_base(query, top_k=2):
    collection = get_vector_collection()
    query_vector = calculate_text_vector(query)

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    search_results = []
    if results and "documents" in results and results["documents"] and results["documents"][0]:
        for i in range(len(results["documents"][0])):
            doc_text = results["documents"][0][i]
            if doc_text:
                search_results.append({
                    "text": doc_text,
                    "id": results["ids"][0][i] if "ids" in results else f"doc_{i}",
                    "metadata": results["metadatas"][0][i] if "metadatas" in results else {},
                    "distance": results["distances"][0][i] if "distances" in results and results["distances"] else 0.0
                })

    return search_results