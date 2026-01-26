from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.routers import chat, users, content, auth_router, ingest, query, admin
from app.services.rag import rag_service
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init Qdrant
    rag_service.init_collection()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"], # Docusaurus defaults
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(content.router, prefix="/content", tags=["content"])
app.include_router(auth_router.router)
app.include_router(ingest.router, prefix="/ingest", tags=["ingestion"])
app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Book Backend"}
