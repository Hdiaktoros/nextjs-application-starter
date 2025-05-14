from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response, APIRouter

REQUEST_COUNT = Counter(
    "fanfic_requests_total", "Total API requests", ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "fanfic_request_latency_seconds", "Request latency in seconds", ["endpoint"]
)

router = APIRouter()

@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
