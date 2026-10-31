# embrouter/proxy/guardrails/guardrail_initializers.py
from typing import Any, Final

import embrouter
from embrouter.integrations.custom_guardrail import CustomGuardrail
from embrouter.proxy._types import CommonProxyErrors
from embrouter.types.guardrails import *


def initialize_bedrock(embrouter_params: EmbrouterParams, guardrail: Guardrail):
    from embrouter.proxy.guardrails.guardrail_hooks.bedrock_guardrails import (
        BedrockGuardrail,
    )

    streaming_params: Final = BedrockGuardrailStreamingParams.from_extras(embrouter_params.model_extra)
    _bedrock_callback: Final = BedrockGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        guardrailIdentifier=embrouter_params.guardrailIdentifier,
        guardrailVersion=embrouter_params.guardrailVersion,
        checks=embrouter_params.checks,
        content_filter_threshold=embrouter_params.content_filter_threshold,
        prompt_attack_threshold=embrouter_params.prompt_attack_threshold,
        pii_confidence_threshold=embrouter_params.pii_confidence_threshold,
        chunk_budget_chars=embrouter_params.chunk_budget_chars,
        contextual_grounding_from_messages=embrouter_params.contextual_grounding_from_messages,
        default_on=embrouter_params.default_on,
        disable_exception_on_block=embrouter_params.disable_exception_on_block,
        mask_request_content=embrouter_params.mask_request_content,
        mask_response_content=embrouter_params.mask_response_content,
        aws_region_name=embrouter_params.aws_region_name,
        aws_access_key_id=embrouter_params.aws_access_key_id,
        aws_secret_access_key=embrouter_params.aws_secret_access_key,
        aws_session_token=embrouter_params.aws_session_token,
        aws_session_name=embrouter_params.aws_session_name,
        aws_profile_name=embrouter_params.aws_profile_name,
        aws_role_name=embrouter_params.aws_role_name,
        aws_web_identity_token=embrouter_params.aws_web_identity_token,
        aws_sts_endpoint=embrouter_params.aws_sts_endpoint,
        aws_external_id=embrouter_params.aws_external_id,
        aws_bedrock_runtime_endpoint=embrouter_params.aws_bedrock_runtime_endpoint,
        experimental_use_latest_role_message_only=embrouter_params.experimental_use_latest_role_message_only,
        only_scan_new_messages=embrouter_params.only_scan_new_messages or False,
        streaming_buffer_until_moderated=streaming_params.streaming_buffer_until_moderated,
        streaming_sampling_rate=streaming_params.streaming_sampling_rate,
        streaming_end_of_stream_only=streaming_params.streaming_end_of_stream_only,
        streaming_buffer_release_on_scan=streaming_params.streaming_buffer_release_on_scan,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_bedrock_callback)
    return _bedrock_callback


def initialize_lakera(embrouter_params: EmbrouterParams, guardrail: Guardrail):
    from embrouter.proxy.guardrails.guardrail_hooks.lakera_ai import lakeraAI_Moderation

    _lakera_callback: Final = lakeraAI_Moderation(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        category_thresholds=embrouter_params.category_thresholds,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_lakera_callback)
    return _lakera_callback


def initialize_lakera_v2(embrouter_params: EmbrouterParams, guardrail: Guardrail):
    from embrouter.proxy.guardrails.guardrail_hooks.lakera_ai_v2 import LakeraAIGuardrail

    _lakera_v2_callback: Final = LakeraAIGuardrail(
        api_base=embrouter_params.api_base,
        api_key=embrouter_params.api_key,
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
        project_id=embrouter_params.project_id,
        payload=embrouter_params.payload,
        breakdown=embrouter_params.breakdown,
        metadata=embrouter_params.metadata,
        dev_info=embrouter_params.dev_info,
        on_flagged=embrouter_params.on_flagged,
        skip_system_message_in_guardrail=embrouter_params.skip_system_message_in_guardrail,
        skip_tool_message_in_guardrail=embrouter_params.skip_tool_message_in_guardrail,
        advisory_system_message=embrouter_params.advisory_system_message,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_lakera_v2_callback)
    return _lakera_v2_callback


_MCP_EVENT_HOOKS: Final = frozenset(
    {
        GuardrailEventHooks.pre_mcp_call.value,
        GuardrailEventHooks.during_mcp_call.value,
        GuardrailEventHooks.post_mcp_call.value,
    }
)


def _configured_event_hooks(mode: str | list[str] | Mode) -> tuple[str, ...]:
    if isinstance(mode, str):
        return (mode,)
    if isinstance(mode, list):
        return tuple(mode)
    return tuple(
        hook
        for value in (*mode.tags.values(), mode.default)
        if value is not None
        for hook in ((value,) if isinstance(value, str) else value)
    )


def _is_mcp_only_mode(mode: str | list[str] | Mode) -> bool:
    hooks: Final = _configured_event_hooks(mode)
    return bool(hooks) and all(hook in _MCP_EVENT_HOOKS for hook in hooks)


def _presidio_output_mode(mode: str | list[str] | Mode, *, include_mcp: bool) -> str | list[str] | Mode:
    def output_hooks(hooks: str | list[str]) -> list[str]:
        if not hooks or (not include_mcp and _is_mcp_only_mode(hooks)):
            return []
        return [GuardrailEventHooks.post_call.value]

    if isinstance(mode, Mode):
        return Mode(
            tags={tag: output_hooks(hooks) for tag, hooks in mode.tags.items()},
            default=output_hooks(mode.default) if mode.default is not None else None,
        )
    return output_hooks(mode)


def initialize_presidio(embrouter_params: EmbrouterParams, guardrail: Guardrail) -> tuple[CustomGuardrail, ...]:
    from embrouter.proxy.guardrails.guardrail_hooks.presidio import (
        _OPTIONAL_PresidioPIIMasking,
    )

    explicit_filter_scope: Final = embrouter_params.presidio_filter_scope
    filter_scope: Final = explicit_filter_scope or ("input" if _is_mcp_only_mode(embrouter_params.mode) else "both")
    run_input: Final = filter_scope in ("input", "both")
    run_output: Final = filter_scope in ("output", "both")

    def _make_presidio_callback(**overrides) -> CustomGuardrail:
        params: Final = dict(
            guardrail_name=guardrail.get("guardrail_name", ""),
            event_hook=embrouter_params.mode,
            output_parse_pii=embrouter_params.output_parse_pii,
            presidio_ad_hoc_recognizers=embrouter_params.presidio_ad_hoc_recognizers,
            mock_redacted_text=embrouter_params.mock_redacted_text,
            default_on=embrouter_params.default_on,
            pii_entities_config=embrouter_params.pii_entities_config,
            presidio_score_thresholds=embrouter_params.presidio_score_thresholds,
            presidio_analyzer_api_base=embrouter_params.presidio_analyzer_api_base,
            presidio_anonymizer_api_base=embrouter_params.presidio_anonymizer_api_base,
            presidio_language=embrouter_params.presidio_language,
            presidio_entities_deny_list=embrouter_params.presidio_entities_deny_list,
            apply_to_output=False,
            _callback_role="scan",
        )
        params.update(overrides)
        # Passed outside the heterogeneous params dict so the argument keeps
        # its precise int | None type.
        callback: Final = _OPTIONAL_PresidioPIIMasking(
            presidio_analyze_chunk_size_bytes=embrouter_params.presidio_analyze_chunk_size_bytes,
            **params,
        )
        embrouter.logging_callback_manager.add_embrouter_callback(callback)
        return callback

    input_callback: Final = _make_presidio_callback() if run_input else None
    unmask_output_callback: Final = (
        _make_presidio_callback(
            output_parse_pii=True,
            event_hook=_presidio_output_mode(embrouter_params.mode, include_mcp=True),
            _callback_role="restore",
        )
        if run_input and embrouter_params.output_parse_pii
        else None
    )
    mask_output_callback: Final = (
        _make_presidio_callback(
            apply_to_output=True,
            event_hook=_presidio_output_mode(embrouter_params.mode, include_mcp=explicit_filter_scope is not None),
            output_parse_pii=False,
            mask_response_content=True,
        )
        if run_output
        else None
    )
    return tuple(
        callback for callback in (input_callback, unmask_output_callback, mask_output_callback) if callback is not None
    )


def initialize_hide_secrets(embrouter_params: EmbrouterParams, guardrail: Guardrail):
    try:
        from embrouter_enterprise.enterprise_callbacks.secret_detection import (
            _ENTERPRISE_SecretDetection,
        )
    except ImportError:
        raise Exception("Trying to use Secret Detection" + CommonProxyErrors.missing_enterprise_package.value)

    _secret_detection_object: Final = _ENTERPRISE_SecretDetection(
        detect_secrets_config=embrouter_params.detect_secrets_config,
        event_hook=embrouter_params.mode,
        guardrail_name=guardrail.get("guardrail_name", ""),
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_secret_detection_object)
    return _secret_detection_object


def initialize_tool_permission(embrouter_params: EmbrouterParams, guardrail: Guardrail):
    from embrouter.proxy.guardrails.guardrail_hooks.tool_permission import (
        ToolPermissionGuardrail,
    )

    rules: list[dict[str, Any]] | None = None
    if embrouter_params.rules:
        rules = []
        for rule in embrouter_params.rules:
            if hasattr(rule, "model_dump"):
                rules.append(rule.model_dump())
            else:
                rules.append(dict(rule))

    _tool_permission_callback: Final = ToolPermissionGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        event_hook=embrouter_params.mode,
        rules=rules,
        default_action=getattr(embrouter_params, "default_action", "deny"),
        on_disallowed_action=getattr(embrouter_params, "on_disallowed_action", "block"),
        default_on=embrouter_params.default_on,
        violation_message_template=embrouter_params.violation_message_template,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_tool_permission_callback)
    return _tool_permission_callback


def initialize_lasso(
    embrouter_params: EmbrouterParams,
    guardrail: Guardrail,
):
    from embrouter.proxy.guardrails.guardrail_hooks.lasso import LassoGuardrail

    _lasso_callback: Final = LassoGuardrail(
        guardrail_name=guardrail.get("guardrail_name", ""),
        lasso_api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base,
        user_id=embrouter_params.lasso_user_id,
        conversation_id=embrouter_params.lasso_conversation_id,
        mask=embrouter_params.mask,
        event_hook=embrouter_params.mode,
        default_on=embrouter_params.default_on,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_lasso_callback)

    return _lasso_callback


def initialize_panw_prisma_airs(embrouter_params, guardrail):
    from embrouter.proxy.guardrails.guardrail_hooks.panw_prisma_airs import (
        PanwPrismaAirsHandler,
    )

    if not embrouter_params.api_key:
        raise ValueError("PANW Prisma AIRS: api_key is required")
    if not embrouter_params.profile_name:
        raise ValueError("PANW Prisma AIRS: profile_name is required")

    _panw_callback: Final = PanwPrismaAirsHandler(
        guardrail_name=guardrail.get("guardrail_name", "panw_prisma_airs"),  # Use .get() with default
        api_key=embrouter_params.api_key,
        api_base=embrouter_params.api_base or "https://service.api.aisecurity.paloaltonetworks.com/v1/scan/sync/request",
        profile_name=embrouter_params.profile_name,
        default_on=embrouter_params.default_on,
        mask_on_block=getattr(embrouter_params, "mask_on_block", False),
        mask_request_content=getattr(embrouter_params, "mask_request_content", False),
        mask_response_content=getattr(embrouter_params, "mask_response_content", False),
        app_name=getattr(embrouter_params, "app_name", None),
        fallback_on_error=getattr(embrouter_params, "fallback_on_error", "block"),
        # `timeout` is now declared on BaseEmbrouterParams (Optional[float] = None),
        # so the attribute always exists. The Pydantic validator on EmbrouterParams
        # coerces strings to float, but None still means "use handler default" —
        # guard against float(None) here.
        timeout=(
            float(getattr(embrouter_params, "timeout", None))
            if getattr(embrouter_params, "timeout", None) is not None
            else 10.0
        ),
        violation_message_template=embrouter_params.violation_message_template,
    )
    embrouter.logging_callback_manager.add_embrouter_callback(_panw_callback)

    return _panw_callback
