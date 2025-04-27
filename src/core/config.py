import os
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    PROJECT_NAME: str = "base-project-fastapi"
    PROJECT_VERSION: str = "0.0.0"

    BASE_DIR = Path(__file__).resolve().parent.parent


settings = Settings()