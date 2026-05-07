from datetime import datetime, timezone
from enum import Enum
import re
from urllib.parse import urlparse

import phonenumbers
from pydantic import BaseModel, EmailStr, Field, field_validator

from .config import settings


class InvestigationStatus(str, Enum):
    queued = "queued"
    running = "running"
    completed = "completed"
    failed = "failed"


class InvestigationInput(BaseModel):
    full_name: str | None = None
    phone_number: str | None = None
    email_address: EmailStr | None = None
    username: str | None = None
    domain: str | None = None
    company_name: str | None = None

    @field_validator("phone_number")
    @classmethod
    def normalize_phone(cls, value: str | None) -> str | None:
        if not value:
            return value
        parsed = phonenumbers.parse(value, settings.default_phone_region)
        if not phonenumbers.is_valid_number(parsed):
            raise ValueError("Invalid phone number")
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

    @field_validator("username")
    @classmethod
    def normalize_username(cls, value: str | None) -> str | None:
        if not value:
            return value
        return re.sub(r"\s+", "", value.strip().lower())

    @field_validator("domain")
    @classmethod
    def normalize_domain(cls, value: str | None) -> str | None:
        if not value:
            return value
        candidate = value.strip().lower()
        if "://" in candidate:
            candidate = urlparse(candidate).netloc
        candidate = candidate.split("/")[0]
        if not re.match(r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$", candidate):
            raise ValueError("Invalid domain")
        return candidate


class InvestigationRecord(BaseModel):
    id: str
    status: InvestigationStatus
    input: InvestigationInput
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ToolRunRequest(BaseModel):
    tool_name: str
    investigation_id: str


class SourceEvidence(BaseModel):
    source: str
    collected_at: datetime
    data: dict


class ReportPayload(BaseModel):
    investigation_id: str
    confidence_score: float
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    grouped_entities: dict[str, list[str]]
    evidence: list[SourceEvidence]
