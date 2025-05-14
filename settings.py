import os

WORK_DIR = os.getenv("WORK_DIR", "/app/workdir")
DEVICE = os.getenv("DEVICE", "cpu")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret")
LLAMA_ENDPOINT = os.getenv("LLAMA_ENDPOINT", "http://llama:8000")
