from pydantic import BaseModel
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, YamlConfigSettingsSource

class MotSettings(BaseSettings):
  mot_client_id: str
  mot_tenant_id: str
  mot_client_secret: str
  mot_api_key: str

class ScraperSettings(BaseModel):
    chrome_binary_location: str
    disable_sandbox: bool
    image_path: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(yaml_file="config.yaml")

    enabled_sites: list[str]
    scraper: ScraperSettings

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
mot_settings = MotSettings() # type: ignore
