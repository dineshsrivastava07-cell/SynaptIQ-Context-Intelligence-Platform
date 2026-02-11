from enum import Enum


class EventType(str, Enum):
    CREATE = "create"
    MODIFY = "modify"
    ACCESS = "access"
    REFERENCE = "reference"
    DISCUSS = "discuss"
    APPROVE = "approve"


class ArtifactType(str, Enum):
    DOC = "doc"
    RECORD = "record"
    TICKET = "ticket"
    EMAIL = "email"
    FILE = "file"


class LifecycleState(str, Enum):
    ACTIVE = "active"
    DORMANT = "dormant"
    OBSOLETE = "obsolete"
    SUPERSEDED = "superseded"


class ConceptType(str, Enum):
    PROJECT = "project"
    CUSTOMER = "customer"
    PRODUCT = "product"
    POLICY = "policy"


class ActivityType(str, Enum):
    CREATE = "create"
    EDIT = "edit"
    REVIEW = "review"
    DISCUSS = "discuss"
    APPROVE = "approve"


class DecisionType(str, Enum):
    EXPLICIT = "explicit"
    INFERRED = "inferred"
