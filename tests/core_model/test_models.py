import pytest
from uuid import UUID
from datetime import datetime, timezone

from src.core_model.models.enums import (
    EventType, ArtifactType, LifecycleState, ConceptType, ActivityType, DecisionType,
)
from src.core_model.models.event import Event
from src.core_model.models.artifact import Artifact
from src.core_model.models.person import Person
from src.core_model.models.system import System
from src.core_model.models.concept import Concept
from src.core_model.models.activity import Activity
from src.core_model.models.decision import Decision


class TestEvent:
    def test_create_event(self):
        evt = Event(
            event_type=EventType.CREATE,
            source_system="filesystem",
            artifact_id=UUID("12345678-1234-5678-1234-567812345678"),
        )
        assert evt.event_type == EventType.CREATE
        assert isinstance(evt.event_id, UUID)
        assert isinstance(evt.timestamp, datetime)

    def test_event_serialization(self):
        evt = Event(
            event_type=EventType.MODIFY,
            source_system="crm",
            artifact_id=UUID("12345678-1234-5678-1234-567812345678"),
            person_id=UUID("87654321-4321-8765-4321-876543218765"),
            metadata={"field": "status", "old": "open", "new": "closed"},
        )
        data = evt.to_dict()
        assert data["event_type"] == "modify"
        assert data["source_system"] == "crm"
        assert data["metadata"]["field"] == "status"

        restored = Event.from_dict(data)
        assert restored.event_id == evt.event_id
        assert restored.event_type == evt.event_type

    def test_event_types(self):
        for et in EventType:
            evt = Event(event_type=et, source_system="test", artifact_id=UUID(int=0))
            assert evt.event_type == et


class TestArtifact:
    def test_create_artifact(self):
        art = Artifact(
            artifact_type=ArtifactType.DOC,
            source_system="wiki",
            title="Architecture Doc",
        )
        assert art.lifecycle_state == LifecycleState.ACTIVE
        assert isinstance(art.artifact_id, UUID)

    def test_artifact_serialization(self):
        art = Artifact(
            artifact_type=ArtifactType.TICKET,
            source_system="jira",
            title="Bug Fix #123",
        )
        data = art.to_dict()
        restored = Artifact.from_dict(data)
        assert restored.title == "Bug Fix #123"
        assert restored.artifact_type == ArtifactType.TICKET


class TestPerson:
    def test_create_person(self):
        p = Person(name="Dinesh", role="Architect", team="Platform", org_unit="Engineering")
        assert p.name == "Dinesh"
        data = p.to_dict()
        restored = Person.from_dict(data)
        assert restored.person_id == p.person_id


class TestSystem:
    def test_create_system(self):
        s = System(system_type="crm", system_name="Salesforce")
        assert s.system_name == "Salesforce"
        data = s.to_dict()
        restored = System.from_dict(data)
        assert restored.system_id == s.system_id


class TestConcept:
    def test_create_concept(self):
        c = Concept(concept_type=ConceptType.PROJECT, name="SynaptIQ")
        assert c.concept_type == ConceptType.PROJECT
        data = c.to_dict()
        restored = Concept.from_dict(data)
        assert restored.name == "SynaptIQ"


class TestActivity:
    def test_create_activity(self):
        a = Activity(activity_type=ActivityType.REVIEW)
        assert a.activity_type == ActivityType.REVIEW
        data = a.to_dict()
        restored = Activity.from_dict(data)
        assert restored.activity_id == a.activity_id


class TestDecision:
    def test_create_decision(self):
        d = Decision(decision_type=DecisionType.EXPLICIT, rationale="Approved by CTO")
        assert d.rationale == "Approved by CTO"

    def test_inferred_decision(self):
        d = Decision(decision_type=DecisionType.INFERRED)
        assert d.rationale is None
        data = d.to_dict()
        restored = Decision.from_dict(data)
        assert restored.decision_type == DecisionType.INFERRED
