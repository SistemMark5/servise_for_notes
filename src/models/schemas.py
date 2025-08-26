from pydantic import BaseModel, Field


class CreateNote(BaseModel):
    title: str = Field(title="Заголовок заметки")
    text: str = Field(title="Текст заметки")

    class Config:
        from_attributes = True


class ReadNote(CreateNote):
    pass


class AddNote(CreateNote):
    id: int

    class Config:
        from_attributes = True
