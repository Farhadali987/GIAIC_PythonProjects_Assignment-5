from app.core.config import settings
from app.ai.llm.base import BaseLLMProvider
from app.ai.llm.qwen import QwenProvider

class LLMServiceFactory:
    @staticmethod
    def get_provider() -> BaseLLMProvider:
        if settings.LLM_PROVIDER == "qwen":
            return QwenProvider()
        # Add Gemini implementation later
        raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")
