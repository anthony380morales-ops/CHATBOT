from memory.long_term import load_memory
from memory.embeddings import embed_text, cosine_similarity

def retrieve_relevant_chunks(query: str, top_k: int = 3) -> list:
    """
    Retrieve the top_k most relevant long-term memory chunks for a query.
    """
    all_memories = load_memory()
    if not all_memories:
        return []

    query_vector = embed_text(query)
    similarities = [
        (cosine_similarity(query_vector, m["vector"]), m["text"])
        for m in all_memories
    ]

    similarities.sort(key=lambda x: x[0], reverse=True)
    return [text for score, text in similarities[:top_k] if score > 0.6]  # threshold
