from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import json

from tenacity import retry, stop_after_attempt, wait_fixed

from ..models import InvestigationInput, ReportPayload, SourceEvidence
from ..tools.adapters import default_tool_registry


class Orchestrator:
    def __init__(self) -> None:
        self.tool_registry = default_tool_registry()

    @retry(stop=stop_after_attempt(2), wait=wait_fixed(1))
    def run_tool(self, tool_name: str, payload: InvestigationInput) -> dict:
        adapter = self.tool_registry.get(tool_name)
        if not adapter:
            raise ValueError(f"Unknown tool: {tool_name}")
        return adapter.run(payload)

    def run_all(self, payload: InvestigationInput) -> list[dict]:
        return [adapter.run(payload) for adapter in self.tool_registry.values()]

    def correlate(self, results: list[dict]) -> dict[str, list[str]]:
        grouped = defaultdict(list)
        for item in results:
            category = item.get("category", "unknown")
            grouped[category].append(item.get("tool", "unknown"))
        return dict(grouped)

    def build_report(self, investigation_id: str, results: list[dict]) -> ReportPayload:
        evidence = [
            SourceEvidence(source=item["tool"], collected_at=datetime.now(timezone.utc), data=item)
            for item in results
        ]
        grouped = self.correlate(results)
        confidence = round(min(0.99, 0.3 + (len(results) * 0.02)), 2)
        report = ReportPayload(
            investigation_id=investigation_id,
            confidence_score=confidence,
            grouped_entities=grouped,
            evidence=evidence,
        )
        reports_dir = Path("reports/generated")
        reports_dir.mkdir(parents=True, exist_ok=True)
        json_path = reports_dir / f"{investigation_id}.json"
        json_path.write_text(json.dumps(report.model_dump(mode="json"), indent=2), encoding="utf-8")
        return report


orchestrator = Orchestrator()
