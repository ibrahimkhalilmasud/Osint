from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "OSINT Aggregation Platform"
    environment: str = Field(default="development", alias="ENVIRONMENT")
    jwt_secret: str = Field(default="change-me", alias="JWT_SECRET")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(default=60, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    default_phone_region: str = Field(default="US", alias="DEFAULT_PHONE_REGION")
    redis_url: str = Field(default="redis://redis:6379/0", alias="REDIS_URL")
    neo4j_uri: str = Field(default="bolt://neo4j:7687", alias="NEO4J_URI")
    neo4j_user: str = Field(default="neo4j", alias="NEO4J_USER")
    neo4j_password: str = Field(default="neo4jpassword", alias="NEO4J_PASSWORD")
    tor_socks_proxy: str = Field(default="", alias="TOR_SOCKS_PROXY")

    class Config:
        case_sensitive = False


settings = Settings()
