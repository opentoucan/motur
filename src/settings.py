from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    client_id: str
    tenant_id: str
    client_secret: str
    api_key: str
