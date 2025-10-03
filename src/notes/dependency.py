from fastapi import Path, HTTPException, status
from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.notes import db_helper
from src.notes.crud import NoteRepository


async def get_by_title(
    title: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    response = await NoteRepository.get_note_for_title(title=title, session=session)
    if response is not None:
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )


async def get_by_id(
    note_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    note = await NoteRepository.get_note_for_id(id=note_id, session=session)
    if note is not None:
        return note
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Note is not found",
    )
