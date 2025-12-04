import sys
import traceback
import io
from contextlib import redirect_stdout

async def run_code_safely(code: str) -> str:
    """
    Executes Python code safely in memory.
    Returns output or error message.
    """
    str_io = io.StringIO()
    try:
        with redirect_stdout(str_io):
            exec(code, {"__builtins__": __builtins__})
    except Exception as e:
        error_trace = traceback.format_exc()
        return f"⚠️ Error during execution:\n{error_trace}"
    return str_io.getvalue() or "✅ Code ran successfully with no output."
