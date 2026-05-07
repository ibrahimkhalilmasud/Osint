from fastapi import APIRouter, Depends, HTTPException

from ..models import InvestigationInput, ToolRunRequest
from ..security import User, require_roles
from ..services.audit import write_audit_event
from ..services.orchestrator import orchestrator
from ..services.reports import persist_report_artifacts
from ..services.store import investigation_store


router = APIRouter(tags=["investigations"])


@router.post("/investigation")
def create_investigation(
    payload: InvestigationInput,
    user: User = Depends(require_roles("analyst", "admin")),
):
    record = investigation_store.create(payload)
    write_audit_event("investigation_created", user.username, {"investigation_id": record.id})
    return record


@router.get("/results/{investigation_id}")
def get_results(
    investigation_id: str,
    user: User = Depends(require_roles("analyst", "admin", "viewer")),
):
    record = investigation_store.get(investigation_id)
    if not record:
        raise HTTPException(status_code=404, detail="Investigation not found")
    return {"investigation": record}


@router.post("/tools/run")
def run_tool(
    payload: ToolRunRequest,
    user: User = Depends(require_roles("analyst", "admin")),
):
    record = investigation_store.get(payload.investigation_id)
    if not record:
        raise HTTPException(status_code=404, detail="Investigation not found")
    result = orchestrator.run_tool(payload.tool_name, record.input)
    write_audit_event("tool_run", user.username, {"tool": payload.tool_name, "investigation_id": payload.investigation_id})
    return result


@router.get("/reports/{investigation_id}")
def get_report(
    investigation_id: str,
    user: User = Depends(require_roles("analyst", "admin", "viewer")),
):
    record = investigation_store.get(investigation_id)
    if not record:
        raise HTTPException(status_code=404, detail="Investigation not found")
    results = orchestrator.run_all(record.input)
    report = orchestrator.build_report(investigation_id, results)
    artifacts = persist_report_artifacts(report)
    write_audit_event("report_generated", user.username, {"investigation_id": investigation_id})
    return {"report": report, "artifacts": artifacts}
