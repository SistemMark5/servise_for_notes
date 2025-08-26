from fastapi import Path, HTTPException, status
from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_helper
from src.models.repository import TaskRepository


async def get_by_title(
    title: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    response = await TaskRepository.get_note_for_title(title=title, session=session)
    if response is not None:
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )
