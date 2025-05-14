from celery import Celery
from core.processor import FanficProcessor

celery_app = Celery(
    "fanfic_tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task(bind=True)
def process_epub_task(self, job_id: str, epub_path: str):
    processor = FanficProcessor()
    result_path = processor.process(epub_path)
    # Here you would update job status in Redis or another durable store
    return result_path
