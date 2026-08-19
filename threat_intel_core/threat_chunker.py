import uuid

def split_text_into_chunks(documents, chunk_size=1000, overlap=150):
    all_chunks = []

    for doc in documents:
        text = doc.get("text", "")
        source = doc.get("source", "unknown")
        
        if not text.strip():
            continue

        words = text.split()
        chunk_idx = 0
        
        i = 0
        while i < len(words):
            chunk_words = words[i : i + chunk_size]
            chunk_text = " ".join(chunk_words)
            
            all_chunks.append({
                "id": f"{source}_chunk_{chunk_idx}_{uuid.uuid4().hex[:6]}",
                "text": chunk_text,
                "metadata": {"source": source, "chunk_index": chunk_idx}
            })
            
            chunk_idx += 1
            i += (chunk_size - overlap)

    return all_chunks