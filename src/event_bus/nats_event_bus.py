import os
import json
import logging
from typing import Callable, Awaitable

import nats
from nats.aio.client import Client as NATSClient

logger = logging.getLogger(__name__)

NATS_URL = os.getenv("NATS_URL", "nats://localhost:4222")


class NATSEventBus:
    """Internal event bus using NATS. Fire-and-forget. No business logic."""

    def __init__(self, url: str = NATS_URL):
        self._url = url
        self._nc: NATSClient | None = None

    async def connect(self) -> None:
        self._nc = await nats.connect(self._url)
        logger.info("Connected to NATS at %s", self._url)

    async def publish(self, topic: str, event_data: dict) -> None:
        if not self._nc:
            raise RuntimeError("Not connected to NATS")
        payload = json.dumps(event_data).encode("utf-8")
        await self._nc.publish(topic, payload)
        logger.debug("Published to %s: %s", topic, event_data.get("event_id", ""))

    async def subscribe(self, topic: str, callback: Callable[[dict], Awaitable[None]]) -> None:
        if not self._nc:
            raise RuntimeError("Not connected to NATS")

        async def _handler(msg):
            data = json.loads(msg.data.decode("utf-8"))
            await callback(data)

        await self._nc.subscribe(topic, cb=_handler)
        logger.info("Subscribed to %s", topic)

    async def close(self) -> None:
        if self._nc:
            await self._nc.close()
            logger.info("NATS connection closed")
