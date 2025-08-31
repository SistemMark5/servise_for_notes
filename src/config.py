from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

class PathTemplates(BaseModel):
    templates_path: str = BASE_DIR / "src" / "templates"
    static_path: str = BASE_DIR / "src" / "static"

class DataBaseConfig(BaseModel):
    url: str
    mode: str
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
