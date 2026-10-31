from embrouter.llms.openai.image_edit.transformation import OpenAIImageEditConfig
from embrouter.secret_managers.main import get_secret_str


class EmbRouterProxyImageEditConfig(OpenAIImageEditConfig):
    """Configuration for image edit requests routed through EmbRouter Proxy."""

    def validate_environment(
        self,
        headers: dict,
        model: str,
        api_key: str | None = None,
        embrouter_params: dict | None = None,
        api_base: str | None = None,
    ) -> dict:
        api_key = api_key or get_secret_str("EMBROUTER_PROXY_API_KEY")
        headers.update({"Authorization": f"Bearer {api_key}"})
        return headers

    def get_complete_url(self, model: str, api_base: str | None, embrouter_params: dict) -> str:
        api_base = api_base or get_secret_str("EMBROUTER_PROXY_API_BASE")
        if api_base is None:
            raise ValueError("api_base not set for EmbRouter Proxy route. Set in env via `EMBROUTER_PROXY_API_BASE`")
        api_base = api_base.rstrip("/")
        return f"{api_base}/images/edits"
