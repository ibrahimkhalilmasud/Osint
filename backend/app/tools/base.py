from abc import ABC, abstractmethod

from ..models import InvestigationInput


class ToolAdapter(ABC):
    name: str

    @abstractmethod
    def run(self, payload: InvestigationInput) -> dict:
        raise NotImplementedError
