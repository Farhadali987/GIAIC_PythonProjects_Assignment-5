from openai import AsyncOpenAI
from app.core.config import settings
from app.ai.llm.base import BaseLLMProvider
from typing import List, Dict

class QwenProvider(BaseLLMProvider):
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.QWEN_API_KEY, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

    async def chat_completion(self, messages: List[Dict[str, str]], **kwargs) -> str:
        response = await self.client.chat.completions.create(
            model="qwen-turbo",
            messages=messages,
            temperature=kwargs.get("temperature", settings.LLM_TEMPERATURE),
            max_tokens=kwargs.get("max_tokens", settings.LLM_MAX_TOKENS),
        )
        return response.choices[0].message.content

    async def stream_chat_completion(self, messages: List[Dict[str, str]], **kwargs):
        # Implementation for streaming
        pass
