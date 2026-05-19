from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.agent import agent_service

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    images: list[str] | None = None

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        result = await agent_service.process(request.message,request.images)
        return {"response":result}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.get("/health")
async def health():
    return {"status":"ok"}