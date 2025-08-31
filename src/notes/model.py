from datetime import datetime

from sqlalchemy import Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src.notes.base import Base


class Note(Base):
    __tablename__ = "notes"

    title: Mapped[str]
    text: Mapped[str] = mapped_column(Text)
    date_post: Mapped[datetime] = mapped_column(server_default=func.now())
