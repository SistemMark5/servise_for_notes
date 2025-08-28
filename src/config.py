from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

class PathTemplates(BaseModel):
    templates_path: str = BASE_DIR / "src" / "templates"
    static_path: str = BASE_DIR / "src" / "static"

class DataBaseConfig(BaseModel):
    MODE: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self) -> str:
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    echo: bool = False


class Settings(BaseSettings):
    templates: PathTemplates = PathTemplates()
    db: DataBaseConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="CONFIG__",
    )


# noinspection PyArgumentList
settings = Settings()
