from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_async_engine(
    settings.DB_URL,
    future=True,
    echo=settings.DB_DEBUG,
    pool_pre_ping=True,
    pool_use_lifo=True,
    pool_recycle=settings.DB_POOL_RECYCLE,
)

session_local = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
