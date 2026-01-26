from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.rag import rag_service
from app.core.config import settings
from pydantic import BaseModel
from typing import List, Optional
import asyncio

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    history: Optional[List[dict]] = []

@router.post("/message")
async def send_message(request: ChatRequest):
    """
    Send a message and get AI-powered response using Cohere RAG.
    Maintains StreamingResponse signature for frontend compatibility.
    """
    
    async def generate():
        try:
            # Call the Cohere RAG service
            # Note: This is currently synchronous (waits for full generation)
            result = await rag_service.generate_response_grounded(
                query=request.query,
                limit=3
            )
            
            answer = result.get("answer", "")
            citations = result.get("sources", [])
            
            # Yield the answer
            yield answer
            
            # Optionally yield citations if the frontend supports a specific format
            # For now, we append them to the text if they exist
            if citations:
                yield "\n\n**Sources:**\n"
                for source in citations:
                    title = source.get('title', 'Unknown')
                    url = source.get('url', '#')
                    yield f"- [{title}]({url})\n"

        except Exception as e:
            yield f"\n\n[Error: {str(e)}]"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@router.get("/health")
async def chat_health():
    """Health check for chat service."""
    return {"status": "healthy", "service": "chat"}
