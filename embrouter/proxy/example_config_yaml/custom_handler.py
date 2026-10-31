from typing import Final

import embrouter
from embrouter import CustomLLM
from embrouter.types.utils import ModelResponse


class MyCustomLLM(CustomLLM):
    def completion(self, *args, **kwargs) -> ModelResponse:
        return embrouter.completion(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello world"}],
            mock_response="Hi!",
        )

    async def acompletion(self, *args, **kwargs) -> embrouter.ModelResponse:
        return embrouter.completion(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello world"}],
            mock_response="Hi!",
        )


my_custom_llm: Final = MyCustomLLM()
