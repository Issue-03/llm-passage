This makes it easier to pass through requests to the LLM APIs.

E.g. Route to VLLM's `/classify` endpoint:


## SDK (Basic)

```python
import embrouter


response = embrouter.llm_passthrough_route(
    model="hosted_vllm/papluca/xlm-roberta-base-language-detection",
    method="POST",
    endpoint="classify",
    api_base="http://localhost:8090",
    api_key=None,
    json={
        "model": "swapped-for-embrouter-model",
        "input": "Hello, world!",
    }
)

print(response)
```

## SDK (Router)

```python
import asyncio
from embrouter import Router

router = Router(
    model_list=[
        {
            "model_name": "roberta-base-language-detection",
            "embrouter_params": {
                "model": "hosted_vllm/papluca/xlm-roberta-base-language-detection",
                "api_base": "http://localhost:8090", 
            }
        }
    ]
)

request_data = {
    "model": "roberta-base-language-detection",
    "method": "POST",
    "endpoint": "classify",
    "api_base": "http://localhost:8090",
    "api_key": None,
    "json": {
        "model": "roberta-base-language-detection",
        "input": "Hello, world!",
    }
}

async def main():
    response = await router.allm_passthrough_route(**request_data)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

## PROXY 

1. Setup config.yaml 

```yaml
model_list:
  - model_name: roberta-base-language-detection
    embrouter_params:
      model: hosted_vllm/papluca/xlm-roberta-base-language-detection
      api_base: http://localhost:8090
```

2. Run the proxy

```bash
embrouter proxy --config config.yaml

# RUNNING on http://localhost:4000
```

3. Use the proxy

```bash
curl -X POST http://localhost:4000/vllm/classify \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your-api-key>" \
-d '{"model": "roberta-base-language-detection", "input": "Hello, world!"}' \
```

# How to add a provider for passthrough

See VLLMModelInfo for an example.

1. Inherit from BaseModelInfo

```python
from embrouter.llms.base_llm.base_utils import BaseLLMModelInfo

class VLLMModelInfo(BaseLLMModelInfo):
    pass
```

2. Register the provider in the ProviderConfigManager.get_provider_model_info

```python
from embrouter.utils import ProviderConfigManager
from embrouter.types.utils import LlmProviders

provider_config = ProviderConfigManager.get_provider_model_info(
    model="my-test-model", provider=LlmProviders.VLLM
)

print(provider_config)
```