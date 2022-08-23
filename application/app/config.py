from pydantic import BaseSettings, AnyUrl


class GlobalConfig(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_URL: AnyUrl = "postgresql+asyncpg://user:password@$localhost/$db"
    DB_URL_SYNC: AnyUrl = "postgresql://user:password@$localhost/$db"
    DB_URL_TEST: AnyUrl = "postgresql://user:password@$localhost/$db"
    DB_DEBUG: bool
    DB_POOL_RECYCLE: int = 0


settings = GlobalConfig()
