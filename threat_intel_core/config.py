import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "threat_knowledge_base")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "threat_chroma_db")
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "threat_engine.log")

DEFAULT_CHUNK_SIZE = 1200
DEFAULT_OVERLAP = 250
DEFAULT_TOP_K = 2
COLLECTION_NAME = "cyber_threat_intel"
EMBEDDING_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"