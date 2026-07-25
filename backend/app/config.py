from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list[str] = [""
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/images"

    class Config:
        envfile = ".env"

settings = Settings() 