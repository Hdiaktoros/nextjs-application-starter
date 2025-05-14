from fastapi import APIRouter, UploadFile, BackgroundTasks, Depends, HTTPException, status
from fastapi.responses import StreamingResponse, FileResponse
from core.tasks import process_epub_task
from auth.jwt_auth import get_current_user
import uuid
import os

router = APIRouter()

# In-memory placeholder for job status - to be replaced with RedisJobStore usage
job_status_store = {}

@router.post("/clean", dependencies=[Depends(get_current_user)])
async def clean_epub(file: UploadFile, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    epub_path = f"/tmp/{job_id}_{file.filename}"
    with open(epub_path, "wb") as f:
        f.write(await file.read())

    # Enqueue background task
    process_epub_task.delay(job_id, epub_path)
    job_status_store[job_id] = "processing"

    return {"job_id": job_id, "status": "processing"}

@router.get("/clean/{job_id}", dependencies=[Depends(get_current_user)])
async def get_job_status(job_id: str):
    status = job_status_store.get(job_id, "unknown")
    return {"job_id": job_id, "status": status}

@router.get("/clean/{job_id}/result", dependencies=[Depends(get_current_user)])
async def get_job_result(job_id: str):
    # Placeholder path - in real implementation, fetch from job store
    result_path = f"/tmp/{job_id}_cleaned.epub"
    if os.path.exists(result_path):
        return FileResponse(result_path, media_type="application/epub+zip", filename=f"{job_id}_cleaned.epub")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Result not found")

@router.get("/clean/{job_id}/stream", dependencies=[Depends(get_current_user)])
async def stream_cleaning_tokens(job_id: str):
    # Pseudocode for streaming tokens from Llama endpoint
    async def token_generator():
        # Simulate streaming tokens
        for i in range(10):
            yield f"data: token_{i}\n\n"
            await asyncio.sleep(0.5)
    return StreamingResponse(token_generator(), media_type="text/event-stream")
