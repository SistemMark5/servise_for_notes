import pytest
from requests import session
from sqlalchemy.ext.asyncio import AsyncSession

from notes.crud import NoteRepository
from notes.schemas import CreateNote, UpdateNote, AddNote


@pytest.mark.asyncio
async def test_create_note(session: AsyncSession):
    async with session:
        note_data = CreateNote(
            title="Hello World!",
            text="Hello World!",
        )
        response = await NoteRepository.create_note(session=session, note=note_data)
        assert response.get("title") == "Hello World!"


@pytest.mark.asyncio
async def test_get_note_for_title(session: AsyncSession):
    async with session:
        title = "Hello World!"
        response = await NoteRepository.get_note_for_title(session=session, title=title)
        assert response.title == title


@pytest.mark.asyncio
async def test_for_get_note_by_id(session: AsyncSession):
    async with session:
        note_id = 1
        response = await NoteRepository.get_note_for_id(session=session, id=note_id)
        assert response.id is not None and response.id == note_id


@pytest.mark.asyncio
async def test_delete_note(session: AsyncSession):
    async with session:
        note_id = 1
        note = await NoteRepository.get_note_for_id(session=session, id=note_id)
        response = await NoteRepository.delete_note(session=session, note=note)
        assert response is None


@pytest.mark.asyncio
async def test_update_note_operation(session: AsyncSession):
    note_in = AddNote(
        id = 1,
        title="Hello!",
        text="Hello!",
    )
    note_update = UpdateNote(
        title="Hello World!",
        text="Hello World!",
    )
    response = await NoteRepository.update_note(session=session, note_in=note_in, note_update=note_update)
    assert response == note_update