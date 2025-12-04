import json
import os
from memory.embeddings import embed_text, cosine_similarity

LT_MEMORY_FILE = "backend/memory/long_term_store.json"

# Ensure file exists
if not os.path.exists(LT_MEMORY_FILE):
    with open(LT_MEMORY_FILE, "w") as f:
        json.dump([], f)

def load_memory():
    with open(LT_MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(LT_MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_lt_memory() -> str:
    """
    Returns the long-term memory items as a readable text block.
    """
    memories = load_memory()
    if not memories:
        return "No long-term memories yet."
    return "\n".join([m["text"] for m in memories])

def add_lt_memory(user_input: str, ai_output: str):
    """
    Adds important memories based on user text.

    Rules:
    - Add facts about user's preferences
    - Add recurring themes
    - Avoid adding trivial messages
    """

    text = user_input.lower()

    important_keywords = [
        "i like", "i prefer", "my favorite", "i love",
        "i dislike", "i want", "my goal", "i plan to",
        "i'm working on", "i have a project"
    ]

    # Check if input contains memory-worthy info
    if not any(k in text for k in important_keywords):
        return  # Skip trivial lines

    memory_vector = embed_text(user_input)

    memory_entry = {
        "text": user_input,
        "vector": memory_vector
    }

    all_memories = load_memory()
    all_memories.append(memory_entry)
    save_memory(all_memories)
