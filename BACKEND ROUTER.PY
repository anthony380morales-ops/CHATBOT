from fastapi import APIRouter
from orchestrator.core_router import process_request

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(payload: dict):
    user_input = payload.get("message", "")
    response = await process_request(user_input)
    return {"response": response}
