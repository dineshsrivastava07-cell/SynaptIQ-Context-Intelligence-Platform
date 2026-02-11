from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .enums import ConceptType


@dataclass
class Concept:
    """Represents abstract organizational concepts (project, customer, product, policy)."""

    concept_type: ConceptType
    name: str
    concept_id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict:
        return {
            "concept_id": str(self.concept_id),
            "concept_type": self.concept_type.value,
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Concept":
        return cls(
            concept_id=UUID(data["concept_id"]),
            concept_type=ConceptType(data["concept_type"]),
            name=data["name"],
        )
