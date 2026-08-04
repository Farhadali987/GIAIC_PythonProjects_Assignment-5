import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from app.services.providers.base import BaseProvider
from app.core.config import settings

class WeatherProvider(BaseProvider):
    def __init__(self):
        super().__init__(api_key="", timeout=settings.API_TIMEOUT, max_retries=settings.API_MAX_RETRIES)
        self.base_url = settings.OPEN_METEO_BASE_URL

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def get_data(self, lat: float, lon: float) -> Any:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}/forecast",
                params={"latitude": lat, "longitude": lon, "current_weather": True}
            )
            response.raise_for_status()
            return response.json()
