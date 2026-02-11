class Topics:
    """Event bus topic definitions. No business logic — just routing."""

    RAW_EVENTS = "raw.events"
    SIGNALS_EXTRACTED = "signals.extracted"
    CONTEXT_UPDATES = "context.updates"
    CONFIDENCE_UPDATES = "confidence.updates"
