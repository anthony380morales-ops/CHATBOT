from orchestrator.agent_selector import choose_agent
from orchestrator.personality import apply_personality
from debug.error_catcher import safe_execute

async def process_request(user_input: str):
    try:
        # Select appropriate agent
        agent = choose_agent(user_input)

        # Execute agent with universal error catcher
        raw_response = await safe_execute(agent.run, user_input)

        # Transform response with personality layer
        final_response = apply_personality(raw_response)

        return final_response

    except Exception as e:
        return f"Something went wrong, but don't worry — I'm on it! 🛠️ Error: {str(e)}"
