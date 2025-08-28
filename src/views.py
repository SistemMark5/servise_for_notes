from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from urllib3 import HTTPResponse

from models import Note
from src.models import db_helper
from src.models.repository import TaskRepository
from src.models.dependency import get_by_title, get_by_id
from src.models.schemas import CreateNote, AddNote
from src.utils.template import template
from fastapi.responses import RedirectResponse

router = APIRouter(
    tags=["Note"],
    prefix="/notes",
)


@router.post("/create-note")
async def create_note(
    request: Request,
    title: str = Form(...),
    text: str = Form(...),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    note = Note(title=title, text=text)
    await TaskRepository.create_note(note=note, session=session)
    return RedirectResponse(url="/notes", status_code=303)


@router.get("/get-note-by-title/{title}")
async def get_note_by_title(note: AddNote = Depends(get_by_title)):
    return note


@router.get("/{note_id}/")
async def get_note_by_id(
    request: Request,
    note_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    note = await TaskRepository.get_note_for_id(session=session, id=note_id)
    return template.TemplateResponse(
        request=request, name="note.html", context={"note": note}
    )


@router.get("/")
async def get_all_notes(
    request: Request,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    notes = await TaskRepository.get_all_note(session=session)
    return template.TemplateResponse(
        request=request, name="index.html", context={"notes": notes}
    )


@router.delete("/delete/{note_id}")
async def delete_note(
    request: Request,
    note: AddNote = Depends(get_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await TaskRepository.delete_note(note=note, session=session)
    return template.TemplateResponse(request=request, name="index.html")
