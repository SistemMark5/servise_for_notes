from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.notes import Note
from src.notes.schemas import CreateNote, AddNote, UpdateNote


class NoteRepository:

    @classmethod
    async def create_note(cls, note: CreateNote, session: AsyncSession):
        task = note.model_dump()
        stmt = Note(**task)
        session.add(stmt)
        await session.commit()
        return task

    @classmethod
    async def get_note_for_title(cls, title: str, session: AsyncSession):
        stmt = select(Note).where(Note.title == title)
        result = await session.execute(stmt)
        note = result.scalars().first()
        return note

    @classmethod
    async def get_all_note(cls, session: AsyncSession):
        stmt = select(Note)
        result = await session.execute(stmt)
        all_note = result.scalars().all()
        return all_note

    @classmethod
    async def get_note_for_id(cls, session: AsyncSession, id: int):
        stmt = select(Note).where(Note.id == id)
        result = await session.execute(stmt)
        return result.scalars().first()

    @classmethod
    async def delete_note(cls, session: AsyncSession, note: AddNote):
        await session.delete(note)
        await session.commit()

    @classmethod
    async def delete_all(cls, session: AsyncSession):
        stmt = delete(Note)
        await session.execute(stmt)
        await session.commit()

    @classmethod
    async def update_note(
        cls,
        session: AsyncSession,
        note_update: UpdateNote,
        note_in: AddNote,
    ):
        for key, value in note_update.model_dump().items():
            setattr(note_in, key, value)
        await session.commit()
        return note_update
