from dataclasses import dataclass, field, asdict
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional

from .enums import ArtifactType, LifecycleState


@dataclass
class Artifact:
    """Represents any informational object tracked by the platform."""

    artifact_type: ArtifactType
    source_system: str
    title: str
    artifact_id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    last_modified_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    lifecycle_state: LifecycleState = LifecycleState.ACTIVE

    def to_dict(self) -> dict:
        return {
            "artifact_id": str(self.artifact_id),
            "artifact_type": self.artifact_type.value,
            "source_system": self.source_system,
            "title": self.title,
            "created_at": self.created_at.isoformat(),
            "last_modified_at": self.last_modified_at.isoformat(),
            "lifecycle_state": self.lifecycle_state.value,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Artifact":
        return cls(
            artifact_id=UUID(data["artifact_id"]),
            artifact_type=ArtifactType(data["artifact_type"]),
            source_system=data["source_system"],
            title=data["title"],
            created_at=datetime.fromisoformat(data["created_at"]),
            last_modified_at=datetime.fromisoformat(data["last_modified_at"]),
            lifecycle_state=LifecycleState(data["lifecycle_state"]),
        )
