from pydantic import BaseModel, Field, ConfigDict


class CreateNote(BaseModel):
    title: str
    text: str


class ReadNote(CreateNote):
    pass


class AddNote(CreateNote):
    id: int

    # model_config = ConfigDict(
    #     from_attributes=True,
    # )
