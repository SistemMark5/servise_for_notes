from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_helper
from src.models.repository import TaskRepository
from src.models.dependency import get_by_title
from src.models.schemas import CreateNote, AddNote

router = APIRouter(
    tags=["Note"],
    prefix="/notes",
)


@router.post("/create-note")
async def create_note(
    note: CreateNote,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await TaskRepository.create_note(note=note, session=session)
    return {"ok": True}


@router.get("/get-note-by-title/{title}")
async def get_note_by_title(note: AddNote = Depends(get_by_title)):
    return note


@router.get("/get-all-notes")
async def get_all_notes(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    response = await TaskRepository.get_all_note(session=session)
    return response
