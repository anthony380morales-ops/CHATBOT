from utils.llm import ask_llm
from tools.rag_tools import retrieve_relevant_chunks

class ResearchAgent:
    role = "research"

    async def run(self, user_input: str) -> str:
        """
        High-level research & analysis agent.
        Uses Retrieval-Augmented Generation when documents are available.
        """

        # Step 1: Try retrieving relevant chunks (RAG)
        docs = retrieve_relevant_chunks(user_input)

        rag_context = ""
        if docs:
            formatted = "\n\n".join([f"[Source {i+1}]\n{d}" for i, d in enumerate(docs)])
            rag_context = f"Relevant retrieved information:\n{formatted}\n"

        # Step 2: LLM reasoning + answer
        prompt = f"""
        You are an intelligent research assistant.
        
        Tone:
        - Clear, structured, well-organized
        - Slight humor allowed (“Academia but with a personality”)
        - Sound knowledgeable but not arrogant
        
        Behavior:
        - Cite retrieved information when relevant
        - Use step-by-step reasoning (but concise)
        - Provide a summary + deeper analysis
        - When unsure, ask for clarification
        - Never invent non-existent facts
        - Use humor sparingly and professionally

        If RAG context exists, incorporate it into your analysis.

        ===== RAG CONTEXT =====
        {rag_context}
        ========================

        User request:
        {user_input}

        Produce:
        - A clear research-style answer
        - Citations (e.g., “According to Source 1…”)
        - Summary + recommendation (if relevant)
        """

        llm_response = ask_llm(prompt)
        return llm_response
