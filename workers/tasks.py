from celery.utils.log import get_task_logger

from celery_app import celery_app
from app.services.orchestrator import orchestrator
from app.services.store import investigation_store


logger = get_task_logger(__name__)


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def run_investigation(self, investigation_id: str) -> dict:
    record = investigation_store.get(investigation_id)
    if not record:
        raise ValueError("Investigation not found")
    results = orchestrator.run_all(record.input)
    logger.info("investigation_processed", extra={"investigation_id": investigation_id, "result_count": len(results)})
    return {"investigation_id": investigation_id, "result_count": len(results)}
