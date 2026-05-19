from fastapi import APIRouter, HTTPException,UploadFile,File,Form,Header
from pydantic import BaseModel
from app.services.agent import agent_service
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

router = APIRouter()

@router.post("/chat")
async def chat(message: str = Form(...), file: UploadFile = File(None),x_api_key:str = Header(None, alias="X-API-Key")):
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    image_data = None
    if file:
        image_data = await file.read()
    try:
        result = await agent_service.process(message,image_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.get("/health")
async def health():
    return {"status":"ok"}