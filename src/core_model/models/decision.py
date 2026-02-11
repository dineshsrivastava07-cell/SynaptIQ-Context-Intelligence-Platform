from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional

from .enums import DecisionType


@dataclass
class Decision:
    """Represents a recorded decision (explicit or inferred)."""

    decision_type: DecisionType
    decision_id: UUID = field(default_factory=uuid4)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    rationale: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "decision_id": str(self.decision_id),
            "decision_type": self.decision_type.value,
            "timestamp": self.timestamp.isoformat(),
            "rationale": self.rationale,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Decision":
        return cls(
            decision_id=UUID(data["decision_id"]),
            decision_type=DecisionType(data["decision_type"]),
            timestamp=datetime.fromisoformat(data["timestamp"]),
            rationale=data.get("rationale"),
        )
