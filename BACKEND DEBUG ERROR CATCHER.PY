import traceback
from debug.debug_agent import DebugAgent

debug_agent = DebugAgent()

async def safe_execute(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)

    except Exception as e:
        error_text = traceback.format_exc()
        debug_info = await debug_agent.analyze_error(error_text)

        return (
            "⚠️ Oops — something tripped internally.\n\n"
            f"**Error:** {str(e)}\n\n"
            f"**Analysis:**\n{debug_info}"
        )

def register_exception_handler(app):
    @app.exception_handler(Exception)
    async def unicorn_handler(request, exc):
        error_text = traceback.format_exc()
        debug_info = await debug_agent.analyze_error(error_text)
        return {"error": str(exc), "analysis": debug_info}
