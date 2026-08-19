from sentence_transformers import SentenceTransformer
from threat_intel_core.config import EMBEDDING_MODEL_NAME

_embedding_model_instance = SentenceTransformer(EMBEDDING_MODEL_NAME)

def get_embedding_engine():
    return _embedding_model_instance

def calculate_text_vector(text):
    engine = get_embedding_engine()
    vector = engine.encode(text, convert_to_numpy=True)
    return vector.tolist()

def calculate_batch_vectors(text_list):
    engine = get_embedding_engine()
    vectors = engine.encode(text_list, convert_to_numpy=True)
    return vectors.tolist()