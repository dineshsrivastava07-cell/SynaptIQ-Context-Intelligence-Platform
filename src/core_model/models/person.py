from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Person:
    """Represents a user or employee in the organization."""

    name: str
    role: str
    team: str
    org_unit: str
    person_id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict:
        return {
            "person_id": str(self.person_id),
            "name": self.name,
            "role": self.role,
            "team": self.team,
            "org_unit": self.org_unit,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        return cls(
            person_id=UUID(data["person_id"]),
            name=data["name"],
            role=data["role"],
            team=data["team"],
            org_unit=data["org_unit"],
        )
