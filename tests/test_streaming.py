import pytest
from fastapi.testclient import TestClient
from routes.main import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_stream_cleaning_tokens():
    response = client.get("/clean/testjob123/stream", headers={"Authorization": "Bearer your_valid_token"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/event-stream"
    # Further tests can be added to check streaming content
