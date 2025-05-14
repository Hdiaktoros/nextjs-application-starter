import pytest
from fastapi.testclient import TestClient
from monitoring.prometheus import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
    assert "fanfic_requests_total" in response.text
