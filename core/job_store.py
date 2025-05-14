import asyncio
import aioredis
import json
from typing import Optional

class RedisJobStore:
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url)
        self.job_prefix = "fanfic:job:"

    async def save_job(self, job_id: str, job_data: dict):
        key = f"{self.job_prefix}{job_id}"
        await self.redis.set(key, json.dumps(job_data))

    async def get_job(self, job_id: str) -> Optional[dict]:
        key = f"{self.job_prefix}{job_id}"
        data = await self.redis.get(key)
        if data:
            return json.loads(data)
        return None

    async def delete_job(self, job_id: str):
        key = f"{self.job_prefix}{job_id}"
        await self.redis.delete(key)
