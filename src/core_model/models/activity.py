from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime, timezone

from .enums import ActivityType


@dataclass
class Activity:
    """Represents a tracked action in the system."""

    activity_type: ActivityType
    activity_id: UUID = field(default_factory=uuid4)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return {
            "activity_id": str(self.activity_id),
            "activity_type": self.activity_type.value,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Activity":
        return cls(
            activity_id=UUID(data["activity_id"]),
            activity_type=ActivityType(data["activity_type"]),
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )
