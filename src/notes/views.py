from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession

from notes.schemas import UpdateNote
from src.notes import db_helper
from src.notes.crud import NoteRepository
from src.notes.dependency import get_by_title, get_by_id
from src.notes.schemas import CreateNote, AddNote
from src.utils.template import template
from fastapi.responses import RedirectResponse

router = APIRouter(
    tags=["Note"],
    prefix="/notes",
)


@router.post("/create-note")
async def create_note(
    title: str = Form(...),
    text: str = Form(...),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    note = CreateNote(title=title, text=text)
    await NoteRepository.create_note(note=note, session=session)
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
    note = await NoteRepository.get_note_for_id(session=session, id=note_id)
    return template.TemplateResponse(
        request=request, name="note.html", context={"note": note}
    )


@router.get("/")
async def get_all_notes(
    request: Request,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    notes = await NoteRepository.get_all_note(session=session)
    return template.TemplateResponse(
        request=request, name="index.html", context={"notes": notes}
    )


@router.delete("/delete/{note_id}")
async def delete_note(
    request: Request,
    note: AddNote = Depends(get_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await NoteRepository.delete_note(note=note, session=session)
    return template.TemplateResponse(request=request, name="index.html")


@router.delete("/delete-all")
async def delete_all_notes(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await NoteRepository.delete_all(session=session)
    return {"ok": True}


@router.put("/update-note/{note_id}")
async def update_note(
    note_update: UpdateNote,
    note_in: AddNote = Depends(get_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await NoteRepository.update_note(
        note_in=note_in, note_update=note_update, session=session
    )
    return {"ok": True}
