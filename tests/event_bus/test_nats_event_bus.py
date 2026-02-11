import pytest
import json
from unittest.mock import AsyncMock, MagicMock, patch

from src.event_bus.nats_event_bus import NATSEventBus
from src.event_bus.topics import Topics


class TestTopics:
    def test_topic_names(self):
        assert Topics.RAW_EVENTS == "raw.events"
        assert Topics.SIGNALS_EXTRACTED == "signals.extracted"
        assert Topics.CONTEXT_UPDATES == "context.updates"
        assert Topics.CONFIDENCE_UPDATES == "confidence.updates"


class TestNATSEventBus:
    @pytest.mark.asyncio
    async def test_publish_without_connect_raises(self):
        bus = NATSEventBus()
        with pytest.raises(RuntimeError, match="Not connected"):
            await bus.publish(Topics.RAW_EVENTS, {"test": True})

    @pytest.mark.asyncio
    async def test_subscribe_without_connect_raises(self):
        bus = NATSEventBus()
        with pytest.raises(RuntimeError, match="Not connected"):
            await bus.subscribe(Topics.RAW_EVENTS, AsyncMock())

    @pytest.mark.asyncio
    async def test_publish_serializes_json(self):
        bus = NATSEventBus()
        mock_nc = AsyncMock()
        bus._nc = mock_nc

        event_data = {"event_id": "test-123", "event_type": "create"}
        await bus.publish(Topics.RAW_EVENTS, event_data)

        mock_nc.publish.assert_called_once()
        call_args = mock_nc.publish.call_args
        assert call_args[0][0] == "raw.events"
        assert json.loads(call_args[0][1].decode("utf-8")) == event_data

    @pytest.mark.asyncio
    async def test_close_when_connected(self):
        bus = NATSEventBus()
        mock_nc = AsyncMock()
        bus._nc = mock_nc

        await bus.close()
        mock_nc.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_close_when_not_connected(self):
        bus = NATSEventBus()
        await bus.close()  # Should not raise
