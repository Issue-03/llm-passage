"""
Registry mapping the callback class string to the class type.

This is used to get the class type from the callback class string.

Example:
    "datadog" -> DataDogLogger
    "prometheus" -> PrometheusLogger
"""

from typing import Final

from embrouter import _custom_logger_compatible_callbacks_literal
from embrouter.integrations.agentops import AgentOps
from embrouter.integrations.anthropic_cache_control_hook import AnthropicCacheControlHook
from embrouter.integrations.argilla import ArgillaLogger
from embrouter.integrations.azure_sentinel.azure_sentinel import AzureSentinelLogger
from embrouter.integrations.azure_storage.azure_storage import AzureBlobStorageLogger
from embrouter.integrations.bitbucket import BitBucketPromptManager
from embrouter.integrations.braintrust_logging import BraintrustLogger
from embrouter.integrations.cloudzero.cloudzero import CloudZeroLogger
from embrouter.integrations.datadog.datadog import DataDogLogger
from embrouter.integrations.datadog.datadog_llm_obs import DataDogLLMObsLogger
from embrouter.integrations.datadog.datadog_metrics import DatadogMetricsLogger
from embrouter.integrations.deepeval import DeepEvalLogger
from embrouter.integrations.dotprompt import DotpromptManager
from embrouter.integrations.focus.focus_logger import FocusLogger
from embrouter.integrations.galileo import GalileoObserve
from embrouter.integrations.gcs_bucket.gcs_bucket import GCSBucketLogger
from embrouter.integrations.gcs_pubsub.pub_sub import GcsPubSubLogger
from embrouter.integrations.gitlab import GitLabPromptManager
from embrouter.integrations.humanloop import HumanloopLogger
from embrouter.integrations.lago import LagoLogger
from embrouter.integrations.langfuse.langfuse_prompt_management import (
    LangfusePromptManagement,
)
from embrouter.integrations.langsmith import LangsmithLogger
from embrouter.integrations.embrouter_agent import EmbRouterAgentModelResolver
from embrouter.integrations.literal_ai import LiteralAILogger
from embrouter.integrations.mavvrik_focus.mavvrik_focus_logger import MavvrikFocusLogger
from embrouter.integrations.mlflow import MlflowLogger
from embrouter.integrations.newrelic import NewRelicLogger
from embrouter.integrations.openmeter import OpenMeterLogger
from embrouter.integrations.opentelemetry import OpenTelemetry
from embrouter.integrations.opik.opik import OpikLogger
from embrouter.integrations.pointfive import PointFiveLogger
from embrouter.integrations.posthog import PostHogLogger
from embrouter.integrations.prometheus import PrometheusLogger
from embrouter.integrations.s3_v2 import S3Logger
from embrouter.integrations.sqs import SQSLogger
from embrouter.integrations.vantage.vantage_logger import VantageLogger
from embrouter.integrations.vector_store_integrations.vector_store_pre_call_hook import (
    VectorStorePreCallHook,
)
from embrouter.integrations.zerobus import ZerobusLogger
from embrouter.proxy.hooks.dynamic_rate_limiter import _PROXY_DynamicRateLimitHandler
from embrouter.proxy.hooks.dynamic_rate_limiter_v3 import _PROXY_DynamicRateLimitHandlerV3


class CustomLoggerRegistry:
    """
    Registry mapping the callback class string to the class type.
    """

    CALLBACK_CLASS_STR_TO_CLASS_TYPE = {
        "lago": LagoLogger,
        "openmeter": OpenMeterLogger,
        "braintrust": BraintrustLogger,
        "galileo": GalileoObserve,
        "langsmith": LangsmithLogger,
        "literalai": LiteralAILogger,
        "embrouter_agent": EmbRouterAgentModelResolver,
        "prometheus": PrometheusLogger,
        "datadog": DataDogLogger,
        "datadog_llm_observability": DataDogLLMObsLogger,
        "datadog_metrics": DatadogMetricsLogger,
        "gcs_bucket": GCSBucketLogger,
        "opik": OpikLogger,
        "argilla": ArgillaLogger,
        "opentelemetry": OpenTelemetry,
        "azure_sentinel": AzureSentinelLogger,
        "azure_storage": AzureBlobStorageLogger,
        "humanloop": HumanloopLogger,
        # OTEL compatible loggers
        "logfire": OpenTelemetry,
        "arize": OpenTelemetry,
        "langfuse_otel": OpenTelemetry,
        "arize_phoenix": OpenTelemetry,
        "langtrace": OpenTelemetry,
        "weave_otel": OpenTelemetry,
        "levo": OpenTelemetry,
        "signoz": OpenTelemetry,
        "mlflow": MlflowLogger,
        "langfuse": LangfusePromptManagement,
        "otel": OpenTelemetry,
        "gcs_pubsub": GcsPubSubLogger,
        "anthropic_cache_control_hook": AnthropicCacheControlHook,
        "agentops": AgentOps,
        "deepeval": DeepEvalLogger,
        "s3_v2": S3Logger,
        "pointfive": PointFiveLogger,
        "zerobus": ZerobusLogger,
        "aws_sqs": SQSLogger,
        "dynamic_rate_limiter": _PROXY_DynamicRateLimitHandler,
        "dynamic_rate_limiter_v3": _PROXY_DynamicRateLimitHandlerV3,
        "vector_store_pre_call_hook": VectorStorePreCallHook,
        "dotprompt": DotpromptManager,
        "bitbucket": BitBucketPromptManager,
        "gitlab": GitLabPromptManager,
        "cloudzero": CloudZeroLogger,
        "focus": FocusLogger,
        "mavvrik": MavvrikFocusLogger,
        "vantage": VantageLogger,
        "posthog": PostHogLogger,
        "newrelic": NewRelicLogger,
    }

    from embrouter.integrations.generic_api.generic_api_callback import (
        GenericAPILogger,
    )

    CALLBACK_CLASS_STR_TO_CLASS_TYPE["generic_api"] = GenericAPILogger

    try:
        from embrouter_enterprise.enterprise_callbacks.pagerduty.pagerduty import (
            PagerDutyAlerting,
        )
        from embrouter_enterprise.enterprise_callbacks.send_emails.resend_email import (
            ResendEmailLogger,
        )
        from embrouter_enterprise.enterprise_callbacks.send_emails.sendgrid_email import (
            SendGridEmailLogger,
        )
        from embrouter_enterprise.enterprise_callbacks.send_emails.smtp_email import (
            SMTPEmailLogger,
        )

        enterprise_loggers = {
            "pagerduty": PagerDutyAlerting,
            "resend_email": ResendEmailLogger,
            "sendgrid_email": SendGridEmailLogger,
            "smtp_email": SMTPEmailLogger,
        }
        CALLBACK_CLASS_STR_TO_CLASS_TYPE.update(enterprise_loggers)
    except ImportError:
        pass  # enterprise not installed

    @classmethod
    def get_callback_str_from_class_type(cls, class_type: type) -> str | None:
        """
        Get the callback string from the class type.

        Args:
            class_type: The class type to find the string for

        Returns:
            str: The callback string, or None if not found
        """
        for (
            callback_str,
            callback_class,
        ) in cls.CALLBACK_CLASS_STR_TO_CLASS_TYPE.items():
            if callback_class == class_type:
                return callback_str
        return None

    @classmethod
    def get_all_callback_strs_from_class_type(cls, class_type: type) -> list[str]:
        """
        Get all callback strings that map to the same class type.
        Some class types (like OpenTelemetry) have multiple string mappings.

        Args:
            class_type: The class type to find all strings for

        Returns:
            list: List of callback strings that map to the class type
        """
        callback_strs: Final[list[str]] = []
        for (
            callback_str,
            callback_class,
        ) in cls.CALLBACK_CLASS_STR_TO_CLASS_TYPE.items():
            if callback_class == class_type:
                callback_strs.append(callback_str)
        return callback_strs

    @classmethod
    def get_class_type_for_custom_logger_name(
        cls,
        custom_logger_name: _custom_logger_compatible_callbacks_literal,
    ) -> type:
        """
        Get the class type for a given custom logger name
        """
        return cls.CALLBACK_CLASS_STR_TO_CLASS_TYPE[custom_logger_name]
