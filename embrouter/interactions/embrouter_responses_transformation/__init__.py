"""
Bridge module for connecting Interactions API to Responses API via embrouter.responses().
"""

from embrouter.interactions.embrouter_responses_transformation.handler import (
    EmbRouterResponsesInteractionsHandler,
)
from embrouter.interactions.embrouter_responses_transformation.transformation import (
    EmbRouterResponsesInteractionsConfig,
)

__all__ = [
    "EmbRouterResponsesInteractionsConfig",  # Transformation config class (not BaseInteractionsAPIConfig)
    "EmbRouterResponsesInteractionsHandler",
]
