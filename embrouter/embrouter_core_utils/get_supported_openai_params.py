from typing import Final, Literal

import embrouter
from embrouter.exceptions import BadRequestError
from embrouter.embrouter_core_utils.get_llm_provider_logic import declared_authenticating_provider
from embrouter.types.utils import LlmProviders, LlmProvidersSet


def get_supported_openai_params(
    model: str,
    custom_llm_provider: str | None = None,
    request_type: Literal["chat_completion", "embeddings", "transcription"] = "chat_completion",
    base_model: str | None = None,
) -> list | None:
    """
    Returns the supported openai params for a given model + provider

    Example:
    ```
    get_supported_openai_params(model="anthropic.claude-3", custom_llm_provider="bedrock")
    ```

    Args:
        base_model: An optional capability hint for deployments whose ``model``
            label isn't recognized on its own (e.g. an Azure deployment name, or a
            friendly Bedrock alias). It is additive: the result is the union of the
            params supported by ``model`` and by ``base_model``, so a hint can only
            add capabilities, never strip ones the real model already supports.

    Returns:
    - List if custom_llm_provider is mapped
    - None if unmapped
    """
    if not custom_llm_provider:
        custom_llm_provider = declared_authenticating_provider(model)
    if not custom_llm_provider:
        try:
            custom_llm_provider = embrouter.get_llm_provider(model=model)[1]
        except BadRequestError:
            return None

    if custom_llm_provider in LlmProvidersSet:
        provider_config = embrouter.ProviderConfigManager.get_provider_chat_config(
            model=model,
            provider=LlmProviders(custom_llm_provider),
            base_model=base_model,
        )
    elif custom_llm_provider.split("/")[0] in LlmProvidersSet:
        provider_config = embrouter.ProviderConfigManager.get_provider_chat_config(
            model=model,
            provider=LlmProviders(custom_llm_provider.split("/")[0]),
            base_model=base_model,
        )
    else:
        provider_config = None

    if provider_config and request_type == "chat_completion":
        supported_params = provider_config.get_supported_openai_params(model=model)
        if base_model and base_model != model:
            base_model_params: Final = provider_config.get_supported_openai_params(model=base_model)
            supported_params = list(dict.fromkeys([*supported_params, *base_model_params]))
        return supported_params

    if custom_llm_provider == "bedrock" or custom_llm_provider == "bedrock_converse":
        return embrouter.AmazonConverseConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "meta_llama":
        provider_config = embrouter.ProviderConfigManager.get_provider_chat_config(
            model=model, provider=LlmProviders.LLAMA
        )
        if provider_config:
            return provider_config.get_supported_openai_params(model=model)
    elif custom_llm_provider == "ollama":
        return embrouter.OllamaConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "ollama_chat":
        return embrouter.OllamaChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "anthropic":
        return embrouter.AnthropicConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "anthropic_text":
        return embrouter.AnthropicTextConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "fireworks_ai":
        if request_type == "embeddings":
            return embrouter.FireworksAIEmbeddingConfig().get_supported_openai_params(model=model)
        elif request_type == "transcription":
            return None
        else:
            return embrouter.FireworksAIConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "nvidia_nim":
        if request_type == "chat_completion":
            return embrouter.nvidiaNimConfig.get_supported_openai_params(model=model)
        elif request_type == "embeddings":
            return embrouter.nvidiaNimEmbeddingConfig.get_supported_openai_params()
    elif custom_llm_provider == "cerebras":
        return embrouter.CerebrasConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "nadir":
        return embrouter.NadirConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "baseten":
        return embrouter.BasetenConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "xai":
        return embrouter.XAIChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "ai21_chat" or custom_llm_provider == "ai21":
        return embrouter.AI21ChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "volcengine":
        return embrouter.VolcEngineConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "groq":
        return embrouter.GroqChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "bedrock_mantle":
        return embrouter.BedrockMantleChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "hosted_vllm":
        return embrouter.HostedVLLMChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "vllm":
        return embrouter.VLLMConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "deepseek":
        return embrouter.DeepSeekChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "tencent":
        return embrouter.TencentChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "cohere_chat" or custom_llm_provider == "cohere":
        return embrouter.CohereChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "maritalk":
        return embrouter.MaritalkConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "openai":
        if request_type == "transcription":
            transcription_provider_config = embrouter.ProviderConfigManager.get_provider_audio_transcription_config(
                model=model, provider=LlmProviders.OPENAI
            )
            if isinstance(transcription_provider_config, embrouter.OpenAIGPTAudioTranscriptionConfig):
                return transcription_provider_config.get_supported_openai_params(model=model)
            else:
                raise ValueError(f"Unsupported provider config: {transcription_provider_config} for model: {model}")
        return embrouter.OpenAIConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "sap":
        if request_type == "chat_completion":
            return embrouter.GenAIHubOrchestrationConfig().get_supported_openai_params(model=model)
        elif request_type == "embeddings":
            return embrouter.GenAIHubEmbeddingConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "azure":
        _azure_detection_model: Final = base_model or model
        if embrouter.AzureOpenAIO1Config().is_o_series_model(model=_azure_detection_model):
            return embrouter.AzureOpenAIO1Config().get_supported_openai_params(model=_azure_detection_model)
        elif embrouter.AzureOpenAIGPT5Config.is_model_gpt_5_model(model=_azure_detection_model):
            return embrouter.AzureOpenAIGPT5Config().get_supported_openai_params(model=_azure_detection_model)
        else:
            return embrouter.AzureOpenAIConfig().get_supported_openai_params(model=_azure_detection_model)
    elif custom_llm_provider == "openrouter":
        return embrouter.OpenrouterConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "vercel_ai_gateway":
        return embrouter.VercelAIGatewayConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "mistral" or custom_llm_provider == "codestral":
        # mistal and codestral api have the exact same params
        if request_type == "chat_completion":
            return embrouter.MistralConfig().get_supported_openai_params(model=model)
        elif request_type == "embeddings":
            return embrouter.MistralEmbeddingConfig().get_supported_openai_params()
        elif request_type == "transcription":
            from embrouter.llms.mistral.audio_transcription.transformation import (
                MistralAudioTranscriptionConfig,
            )

            return MistralAudioTranscriptionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "text-completion-codestral":
        return embrouter.CodestralTextCompletionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "sambanova":
        if request_type == "embeddings":
            return embrouter.SambaNovaEmbeddingConfig().get_supported_openai_params(model=model)
        else:
            return embrouter.SambanovaConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "nebius":
        if request_type == "chat_completion":
            return embrouter.NebiusConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "wandb":
        if request_type == "chat_completion":
            return embrouter.WandbConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "replicate":
        return embrouter.ReplicateConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "huggingface":
        return embrouter.HuggingFaceChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "jina_ai":
        if request_type == "embeddings":
            return embrouter.JinaAIEmbeddingConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "together_ai":
        return embrouter.TogetherAIChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "databricks":
        if request_type == "chat_completion":
            return embrouter.DatabricksConfig().get_supported_openai_params(model=model)
        elif request_type == "embeddings":
            return embrouter.DatabricksEmbeddingConfig().get_supported_openai_params()
    elif custom_llm_provider == "palm" or custom_llm_provider == "gemini":
        return embrouter.GoogleAIStudioGeminiConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "novita":
        return embrouter.NovitaConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "vertex_ai" or custom_llm_provider == "vertex_ai_beta":
        if request_type == "chat_completion":
            if model.startswith("mistral"):
                return embrouter.VertexAIMistralConfig().get_supported_openai_params(model=model)
            elif model.startswith("codestral"):
                return embrouter.CodestralTextCompletionConfig().get_supported_openai_params(model=model)
            elif model.startswith("claude"):
                return embrouter.VertexAIAnthropicConfig().get_supported_openai_params(model=model)
            elif model.startswith("gemini"):
                return embrouter.VertexGeminiConfig().get_supported_openai_params(model=model)
            else:
                return embrouter.VertexAILlama3Config().get_supported_openai_params(model=model)
        elif request_type == "embeddings":
            return embrouter.VertexAITextEmbeddingConfig().get_supported_openai_params()
    elif custom_llm_provider == "sagemaker":
        return embrouter.SagemakerConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "aleph_alpha":
        return [
            "max_tokens",
            "stream",
            "top_p",
            "temperature",
            "presence_penalty",
            "frequency_penalty",
            "n",
            "stop",
        ]
    elif custom_llm_provider == "cloudflare":
        return embrouter.CloudflareChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "nlp_cloud":
        return embrouter.NLPCloudConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "petals":
        return embrouter.PetalsConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "deepinfra":
        return embrouter.DeepInfraConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "perplexity":
        return embrouter.PerplexityChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "nscale":
        return embrouter.NscaleConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "anyscale":
        return [
            "temperature",
            "top_p",
            "stream",
            "max_tokens",
            "stop",
            "frequency_penalty",
            "presence_penalty",
        ]
    elif custom_llm_provider == "watsonx":
        return embrouter.IBMWatsonXChatConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "watsonx_text":
        return embrouter.IBMWatsonXAIConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "custom_openai" or custom_llm_provider == "text-completion-openai":
        return embrouter.OpenAITextCompletionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "predibase":
        return embrouter.PredibaseConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "voyage":
        if request_type == "embeddings" and embrouter.VoyageMultimodalEmbeddingConfig.is_multimodal_embeddings(model):
            return embrouter.VoyageMultimodalEmbeddingConfig().get_supported_openai_params(model=model)
        return embrouter.VoyageEmbeddingConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "infinity":
        return embrouter.InfinityEmbeddingConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "triton":
        if request_type == "embeddings":
            return embrouter.TritonEmbeddingConfig().get_supported_openai_params(model=model)
        else:
            return embrouter.TritonConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "deepgram":
        if request_type == "transcription":
            return embrouter.DeepgramAudioTranscriptionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "ovhcloud":
        if request_type == "transcription":
            from embrouter.llms.ovhcloud.audio_transcription.transformation import (
                OVHCloudAudioTranscriptionConfig,
            )

            return OVHCloudAudioTranscriptionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "scaleway":
        if request_type == "transcription":
            from embrouter.llms.scaleway.audio_transcription.transformation import (
                ScalewayAudioTranscriptionConfig,
            )

            return ScalewayAudioTranscriptionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "elevenlabs":
        if request_type == "transcription":
            from embrouter.llms.elevenlabs.audio_transcription.transformation import (
                ElevenLabsAudioTranscriptionConfig,
            )

            return ElevenLabsAudioTranscriptionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider == "soniox":
        if request_type == "transcription":
            return embrouter.SonioxAudioTranscriptionConfig().get_supported_openai_params(model=model)
    elif custom_llm_provider in embrouter._custom_providers:
        if request_type == "chat_completion":
            provider_config = embrouter.ProviderConfigManager.get_provider_chat_config(
                model=model, provider=LlmProviders.CUSTOM
            )
            if provider_config:
                return provider_config.get_supported_openai_params(model=model)
        elif request_type == "embeddings" or request_type == "transcription":
            return None

    return None
