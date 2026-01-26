from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
from app.services.auth import verify_admin
from app.services.ingestion import ingestion_service
from app.schemas.ingest import JobResponse
import random # Mock ID for MVP

router = APIRouter()

@router.post("/reindex", response_model=JobResponse, status_code=status.HTTP_202_ACCEPTED)
async def force_reindex(
    background_tasks: BackgroundTasks,
    admin: dict = Depends(verify_admin)
):
    """
    Trigger a full re-index of the content.
    Only accessible by admins.
    """
    job_id = random.randint(1000, 9999) # Replace with DB insert in real app

    # Assuming a default source_dir or from config
    background_tasks.add_task(
        ingestion_service.ingest_content, 
        source_dir="docs/", # Default source dir for reindex
        force_reindex=True
    )
    
    return JobResponse(job_id=job_id, status="pending")
