from fastapi import APIRouter, HTTPException,UploadFile,File,Form
from pydantic import BaseModel
from app.services.agent import agent_service

router = APIRouter()

@router.post("/chat")
async def chat(message: str = Form(...), file: UploadFile = File(None)):
    image_data = None
    if file:
        image_data = await file.read()
    try:
        result = await agent_service.process(message,image_data)
        return {"response":result}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.get("/health")
async def health():
    return {"status":"ok"}