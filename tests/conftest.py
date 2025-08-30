from src.config import settings
from src.models import Base

import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool


# Фикстура engine с session scope
@pytest_asyncio.fixture(scope="session")
async def engine():
    engine = create_async_engine(
        url=settings.db.DATABASE_URL_asyncpg,
        poolclass=NullPool,
        echo=False,
    )
    yield engine
    await engine.dispose()


# Фикстура для инициализации БД (без зависимости от event_loop)
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db(engine):
    assert settings.db.MODE == "TEST"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# Фикстура сессии (function scope)
@pytest_asyncio.fixture
async def session(engine):
    async with async_sessionmaker(engine, expire_on_commit=False)() as session:
        yield session
