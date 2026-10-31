"""
Type definitions for the EmbRouter Policy Engine.

This module re-exports types from embrouter.types.proxy.policy_engine for backward compatibility.
The canonical location for these types is embrouter/types/proxy/policy_engine/.
"""

# Re-export all types from the new location
from embrouter.types.proxy.policy_engine import (  # Policy types; Validation types; Resolver types
    Policy,
    PolicyConfig,
    PolicyGuardrails,
    PolicyMatchContext,
    PolicyScope,
    PolicyValidateRequest,
    PolicyValidationError,
    PolicyValidationErrorType,
    PolicyValidationResponse,
    ResolvedPolicy,
)

__all__ = [
    # Policy types
    "Policy",
    "PolicyConfig",
    "PolicyGuardrails",
    # Resolver types
    "PolicyMatchContext",
    "PolicyScope",
    # Validation types
    "PolicyValidateRequest",
    "PolicyValidationError",
    "PolicyValidationErrorType",
    "PolicyValidationResponse",
    "ResolvedPolicy",
]
