from pydantic import BaseModel
from typing import Optional, List, Literal

class Source(BaseModel):
    title: str
    url: str
    score: float
    snippet: Optional[str] = None

class Provenance(BaseModel):
    mode: Literal["global", "selection"]
    latency_ms: Optional[float] = None

class QueryRequest(BaseModel):
    query: str
    selection_context: Optional[str] = None
    selection_only: bool = False

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    provenance: Provenance
