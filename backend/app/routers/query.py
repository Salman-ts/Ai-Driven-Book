from fastapi import APIRouter, Request, HTTPException, status
from app.schemas.query import QueryRequest, QueryResponse
from app.services.rag import rag_service
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post("/", response_model=QueryResponse)
@limiter.limit("20/minute") # Rate limit from T003/T014 reqs
async def ask_question(request: Request, body: QueryRequest):
    """
    Ask a grounded question about the book.
    Supports global search or selected-text focus.
    """
    if not body.query.strip():
        raise HTTPException(status_code=422, detail="Query cannot be empty")
        
    try:
        result = await rag_service.generate_response_grounded(
            query=body.query,
            selection_context=body.selection_context,
            selection_only=body.selection_only
        )
        return QueryResponse(**result)
    except Exception as e:
        # Log error here
        print(f"RAG Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate answer")
