from datetime import datetime, timezone

from .base import ToolAdapter
from ..models import InvestigationInput


class StubToolAdapter(ToolAdapter):
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def run(self, payload: InvestigationInput) -> dict:
        return {
            "tool": self.name,
            "category": self.category,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "result": "adapter configured",
            "input": payload.model_dump(mode="json", exclude_none=True),
        }


def default_tool_registry() -> dict[str, ToolAdapter]:
    pairs = {
        "holehe": "email",
        "maigret": "username_email",
        "emailrep": "email",
        "h8mail": "email",
        "sherlock": "username",
        "socialscan": "username",
        "whatsmyname": "username",
        "amass": "domain",
        "subfinder": "domain",
        "theHarvester": "domain",
        "dnsx": "domain",
        "spiderfoot": "general",
        "recon-ng": "general",
        "numverify": "phone",
        "hibp": "breach",
        "exiftool": "metadata",
    }
    return {name: StubToolAdapter(name=name, category=category) for name, category in pairs.items()}
