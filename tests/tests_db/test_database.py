import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from models.repository import TaskRepository
from models.schemas import CreateNote


@pytest.mark.asyncio
async def test_create_note(session: AsyncSession):
    async with session:
        note_data = CreateNote(
            title="Hello World!",
            text="Hello World!",
        )
        response = await TaskRepository.create_note(session=session, note=note_data)
        assert response.get("title") == "Hello World!"

