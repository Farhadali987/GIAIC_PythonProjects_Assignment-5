from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "KisanAI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str
    
    # Clerk
    CLERK_JWT_KEY: str
    CLERK_SECRET_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
