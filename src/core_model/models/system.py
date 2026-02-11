from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class System:
    """Represents a source system connected to the platform."""

    system_type: str
    system_name: str
    system_id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict:
        return {
            "system_id": str(self.system_id),
            "system_type": self.system_type,
            "system_name": self.system_name,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "System":
        return cls(
            system_id=UUID(data["system_id"]),
            system_type=data["system_type"],
            system_name=data["system_name"],
        )
