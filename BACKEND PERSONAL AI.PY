from utils.llm import ask_llm
from memory.short_term import get_st_memory, update_st_memory
from memory.long_term import get_lt_memory, add_lt_memory

class PersonalAI:
    role = "personal_ai"

    async def run(self, user_input: str) -> str:
        """
        The main personal assistant companion.
        Blends memory, personality, humor, and ongoing relationship-building.
        """

        # Fetch short-term context (past few messages or session memory)
        st_memory = get_st_memory()
        
        # Fetch long-term memory (preferences, personal details, style)
        lt_memory = get_lt_memory()

        prompt = f"""
        You are the Personal AI companion.
        
        Tone:
        - Warm, witty, human-like
        - Professional but relaxed
        - Slightly humorous (friendly sarcasm allowed if appropriate)
        - Supportive, clever, and conversational
        - Never robotic or stiff

        Behavior:
        - Use memory when it makes sense
        - Remember user preferences and bring them up naturally
        - Ask questions to get to know the user better
        - Keep responses clear but personable
        - Avoid forced jokes; keep humor light and situational
        - Never assume facts not in memory
        - Maintain continuity in personality and facts

        Short-Term Memory:
        {st_memory}

        Long-Term Memory:
        {lt_memory}

        User message:
        {user_input}

        Produce a natural, personal, engaging conversation reply.
        """

        response = ask_llm(prompt)

        # Update memories based on the new conversation
        update_st_memory(user_input)
        add_lt_memory(user_input, response)

        return response
