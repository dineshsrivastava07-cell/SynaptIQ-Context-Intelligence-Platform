from dataclasses import dataclass, field, asdict
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional

from .enums import EventType


@dataclass
class Event:
    """Universal event model for the Context Intelligence Platform.
    Append-only. All events are immutable once created."""

    event_type: EventType
    source_system: str
    artifact_id: UUID
    event_id: UUID = field(default_factory=uuid4)
    person_id: Optional[UUID] = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Optional[dict] = None

    def to_dict(self) -> dict:
        data = asdict(self)
        data["event_id"] = str(self.event_id)
        data["artifact_id"] = str(self.artifact_id)
        data["person_id"] = str(self.person_id) if self.person_id else None
        data["timestamp"] = self.timestamp.isoformat()
        data["event_type"] = self.event_type.value
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Event":
        return cls(
            event_id=UUID(data["event_id"]),
            event_type=EventType(data["event_type"]),
            source_system=data["source_system"],
            artifact_id=UUID(data["artifact_id"]),
            person_id=UUID(data["person_id"]) if data.get("person_id") else None,
            timestamp=datetime.fromisoformat(data["timestamp"]),
            metadata=data.get("metadata"),
        )
