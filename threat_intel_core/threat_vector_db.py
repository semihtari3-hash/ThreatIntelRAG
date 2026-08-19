import chromadb
from chromadb.config import Settings
from threat_intel_core.config import VECTOR_DB_DIR, COLLECTION_NAME
from threat_intel_core.threat_embeddings import calculate_batch_vectors

_chroma_client = chromadb.PersistentClient(
    path=VECTOR_DB_DIR,
    settings=Settings(allow_reset=True)
)

def get_vector_collection():
    return _chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )

def inject_chunks_into_db(chunks):
    if not chunks:
        return

    collection = get_vector_collection()

    ids = [chunk["id"] for chunk in chunks]
    texts = [chunk["text"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]

    embeddings = calculate_batch_vectors(texts)

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )