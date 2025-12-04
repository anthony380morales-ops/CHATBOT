from fastapi import FastAPI
from router import router
from utils.logger import init_logging
from debug.error_catcher import register_exception_handler

app = FastAPI(
    title="Unified Multi-Agent AI System",
    description="AI with coding, therapy, research, customer-service, debugging, memory, and multi-agent orchestration",
    version="1.0"
)

# Logging system
init_logging()

# Global routes
app.include_router(router)

# Register universal error handler
register_exception_handler(app)

@app.get("/")
async def root():
    return {"status": "running", "message": "Unified AI System Online 😄"}
