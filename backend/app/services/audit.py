import json
import logging


logger = logging.getLogger("osint.audit")


def write_audit_event(event: str, actor: str, metadata: dict) -> None:
    logger.info(json.dumps({"event": event, "actor": actor, "metadata": metadata}, default=str))
