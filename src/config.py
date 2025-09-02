from pydantic import BaseModel
from pydantic_settings import BaseSettings, EnvSettingsSource, PydanticBaseSettingsSource, SettingsConfigDict, YamlConfigSettingsSource

class Settings(BaseSettings):
    class Scraper(BaseModel):
        chrome_binary_location: str
        disable_sandbox: bool
        image_path: str

    model_config = SettingsConfigDict(yaml_file="config.yaml", env_nested_delimiter="__")
    enabled_sites: list[str]
    scraper: Scraper

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (init_settings, YamlConfigSettingsSource(settings_cls), EnvSettingsSource(settings_cls) )
