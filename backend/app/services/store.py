from datetime import datetime, timezone
from uuid import uuid4

from ..models import InvestigationInput, InvestigationRecord, InvestigationStatus


class InvestigationStore:
    def __init__(self) -> None:
        self._records: dict[str, InvestigationRecord] = {}

    def create(self, payload: InvestigationInput) -> InvestigationRecord:
        investigation_id = str(uuid4())
        record = InvestigationRecord(id=investigation_id, status=InvestigationStatus.queued, input=payload)
        self._records[investigation_id] = record
        return record

    def get(self, investigation_id: str) -> InvestigationRecord | None:
        return self._records.get(investigation_id)

    def update_status(self, investigation_id: str, status: InvestigationStatus) -> InvestigationRecord | None:
        record = self._records.get(investigation_id)
        if not record:
            return None
        record.status = status
        record.updated_at = datetime.now(timezone.utc)
        self._records[investigation_id] = record
        return record


investigation_store = InvestigationStore()
