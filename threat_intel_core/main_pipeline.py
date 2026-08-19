import os
from threat_intel_core.config import KNOWLEDGE_BASE_DIR, LOG_DIR, LOG_FILE
from threat_intel_core.threat_loader import load_threat_documents
from threat_intel_core.threat_chunker import split_text_into_chunks
from threat_intel_core.threat_vector_db import inject_chunks_into_db
from threat_intel_core.threat_search import search_threat_knowledge_base
from threat_intel_core.foundry_llm import process_threat_query_stream

os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

def write_system_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")

def run_threat_ingest(chunk_size, overlap):
    write_system_log("Threat ingestion started.")
    documents = load_threat_documents(KNOWLEDGE_BASE_DIR)
    if not documents:
        write_system_log("Knowledge base is empty.")
        return 0
    
    chunks = split_text_into_chunks(documents, chunk_size, overlap)
    inject_chunks_into_db(chunks)
    write_system_log(f"Successfully ingested {len(chunks)} chunks.")
    return len(chunks)

def run_threat_rag(query, history, chunk_size, overlap, top_k, model_name, temperature):
    write_system_log(f"Query received: {query}")
    search_results = search_threat_knowledge_base(query, top_k)
    
    if not search_results:
        yield "", history + [{"role": "user", "content": query}, {"role": "assistant", "content": "Tehdit veritabanında bu sorguya dair bir eşleşme bulunamadı."}]
        return

    context_segments = [item["text"] for item in search_results if item.get("text")]
    context_str = "\n\n---\n\n".join(context_segments)

    llm_stream = process_threat_query_stream(context_str, query, temperature, model_name)
    full_response = ""
    for token in llm_stream:
        full_response += token
        updated_history = history + [
            {"role": "user", "content": query},
            {"role": "assistant", "content": full_response}
        ]
        yield "", updated_history