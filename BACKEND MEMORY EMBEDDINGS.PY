import numpy as np

def embed_text(text: str):
    """
    Placeholder embedding model for now.
    Replace with actual embeddings (OpenAI, HF, local model).

    Currently returns a reproducible random vector.
    """

    np.random.seed(abs(hash(text)) % (10**6))
    return np.random.rand(384).tolist()  # 384-dimension vector

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two vectors.
    """
    a = np.array(a)
    b = np.array(b)

    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
