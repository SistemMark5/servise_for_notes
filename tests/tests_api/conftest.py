import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from notes import Note
from src.notes import db_helper


@pytest_asyncio.fixture()
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test/",
    ) as client:
        yield client

@pytest.fixture
def json_model():
    return {
        "title": "Hello World!",
        "text": "Hello World!"
    }

@pytest_asyncio.fixture(autouse=True)
async def override_db_session(session, monkeypatch):
    async def _get_test_session():
        return session
    monkeypatch.setattr(db_helper, "session_dependency", _get_test_session)
    yield

@pytest_asyncio.fixture
async def note_factory(session: AsyncSession):
    async def _create_user(title: str, text: str):
        note = Note(title=title, text=text)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    return _create_user