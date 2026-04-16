from sentence_transformers import SentenceTransformer
from typing import List

MODEL_NAME="sentence-transformers/all-mpnet-base-v2"
model=SentenceTransformer(MODEL_NAME)


def embed_chunks(chunks :List[str]) -> List[List[float]]:
    """
    Convert a list of text chunks into a list of embedding vectors.
    
    Args:
        chunks: list of text strings to embed
    
    Returns:
        list of embeddings, each embedding is a list of 768 floats
    """
    embeddings=model.encode(chunks,show_progress_bar=True)
    return embeddings.tolist()

def embed_query(query: List[str])->List[float]:
    """
    Convert a single query string into an embedding vector.
    
    Args:
        query: the user's question
    
    Returns:
        single embedding as a list of 768 floats
    """
    embedding=model.encode(query)
    return embedding.tolist()