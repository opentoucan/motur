from hishel import Controller, AsyncRedisStorage, AsyncInMemoryStorage, AsyncCacheTransport, AsyncBaseStorage
from httpx import AsyncHTTPTransport
from pydantic import BaseModel
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, YamlConfigSettingsSource

class VehicleSettings(BaseSettings):
  mot_client_id: str
  mot_tenant_id: str
  mot_client_secret: str
  mot_api_key: str
  ves_api_key: str

class ScraperSettings(BaseModel):
    chrome_binary_location: str
    disable_sandbox: bool
    image_path: str

class RedisSettings(BaseModel):
    enabled: bool = False
    host: str = "localhost"
    port: int = 6379

class Settings(BaseSettings):
    model_config = SettingsConfigDict(yaml_file="config.yaml")

    enabled_sites: list[str]
    scraper: ScraperSettings
    redis: RedisSettings | None = None

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (YamlConfigSettingsSource(settings_cls), )

settings = Settings() # type: ignore

def GetHishelTransport():
    import redis.asyncio as redis
    storage = AsyncBaseStorage()
    redis_settings = RedisSettings() # type: ignore
    if settings.redis is not None and settings.redis.enabled:
        storage = AsyncRedisStorage(client=redis.Redis(host=redis_settings.host,port=redis_settings.port), ttl=300) # type: ignore
    else:
        storage = AsyncInMemoryStorage(capacity=64)
    transport = AsyncCacheTransport(
        transport=AsyncHTTPTransport(),
        storage=storage,
        controller=Controller(
            cacheable_methods=["GET", "POST"],
            cacheable_status_codes=[200],
            allow_stale=True,
            always_revalidate=False,
            force_cache=True,
        )
    )
    return transport
