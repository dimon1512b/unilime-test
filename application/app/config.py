from flask_caching import Cache
from pydantic import BaseSettings


class GlobalConfig(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_URL: str
    DB_URL_SYNC: str
    DB_DEBUG: bool
    DB_POOL_RECYCLE: int = 0


settings = GlobalConfig()
