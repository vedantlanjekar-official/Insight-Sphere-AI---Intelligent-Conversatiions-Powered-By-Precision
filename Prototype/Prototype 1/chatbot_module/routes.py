from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .service import OllamaService

router = APIRouter()
service = OllamaService()

class ChatRequest(BaseModel):
    message: str
    model: str = "llama3" # Optional, defaults to llama3

class ChatResponse(BaseModel):
    response: str

from fastapi.responses import StreamingResponse

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint to interact with Insight Sphere AI.
    Returns a streaming response.
    """
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Update model if provided
    if request.model != service.model:
        service.model = request.model

    return StreamingResponse(service.generate_response(request.message, stream=True), media_type="text/plain")
