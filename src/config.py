from hishel import Controller, AsyncRedisStorage, AsyncInMemoryStorage, AsyncCacheTransport, AsyncBaseStorage
from httpx import AsyncHTTPTransport
from pydantic import BaseModel
from pydantic_settings import BaseSettings, EnvSettingsSource, PydanticBaseSettingsSource, SettingsConfigDict, YamlConfigSettingsSource



class Settings(BaseSettings):
    class MotApi(BaseModel):
        client_id: str
        tenant_id: str
        client_secret: str
        api_key: str

    class VesApi(BaseModel):
        api_key: str

    class ScraperSettings(BaseModel):
        chrome_binary_location: str
        disable_sandbox: bool
        image_path: str

    class Redis(BaseModel):
        enabled: bool = False
        host: str = "localhost"
        port: int = 6379
        password: str

    model_config = SettingsConfigDict(yaml_file="config.yaml", env_prefix="MOTUR__", env_nested_delimiter="__")
    mot_api: MotApi
    ves_api: VesApi
    enabled_sites: list[str]
    scraper: ScraperSettings
    redis: Redis | None = None

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (YamlConfigSettingsSource(settings_cls), EnvSettingsSource(settings_cls) )

settings = Settings() # type: ignore

def GetHishelTransport():
    import redis.asyncio as redis
    storage = AsyncBaseStorage()
    if settings.redis is not None and settings.redis.enabled:
        storage = AsyncRedisStorage(client=redis.Redis(host=settings.redis.host,port=settings.redis.port, password=settings.redis.password), ttl=300) # type: ignore
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
