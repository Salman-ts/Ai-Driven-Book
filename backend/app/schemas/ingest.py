from pydantic import BaseModel
from typing import Optional

class IngestRequest(BaseModel):
    source_dir: Optional[str] = "docs/"
    force_reindex: bool = False

class JobResponse(BaseModel):
    job_id: int
    status: str
