import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_note(client: AsyncClient, json_model):
    response = await client.post("/notes/create-note", data=json_model)
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_get_all_notes(client: AsyncClient):
    response = await client.get("/notes")
    assert response.status_code == 307

@pytest.mark.asyncio
async def test_get_note_for_id(client: AsyncClient, note_factory):
    note = await note_factory(title="Hello World!", text="Hello World!")
    response = await client.get(f"/notes/{note.id}")
    assert response.status_code == 307