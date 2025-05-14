import pytest
import asyncio
from core.job_store import RedisJobStore

@pytest.mark.asyncio
async def test_save_and_get_job():
    store = RedisJobStore("redis://localhost:6379/0")
    job_id = "testjob123"
    job_data = {"status": "processing"}
    await store.save_job(job_id, job_data)
    retrieved = await store.get_job(job_id)
    assert retrieved == job_data
    await store.delete_job(job_id)
    deleted = await store.get_job(job_id)
    assert deleted is None
