from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
from app.services.auth import verify_admin
from app.services.ingestion import ingestion_service
from app.schemas.ingest import IngestRequest, JobResponse
import random # Mock ID for MVP

router = APIRouter()

@router.post("/", response_model=JobResponse, status_code=status.HTTP_202_ACCEPTED)
async def trigger_ingestion(
    request: IngestRequest,
    background_tasks: BackgroundTasks,
    admin: dict = Depends(verify_admin)
):
    """
    Trigger content ingestion in background.
    Only accessible by admins.
    """
    job_id = random.randint(1000, 9999) # Replace with DB insert in real app
    
    background_tasks.add_task(
        ingestion_service.ingest_content, 
        source_dir=request.source_dir, 
        force_reindex=request.force_reindex
    )
    
    return JobResponse(job_id=job_id, status="pending")
