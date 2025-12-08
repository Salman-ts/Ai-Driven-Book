from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.services.rag import rag_service
from app.services.auth import get_current_user
from app.core.config import settings
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    history: Optional[List[dict]] = []

@router.post("/message")
async def send_message(
    request: ChatRequest,
    user: dict = Depends(get_current_user)
):
    # 1. Search for context
    # user_profile = ... # Fetch from DB if needed for context
    
    search_results = await rag_service.search(request.query, limit=3)
    
    context_text = "\n\n".join([
        f"Source: {res.payload.get('chapter', 'Unknown')}\nContent: {res.payload.get('content', '')}"
        for res in search_results
    ])
    
    system_prompt = f"""You are an AI assistant for an educational book. 
    Answer the user's question based strictly on the provided context.
    If the answer is not in the context, say you don't know.
    
    Context:
    {context_text}
    """
    
    messages = [{"role": "system", "content": system_prompt}] + request.history + [{"role": "user", "content": request.query}]
    
    async def generate():
        stream = await rag_service.openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    return StreamingResponse(generate(), media_type="text/event-stream")
