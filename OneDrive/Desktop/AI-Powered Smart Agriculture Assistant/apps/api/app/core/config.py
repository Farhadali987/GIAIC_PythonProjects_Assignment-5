from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "KisanAI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str
    
    # LLM
    LLM_PROVIDER: str = "qwen"
    QWEN_API_KEY: str
    GEMINI_API_KEY: Optional[str] = None
    # External APIs
    OPEN_METEO_BASE_URL: str = "https://api.open-meteo.com/v1"
    CLOUDINARY_URL: str
    HUGGING_FACE_API_KEY: str
    
    # Provider Settings
    API_TIMEOUT: int = 10
    API_MAX_RETRIES: int = 3
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
